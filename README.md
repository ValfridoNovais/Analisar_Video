# 🎓 Analisador de Vídeos - CEFS (Curso Especial de Formação de Sargentos)

Este projeto em Python com Streamlit automatiza a análise de vídeos submetidos por alunos do CEFS. Ele extrai o áudio, realiza transcrição com o modelo `whisper-1` da OpenAI e gera uma avaliação com base em critérios definidos no barema da disciplina de Análise Criminal. A análise é gerada via `gpt-4o-mini`, otimizando custo e desempenho.


```
TITULO 1: 🎓 Analisador de Vídeos - CEFS (Curso Especial de Formação de Sargentos)

Este projeto em Python utiliza Streamlit para criar uma interface web que automatiza a análise de vídeos submetidos por alunos do CEFS. A aplicação extrai o áudio do vídeo, realiza a transcrição com o modelo `whisper-1` da OpenAI e, em seguida, utiliza o `gpt-4o-mini` para gerar uma avaliação detalhada com base em critérios pré-definidos, otimizando o processo de correção e feedback.

---

TITULO 2: 🎯 Funcionalidades Principais

1.  **Interface Web Intuitiva:** Utiliza Streamlit para oferecer uma interface simples onde o avaliador pode selecionar o vídeo a ser analisado.
2.  **Extração e Compressão de Áudio:** O áudio do vídeo é extraído e salvo no formato **MP3**. Essa compressão é **essencial** para garantir que o arquivo de áudio não ultrapasse o limite de 25 MB da API do Whisper.
3.  **Transcrição Automática:** O arquivo de áudio é enviado para a API da OpenAI, que utiliza o modelo `whisper-1` para gerar uma transcrição textual precisa do discurso do aluno.
4.  **Inputs Manuais do Avaliador:** A interface permite que o avaliador humano insira observações que a IA não pode verificar pelo áudio, como:
    *   Adequação do fardamento.
    *   Grau de leitura observado durante a apresentação.
5.  **Análise com IA:** A transcrição e as observações manuais são enviadas ao modelo `gpt-4o-mini`, que atua como um avaliador virtual, gerando:
    *   Nota final (de 0 a 2,0).
    *   Pontuação detalhada por critério.
    *   Feedback com pontos fortes e sugestões de melhoria.
6.  **Armazenamento Organizado:** Todos os artefatos gerados (áudio, transcrição e avaliação final) são salvos em pastas específicas, com nomes de arquivo padronizados com data e hora para fácil rastreamento.

---

TITULO 2: 📁 Estrutura de Pastas

BLOCO DE CÓDIGO (bash):
Analisar_Video/
│
├── app.py                      # Aplicação principal (Streamlit)
├── .env                        # Contém a OPENAI_API_KEY (NÃO versionar)
├── .gitignore                  # Arquivos e pastas ignoradas pelo Git
├── README.md                   # Este arquivo
├── requirements.txt            # Dependências do projeto
│
├── videos/                     # (Entrada) Vídeos brutos (.mp4, .mov)
├── audios/                     # (Saída) Áudios extraídos e comprimidos (.mp3)
├── trancricoes/                # (Saída) Transcrições geradas (.txt)
├── resposta/                   # (Saída) Avaliações finais (.txt e .md)
└── venvVIDEOCEFS/              # Ambiente virtual do projeto (NÃO versionar)
FIM DO BLOCO DE CÓDIGO

---

TITULO 2: 🧪 Tecnologias Utilizadas

- **Python 3.9+**
- **Streamlit:** Para a interface web interativa.
- **OpenAI API:** Para transcrição (`whisper-1`) e avaliação (`gpt-4o-mini`).
- **MoviePy:** Para extração de áudio dos vídeos.
- **python-dotenv:** Para carregar a chave da API de forma segura a partir de um arquivo `.env`.

---

TITULO 2: 📦 Instalação e Execução

TITULO 3: 1. Pré-requisitos

- **Python** instalado.
- **FFmpeg:** `moviepy` depende do FFmpeg para processar áudio e vídeo. Se você não o tiver, pode instalá-lo a partir do [site oficial](https://ffmpeg.org/download.html) e garantir que ele esteja no PATH do seu sistema.

TITULO 3: 2. Configuração do Ambiente

Clone o repositório e crie o ambiente virtual:
BLOCO DE CÓDIGO (bash):
git clone <url_do_repositorio>
cd Analisar_Video
python -m venv venvVIDEOCEFS
# No Windows
venvVIDEOCEFS\Scripts\activate
# No macOS/Linux
# source venvVIDEOCEFS/bin/activate
FIM DO BLOCO DE CÓDIGO

TITULO 3: 3. Chave da API

Crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave da OpenAI:
BLOCO DE CÓDIGO:
OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
FIM DO BLOCO DE CÓDIGO

TITULO 3: 4. Instalação das Dependências

Instale as bibliotecas listadas no `requirements.txt`:
BLOCO DE CÓDIGO (bash):
pip install -r requirements.txt
FIM DO BLOCO DE CÓDIGO

> #### ⚠️ **Atenção à Versão do `moviepy`**
> O arquivo `requirements.txt` deve especificar **exatamente** a versão `moviepy==1.0.3`. Existe um fork não oficial da biblioteca com uma versão `2.x` que é frequentemente instalada por padrão pelo `pip`, mas que possui uma estrutura de módulos diferente e **causa erros** de importação (`ModuleNotFoundError: No module named 'moviepy.editor'`). Para garantir a compatibilidade, a versão deve ser fixada.

TITULO 3: 5. Execução da Aplicação

Com o ambiente virtual ativado, execute o Streamlit:
BLOCO DE CÓDIGO (bash):
streamlit run app.py
FIM DO BLOCO DE CÓDIGO
A aplicação será aberta no seu navegador.

---

TITULO 2: 🧾 Barema Aplicado (Peso Total: 2,0 pts)

| Critério | Faixa de Pontos |
| :--- | :--- |
| Introdução e indicação do tema | 0 a 0,3 |
| Explicação da metodologia do indicador | 0 a 0,5 |
| Domínio do conteúdo (sem leitura excessiva) | 0 a 0,3 |
| Pertinência do conteúdo ao tema | 0 a 0,3 |
| Conclusão e importância profissional | 0 a 0,3 |
| Requisitos formais (tempo, uniforme, presença) | 0 a 0,3 |

---

TITULO 2: 🔐 Segurança

- **NUNCA** envie seu arquivo `.env` para repositórios públicos.
- O arquivo `.gitignore` deste projeto já está configurado para ignorar o `.env`, o ambiente virtual e as pastas de mídia (`videos`, `audios`, etc.), protegendo dados sensíveis.

---

TITULO 2: 🧠 Autor

Desenvolvido por Valfrido Novais – [@valfridonovais](https://instagram.com/valfridonovais)  
Projetado para uso educacional no Curso Especial de Formação de Sargentos da PMMG.
```

**Instruções para reformatar:**
1.  Substitua `TITULO 1:` por `#`
2.  Substitua `TITULO 2:` por `##`
3.  Substitua `TITULO 3:` por `###`
4.  Substitua `BLOCO DE CÓDIGO (bash):` por ` ```bash `
5.  Substitua `BLOCO DE CÓDIGO:` por ` ``` `
6.  Substitua `FIM DO BLOCO DE CÓDIGO` por ` ``` `

Peço desculpas novamente pelo transtorno. Esta abordagem deve funcionar sem problemas.