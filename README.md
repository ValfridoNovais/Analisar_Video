# 🎓 Analisador de Vídeos - CEFS (Curso Especial de Formação de Sargentos)

Este projeto em Python com Streamlit automatiza a análise de vídeos submetidos por alunos do CEFS. Ele extrai o áudio, realiza transcrição com o modelo `whisper-1` da OpenAI e gera uma avaliação com base em critérios definidos no barema da disciplina de Análise Criminal. A análise é gerada via `gpt-4o-mini`, otimizando custo e desempenho.

---

## 📁 Estrutura de Pastas

```bash
Analisar_Video/
│
├── app.py                      # Aplicação principal (Streamlit)
├── .env                        # Contém a OPENAI_API_KEY
├── .gitignore                  # Arquivos e pastas ignoradas no Git
├── requirements.txt            # Dependências do projeto
│
├── videos/                     # Vídeos brutos enviados pelos alunos (.mp4, .mov)
├── audios/                     # Áudios extraídos (.wav)
├── trancricoes/                # Transcrições geradas a partir dos áudios (.txt)
├── resposta/                   # Arquivos de avaliação gerados (.txt e .md)
└── venvVIDEOCEFS/              # Ambiente virtual do projeto
```

---

## 🧪 Tecnologias utilizadas

- **Python 3.9+**
- **Streamlit** – para interface web
- **OpenAI API** – para transcrição (`whisper-1`) e avaliação (`gpt-4o-mini`)
- **moviepy** – para extração do áudio dos vídeos
- **python-dotenv** – para carregar a chave da API com segurança

---

## 🔐 Configuração do `.env`

Crie um arquivo `.env` na raiz do projeto com sua chave da OpenAI:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 📦 Instalação e execução

1. **Clone o repositório ou crie a estrutura de diretórios manualmente.**

2. **Ative o ambiente virtual (caso não tenha):**
   ```bash
   python -m venv venvVIDEOCEFS
   venvVIDEOCEFS\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o app:**
   ```bash
   streamlit run app.py
   ```

---

## 🎯 Funcionalidades

1. **Seleção de vídeo:** usuário escolhe um arquivo da pasta `/videos`.
2. **Extração do áudio:** o vídeo é convertido em `.wav` na pasta `/audios`.
3. **Transcrição automática:** usando o `whisper-1` da OpenAI.
4. **Inputs manuais:**
   - Fardamento utilizado (Adequado / Inadequado)
   - Grau de leitura (0 a 5)
5. **Análise com IA:**
   - Enviada ao modelo `gpt-4o-mini`
   - Geração de nota final e pontuação por critério
6. **Resposta salva automaticamente:**
   - `.txt` e `.md` com nome: `nome_video_yyyymmddHHMM.*`
   - Armazenado na pasta `/resposta`

---

## 🧾 Barema aplicado na análise (peso total: 2,0 pts)

| Critério                                                    | Faixa de Pontos |
|-------------------------------------------------------------|------------------|
| Introdução e indicação do tema                              | 0 a 0,3          |
| Explicação da metodologia do indicador                      | 0 a 0,5          |
| Domínio do conteúdo (sem leitura excessiva)                 | 0 a 0,3          |
| Pertinência do conteúdo ao tema                             | 0 a 0,3          |
| Conclusão e importância profissional                        | 0 a 0,3          |
| Requisitos formais (tempo, uniforme, presença)              | 0 a 0,3          |

---

## 🔄 Observações sobre o uso

- A IA apenas avalia a transcrição. A leitura e o fardamento são indicados manualmente pelo avaliador.
- A duração do vídeo deve ser entre **60 e 180 segundos**. Verificações automáticas podem ser adicionadas.
- O nome base do vídeo será usado em todos os arquivos gerados.

---

## 🧾 Exemplo de dependências (`requirements.txt`)

```txt
streamlit
openai
moviepy
python-dotenv
```

---

## ✅ Exemplo de execução

1. Coloque um vídeo em `/videos`
2. Rode o sistema
3. Selecione o vídeo
4. Informe o fardamento e grau de leitura
5. Clique em “Processar vídeo”
6. Resultado será exibido e salvo em `/resposta`

---

## 🔐 Segurança

- **NUNCA** envie `.env`, `.wav` ou vídeos para repositórios públicos.
- O arquivo `.gitignore` já protege as pastas sensíveis.

---

## 🧠 Autor

Desenvolvido por Valfrido Novais – [@valfridonovais](https://instagram.com/valfridonovais)  
Projetado para uso educacional no Curso Especial de Formação de Sargentos da PMMG.

