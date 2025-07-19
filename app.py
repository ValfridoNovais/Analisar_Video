import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI
from moviepy.editor import VideoFileClip
from datetime import datetime
import fitz  # PyMuPDF

# === CONFIGURAÇÃO DE AMBIENTE ===
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Diretório base do projeto
BASE_DIR = r"C:\Repositorios_GitHube\MeusProjetos\Analisar_Video"

# Estrutura de pastas
PASTAS = {
    "videos": os.path.join(BASE_DIR, "videos"),
    "audios": os.path.join(BASE_DIR, "audios"),
    "trancricoes": os.path.join(BASE_DIR, "trancricoes"),
    "resposta": os.path.join(BASE_DIR, "resposta")
}

# === FUNÇÕES (sem alterações aqui) ===
def extrair_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path, codec='mp3')
    return audio_path

def transcrever_whisper(audio_path):
    with open(audio_path, "rb") as f:
        resposta = client.audio.transcriptions.create(model="whisper-1", file=f)
    return resposta.text

def carregar_contexto_pdf(pdf_path):
    try:
        with fitz.open(pdf_path) as doc:
            texto_completo = "".join(page.get_text() for page in doc)
        return texto_completo
    except Exception as e:
        st.error(f"Erro ao ler o arquivo PDF de contexto: {e}")
        return None

def analisar_trabalho(transcricao, fardamento, leitura, contexto_pdf):
    prompt = f"""
Você é um membro da banca avaliadora do Curso Especial de Formação de Sargentos (CEFS) da PMMG.
Sua tarefa é avaliar uma instrução em vídeo gravada por um aluno, usando estritamente as regras e critérios definidos no documento oficial do curso.

---
CONTEXTO - DOCUMENTO OFICIAL DO TRABALHO (Roteiro e Barema):
\"\"\"
{contexto_pdf}
\"\"\"
---

AVALIAÇÃO DO ALUNO:

1. TRANSCRIÇÃO DO VÍDEO DO ALUNO:
\"\"\"
{transcricao}
\"\"\"

2. OBSERVAÇÕES DO AVALIADOR HUMANO:
- Fardamento utilizado: {fardamento}
- Grau de leitura observado (0=nenhuma, 5=total): {leitura}

---
SUA MISSÃO:

Com base na TRANSCRIÇÃO e nas OBSERVAÇÕES, e usando o DOCUMENTO OFICIAL como sua única fonte de regras, realize a seguinte análise.
Formate a saída exclusivamente com HTML, seguindo rigorosamente o padrão abaixo. Não adicione nenhum texto ou caractere fora das tags HTML.

<div>
  <p><strong>AVALIAÇÃO DA INSTRUÇÃO</strong></p>
  <p><strong>1. PONTUAÇÃO POR CRITÉRIO:</strong></p>
  <ul>
    <li><strong>Introdução e Relato do Tema:</strong> [Pontos] / 0,3</li>
    <li><strong>Explicação da Metodologia do Indicador:</strong> [Pontos] / 0,5</li>
    <li><strong>Domínio do Conteúdo (Evitar Leitura):</strong> [Pontos] / 0,3</li>
    <li><strong>Pertinência das Informações:</strong> [Pontos] / 0,3</li>
    <li><strong>Conclusão (Importância Profissional):</strong> [Pontos] / 0,3</li>
    <li><strong>Requisitos Formais (Tempo, Uniforme, Presença):</strong> [Pontos] / 0,3</li>
  </ul>
  <p><strong>2. NOTA FINAL:</strong><br><strong>[Nota Final] / 2,0</strong></p>
  <p><strong>3. ANÁLISE E FEEDBACK:</strong><br><strong>Pontos Fortes:</strong></p>
  <ul>
    <li>[Ponto positivo 1]</li>
    <li>[Ponto positivo 2]</li>
  </ul>
  <p><strong>Sugestões de Melhoria:</strong></p>
  <ul>
    <li>[Sugestão 1]</li>
    <li>[Sugestão 2]</li>
  </ul>
</div>
"""
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )
    return resposta.choices[0].message.content

def salvar_resposta(texto, nome_base):
    txt_path = os.path.join(PASTAS["resposta"], f"{nome_base}.txt")
    md_path = os.path.join(PASTAS["resposta"], f"{nome_base}.md")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(texto)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(texto)

# === INTERFACE STREAMLIT ===
st.set_page_config(page_title="Avaliador CEFS", layout="wide")
st.title("📊 Painel de Avaliação de Vídeos - CEFS")

# --- Interface dividida em colunas ---
col1, col2 = st.columns([1, 2])

# --- COLUNA 1: Ferramenta de Nova Análise ---
with col1:
    st.header("📝 Nova Análise")
    videos = [f for f in os.listdir(PASTAS["videos"]) if f.endswith((".mp4", ".mov", ".mkv"))]
    video_escolhido = st.selectbox("🎥 Selecione o vídeo:", videos, index=None, placeholder="Escolha um vídeo para avaliar...")

    if video_escolhido:
        fardamento = st.selectbox("👔 Fardamento:", ["Adequado", "Inadequado"])
        leitura = st.slider("📖 Grau de leitura:", 0, 5, 2)

        if st.button("▶️ Processar e Avaliar Vídeo"):
            # ... (Lógica de processamento que você já tem)
            video_path = os.path.join(PASTAS["videos"], video_escolhido)
            nome_base = os.path.splitext(video_escolhido)[0] + "_" + datetime.now().strftime("%Y%m%d%H%M")
            audio_path = os.path.join(PASTAS["audios"], nome_base + ".mp3")
            trans_path = os.path.join(PASTAS["trancricoes"], nome_base + ".txt")
            pdf_path = os.path.join(BASE_DIR, "CEFS_2025_Roteiro de trabalho (1).pdf")
            
            contexto_pdf = carregar_contexto_pdf(pdf_path)

            if contexto_pdf:
                with st.spinner("Processando..."):
                    extrair_audio(video_path, audio_path)
                    texto = transcrever_whisper(audio_path)
                    with open(trans_path, "w", encoding="utf-8") as f:
                        f.write(texto)
                    resultado = analisar_trabalho(texto, fardamento, leitura, contexto_pdf)
                    salvar_resposta(resultado, nome_base)
                
                st.success("Avaliação concluída e salva!")
                # Força um refresh para que a nova avaliação apareça na lista da direita
                st.rerun()

# --- COLUNA 2: Histórico Permanente de Avaliações ---
with col2:
    st.header("📜 Histórico de Avaliações Salvas")

    # Lista todos os arquivos .txt na pasta de respostas, do mais novo para o mais antigo
    try:
        arquivos_resposta = sorted(
            [f for f in os.listdir(PASTAS["resposta"]) if f.endswith(".txt")],
            key=lambda f: os.path.getmtime(os.path.join(PASTAS["resposta"], f)),
            reverse=True
        )
    except FileNotFoundError:
        st.error(f"A pasta de respostas não foi encontrada em: {PASTAS['resposta']}")
        arquivos_resposta = []

    if not arquivos_resposta:
        st.info("Nenhuma avaliação foi salva na pasta de respostas ainda.")
    else:
        # Cria um seletor para o usuário escolher qual avaliação ver
        arquivo_selecionado = st.selectbox(
            "Selecione uma avaliação para visualizar:",
            arquivos_resposta,
            index=None,
            placeholder="Escolha uma avaliação do histórico..."
        )

        # Se o usuário escolheu um arquivo, lê e exibe seu conteúdo
        if arquivo_selecionado:
            caminho_arquivo = os.path.join(PASTAS["resposta"], arquivo_selecionado)
            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                conteudo_avaliacao = f.read()
            
            st.markdown("---")
            st.subheader(f"Visualizando: {arquivo_selecionado}")
            st.markdown(conteudo_avaliacao, unsafe_allow_html=True)

            # Botão de download para o arquivo selecionado
            st.download_button(
                label="📥 Baixar esta avaliação (.txt)",
                data=conteudo_avaliacao,
                file_name=arquivo_selecionado
            )
