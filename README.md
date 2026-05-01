# Buddy: Local Voice Assistant (LLM + TTS Cloning)

A 100% local and offline virtual assistant, integrating large language models (Ollama/Llama 3) with Zero-Shot voice cloning (XTTSv2) for interactions with customized personalities (e.g., game characters).

## How it works
This project evolved to eliminate audio routing bottlenecks (such as relying on VB-Cables and external software like RVC). Now, it operates in a *clean* architecture:
1. **Ollama (Llama 3):** Generates intelligent responses based on a strict personality prompt.
2. **Coqui XTTSv2:** Clones any character's voice from a simple 5-second reference audio, generating speech with emotion directly within Python.

## Requirements
* Python 3.10 or 3.11 (Avoid super recent versions like 3.14 due to PyTorch compatibility).
* Nvidia Graphics Card (Tested on a 16GB VRAM GPU).
* Ollama installed and running locally.

## How to use
1. Clone the repository.
2. Install the dependencies: `pip install -r requirements.txt`
3. Place a clean 5 to 10-second audio file named `reference.wav` in the root directory.
4. Run the main script.

*Note: The heavy XTTS models will be downloaded automatically on the first run.*
