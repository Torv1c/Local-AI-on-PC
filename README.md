# Local-AI-on-PC
# 🤖 Buddy: Assistente de Voz Local (LLM + TTS Clonagem)

Um assistente virtual 100% local e offline, integrando modelos de linguagem (Ollama/Llama 3) com clonagem de voz Zero-Shot (XTTSv2) para interações com personalidades customizadas (ex: personagens de jogos).

## 🚀 Como funciona
O projeto foi evoluindo para remover gargalos de roteamento de áudio (como o uso de VB-Cables e softwares externos como o RVC). Agora, ele opera de forma *clean*:
1. **Ollama (Llama 3):** Gera respostas inteligentes baseadas em um prompt de personalidade estrito.
2. **Coqui XTTSv2:** Clona a voz de qualquer personagem a partir de um áudio de referência de 5 segundos, gerando a fala com emoção diretamente no Python.

## 🛠️ Requisitos
* Python 3.10 ou 3.11 (Não use versões super recentes como 3.14).
* Placa de vídeo Nvidia (Testado em 16GB VRAM).
* Ollama instalado e rodando localmente.

## ⚙️ Como usar
1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`
3. Coloque um arquivo de áudio limpo de 5 a 10 segundos chamado `referencia.wav` na raiz do projeto.
4. Rode o script principal.

*Nota: Os modelos pesados do XTTS serão baixados automaticamente na primeira execução.*
