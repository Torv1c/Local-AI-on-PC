import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel
import keyboard
import ollama
import time
import asyncio
import edge_tts
import pygame
import os

# --- Configuração de Voz e Áudio ---
pygame.mixer.init()
# O Antônio será a voz do Veigar (infelizmente não temos a voz original do LoL aqui haha)
VOZ = "pt-BR-AntonioNeural" 

async def gerar_e_salvar_voz(texto, arquivo_saida):
    communicate = edge_tts.Communicate(texto, VOZ)
    await communicate.save(arquivo_saida)

# --- Configuração do Fifine ---
sd.default.device = 45, None

print("Iniciando sistemas do Pequeno Mestre do Mal...")
print("1. Carregando os Ouvidos (Whisper)...")
modelo_ouvido = WhisperModel("small", device="cpu", compute_type="int8")

print("2. Conectando ao Cérebro (Ollama / Llama 3)...")
ollama.generate(model='llama3', prompt='Apenas diga "ok"')

print("\n=======================================================")
print("✅ Buddy ONLINE! Pressione [Ctrl + ;] para INICIAR a gravação.")
print("   (Para encerrar o assistente, clique no terminal e aperte Ctrl+C)")
print("=======================================================\n")

taxa_amostragem = 48000  # Ou 48000, que é o padrão do Fifine
limite_tempo = 60

while True:
    keyboard.wait('ctrl+;') 
    print("\n🎤 [Gravando...] Pressione [Ctrl + ;] novamente para PARAR.")
    
    audio = sd.rec(int(limite_tempo * taxa_amostragem), samplerate=taxa_amostragem, channels=2, dtype='float32')
    tempo_inicio = time.time()
    time.sleep(0.5) 
    
    keyboard.wait('ctrl+;')
    sd.stop()

    audio = audio[:, 0].flatten()
    tempo_final = time.time()
    
    print("⏳ [Processando a sua voz...]")
    time.sleep(0.5)
    
    tempo_falado = tempo_final - tempo_inicio
    audio_recortado = audio[:int(tempo_falado * taxa_amostragem)]
    
    sf.write("temp_voz.wav", audio_recortado, taxa_amostragem)
    segmentos, _ = modelo_ouvido.transcribe("temp_voz.wav", language="pt")
    
    texto_falado = "".join([segmento.text for segmento in segmentos]).strip()
    
    if texto_falado != "":
        print(f"Você: {texto_falado}")
        print("🧠 Buddy pensando...")
        
        # A sua instrução de personalidade, mas bloqueando os símbolos para o leitor de voz não bugar
        prompt_personalidade = (
            "Descreva a personalidade "
            f"O usuário disse o seguinte, responda em português: {texto_falado}"
        )
        
        resposta = ollama.generate(model='llama3', prompt=prompt_personalidade)
        texto_resposta = resposta['response']
        
        print(f"Buddy: {texto_resposta}")
        
        # --- A Mágica da Voz Realista ---
        arquivo_mp3 = f"resposta_{int(time.time())}.mp3"
        
        # Gera o áudio
        asyncio.run(gerar_e_salvar_voz(texto_resposta, arquivo_mp3))
        
        # --- A Mágica da Voz Realista (Versão Forçada no Cabo) ---
        print("🔊 Enviando voz para o RVC...")
        
        # 1. Gera o áudio
        asyncio.run(gerar_e_salvar_voz(texto_resposta, "temp_voz.mp3"))
        
        # 2. Lê o áudio gerado
        import soundfile as sf
        dados, freq = sf.read("temp_voz.mp3")
        
        # 3. Toca no Dispositivo 35 (CABLE Input) em vez do padrão
        # Se der erro aqui, verifique se o número do 'CABLE Input' ainda é 35
        sd.play(dados, freq, device=9)
        sd.wait() # Espera o Veigar terminar de falar
        
        # 4. Limpeza
        os.remove("temp_voz.mp3")
        
    else:
        print("❌ Não escutei nada. Pressione [Ctrl + ;] para tentar novamente.")
