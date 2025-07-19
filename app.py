import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI
from moviepy.editor import VideoFileClip
from datetime import datetime

# === CONFIGURAÇÃO DE AMBIENTE ===
# Carrega variáveis do arquivo .env (ex: OPENAI_API_KEY)
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

# === FUNÇÃO 1: Extração de áudio do vídeo ===
def extrair_audio(video_path, audio_path):
    """
    Extrai o áudio de um vídeo (.mp4, .mov...) e salva como .wav
    """
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    return audio_path

# === FUNÇÃO 2: Transcrição com Whisper-1 (OpenAI API) ===
def transcrever_whisper(audio_path):
    """
    Usa o modelo 'whisper-1' da OpenAI para transcrever o áudio extraído.
    """
    with open(audio_path, "rb") as f:
        resposta = client.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )
    return resposta.text

# === FUNÇÃO 3: Envia a transcrição e inputs para análise por IA ===
def analisar_trabalho(transcricao, fardamento, leitura):
    """
    Gera avaliação textual e pontuação com base na transcrição, observações e barema CEFS.
    """
    prompt = f"""
Você é um avaliador do Curso Especial de Formação de Sargentos (CEFS).
Abaixo está a transcrição de um vídeo de apresentação de um aluno sobre indicadores da GDO.

Critérios de avaliação (máx. 2,0 pontos):
- Introdução e indicação do tema: 0 a 0,3
- Explicação da metodologia do indicador: 0 a 0,5
- Domínio do conteúdo (evitar leitura): 0 a 0,3
- Pertinência do conteúdo: 0 a 0,3
- Conclusão e importância profissional: 0 a 0,3
- Requisitos formais (tempo, uniforme, presença): 0 a 0,3

*Observação do avaliador sobre o vídeo:*
- Fardamento: {fardamento}
- Grau de leitura (0 a 5): {leitura} (0 = não leu, 5 = só leu o texto)

Transcrição do vídeo:
\"\"\"{transcricao}\"\"\"

Com base nos critérios e observações acima, forneça:
1. Nota final (máx. 2,0)
2. Pontuação por critério
3. Pontos fortes e sugestões de melhoria
"""
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",  # versão mais barata e eficiente
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return resposta.choices[0].message.content

# === FUNÇÃO 4: Salvar resposta em TXT e Markdown ===
def salvar_resposta(texto, nome_base):
    """
    Salva a análise gerada em .txt e .md na pasta de respostas.
    """
    txt_path = os.path.join(PASTAS["resposta"], f"{nome_base}.txt")
    md_path = os.path.join(PASTAS["resposta"], f"{nome_base}.md")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(texto)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(texto)

# === INTERFACE STREAMLIT ===
st.set_page_config(page_title="Avaliador CEFS", layout="centered")
st.title("📊 Avaliador de Vídeo - CEFS")

# Lista os vídeos disponíveis para análise
videos = [f for f in os.listdir(PASTAS["videos"]) if f.endswith((".mp4", ".mov", ".mkv"))]
video_escolhido = st.selectbox("🎥 Selecione o vídeo para análise:", videos)

if video_escolhido:
    # Caminhos e nomes baseados em timestamp
    video_path = os.path.join(PASTAS["videos"], video_escolhido)
    nome_base = os.path.splitext(video_escolhido)[0] + "_" + datetime.now().strftime("%Y%m%d%H%M")
    audio_path = os.path.join(PASTAS["audios"], nome_base + ".wav")
    trans_path = os.path.join(PASTAS["trancricoes"], nome_base + ".txt")

    # Inputs manuais: fardamento e grau de leitura
    fardamento = st.selectbox("👔 Fardamento utilizado:", ["Adequado", "Inadequado"])
    leitura = st.slider("📖 Grau de leitura (0 = não leu, 5 = só leu):", 0, 5, 2)

    # Botão principal de execução
    if st.button("▶️ Processar vídeo"):
        with st.spinner("🎞️ Extraindo áudio do vídeo..."):
            extrair_audio(video_path, audio_path)

        with st.spinner("🧠 Transcrevendo com Whisper..."):
            texto = transcrever_whisper(audio_path)
            with open(trans_path, "w", encoding="utf-8") as f:
                f.write(texto)

        with st.spinner("🤖 Gerando análise com GPT..."):
            resultado = analisar_trabalho(texto, fardamento, leitura)
            salvar_resposta(resultado, nome_base)

        # Interface final com downloads e texto
        st.success("✅ Avaliação concluída!")
        st.download_button("📥 Baixar resposta (.txt)", resultado, file_name=nome_base + ".txt")
        st.download_button("📥 Baixar resposta (.md)", resultado, file_name=nome_base + ".md")
        st.text_area("📋 Resultado da Análise:", resultado, height=400)
