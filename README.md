Com certeza! A sua preocupação é muito pertinente. Um bom `README` é a porta de entrada do projeto e, para compartilhar com colegas, ele precisa ser impecável, claro e completo.

Analisei o seu `README` atual e ele já é muito bom, mas podemos aprimorá-lo para refletir as últimas e mais importantes funcionalidades que você adicionou. As mudanças o deixarão mais claro para um usuário que está vendo o projeto pela primeira vez.

Abaixo está uma versão revisada e mais completa. Eu a coloquei dentro de um bloco de código para que você possa copiar e colar sem problemas de renderização.

### README.md Revisado e Pronto para Compartilhar

```markdown
# 🎓 Painel de Avaliação de Vídeos - CEFS

Este projeto em Python utiliza Streamlit para criar um painel de controle completo que automatiza e gerencia a análise de vídeos submetidos por alunos do Curso Especial de Formação de Sargentos (CEFS).

A aplicação lê o roteiro oficial do trabalho (em PDF) para garantir que as avaliações sejam precisas e consistentes. Ela extrai o áudio dos vídeos, transcreve com a API da OpenAI (`whisper-1`) e utiliza um modelo de linguagem (`gpt-4o-mini`) para gerar uma avaliação detalhada, que fica salva em um histórico permanente para consulta futura.

---

## 🎯 Funcionalidades Principais

-   **Análise Baseada em Documento Oficial:** O sistema utiliza um arquivo PDF como fonte da verdade, garantindo que a IA aplique exatamente os mesmos critérios e baremas que um avaliador humano.
-   **Painel de Controle Unificado:** A interface, dividida em colunas, permite realizar novas análises e consultar avaliações passadas no mesmo local.
-   **Histórico Permanente:** Todas as avaliações geradas são salvas na pasta `/resposta` e podem ser acessadas a qualquer momento através de um menu suspenso no painel.
-   **Extração e Compressão de Áudio:** O áudio é extraído dos vídeos e comprimido para o formato MP3, evitando erros de upload para a API da OpenAI (que tem um limite de 25 MB).
-   **Transcrição e Avaliação por IA:** Utiliza os modelos mais eficientes da OpenAI para transcrever o áudio e gerar uma análise formatada, com pontuação, nota final e feedback construtivo.
-   **Armazenamento Organizado:** Todos os arquivos gerados (áudios, transcrições, avaliações) são salvos em pastas dedicadas e nomeados com data e hora para fácil rastreamento.

---

## 📁 Estrutura de Pastas

```bash
Analisar_Video/
│
├── app.py                                  # Aplicação principal (Streamlit)
├── CEFS_2025_Roteiro de trabalho (1).pdf   # Documento base para a IA
├── .env                                    # Contém a OPENAI_API_KEY (NÃO versionar)
├── .gitignore                              # Arquivos e pastas ignoradas pelo Git
├── README.md                               # Este arquivo
├── requirements.txt                        # Dependências do projeto
│
├── videos/                                 # (Entrada) Vídeos brutos (.mp4, .mov)
├── audios/                                 # (Saída) Áudios extraídos e comprimidos (.mp3)
├── trancricoes/                            # (Saída) Transcrições geradas (.txt)
├── resposta/                               # (Saída) Avaliações salvas (.txt, .md)
└── venvVIDEOCEFS/                          # Ambiente virtual do projeto (NÃO versionar)
```

---

## 🧪 Tecnologias Utilizadas

-   **Python 3.9+**
-   **Streamlit:** Para a interface web interativa.
-   **OpenAI API:** Para transcrição (`whisper-1`) e avaliação (`gpt-4o-mini`).
-   **MoviePy:** Para extração de áudio dos vídeos.
-   **PyMuPDF:** Para extrair o texto do arquivo de roteiro em PDF.
-   **python-dotenv:** Para carregar a chave da API de forma segura.

---

## 📦 Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto em seu computador.

### 1. Pré-requisitos

-   **Python** instalado (versão 3.9 ou superior).
-   **FFmpeg:** `moviepy` depende do FFmpeg para processar mídias. Se não o tiver, instale a partir do [site oficial](https://ffmpeg.org/download.html) e garanta que ele esteja acessível no PATH do seu sistema.

### 2. Configuração do Ambiente

Primeiro, clone o repositório (ou baixe e extraia o ZIP) e crie um ambiente virtual para isolar as dependências.

```bash
# Opcional: Clone o repositório se estiver usando Git
git clone <url_do_repositorio>
cd Analisar_Video

# Crie e ative o ambiente virtual
python -m venv venvVIDEOCEFS

# No Windows:
venvVIDEOCEFS\Scripts\activate

# No macOS/Linux:
# source venvVIDEOCEFS/bin/activate
```

### 3. Chave da API da OpenAI

Crie um arquivo chamado `.env` na pasta raiz do projeto. Dentro dele, adicione sua chave da API da OpenAI.

```
OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### 4. Instalação das Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas necessárias de uma só vez usando o arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 🗒️ Comentários Adicionais do Avaliador

Durante a avaliação, o avaliador humano pode inserir observações manuais complementares, como:

- "A conclusão foi superficial e não abordou a importância do indicador"
- "O vídeo teve duração superior ao limite de 180 segundos"
- "O aluno demonstrou domínio oral, mesmo com pequenas pausas"

Essas informações são passadas diretamente ao modelo GPT para reavaliar os critérios e ajustar a pontuação, especialmente nos itens como **Conclusão** ou **Requisitos formais**.


> #### ⚠️ **Atenção à Versão do `moviepy`**
> O arquivo `requirements.txt` deste projeto já fixa a versão correta (`moviepy==1.0.3`). Isso é crucial porque a instalação padrão do `pip` pode buscar uma versão `2.x` de um fork não oficial, que causa erros de importação e quebra a aplicação.

### 5. Execução da Aplicação

Finalmente, execute o comando abaixo no terminal. O painel de controle será aberto automaticamente no seu navegador.

```bash
streamlit run app.py
```

---

## 🔏 Segurança e Privacidade

-   **NUNCA** envie seu arquivo `.env` para repositórios públicos ou compartilhe sua chave de API.
-   O arquivo `.gitignore` já está configurado para proteger pastas com dados sensíveis (vídeos, áudios, etc.) e arquivos de configuração.

---

## 🧠 Autor

Desenvolvido por Valfrido Novais – [@valfridonovais](https://instagram.com/valfridonovais)  
Projetado para uso educacional no Curso Especial de Formação de Sargentos da PMMG.
```