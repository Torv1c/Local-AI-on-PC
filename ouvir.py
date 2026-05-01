import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel

sd.default.device = 3  # Substitua pelo número do seu microfone (use sd.query_devices() para descobrir)

# 1. Preparando o "Ouvido" da IA
print("Carregando o modelo Whisper (isso pode demorar um pouco na primeira vez)...")
# Vamos usar o modelo "small", que é leve, rápido e muito bom em português
modelo = WhisperModel("small", device="cpu", compute_type="int8") 

# 2. Configurações do Microfone
duracao = 5  # Segundos que ele vai ficar gravando
taxa_amostragem = 16000  # Qualidade do áudio (16kHz é o padrão)

print(f"\n[!] Fale agora! Gravando sua voz por {duracao} segundos...")

# Liga o microfone e grava
audio = sd.rec(int(duracao * taxa_amostragem), samplerate=taxa_amostragem, channels=1, dtype='float32')
sd.wait() # Espera os 5 segundos passarem
print("[!] Gravação concluída. Processando o que você disse...")

# Salva o áudio em um arquivo temporário
sf.write("teste_voz.wav", audio, taxa_amostragem)

# 3. A Mágica: Transcrevendo o áudio para texto
segmentos, info = modelo.transcribe("teste_voz.wav", beam_size=5, language="pt")

print("\n=== RESULTADO DA TRANSCRIÇÃO ===")
for segmento in segmentos:
    print(f"Você disse: {segmento.text}")
print("================================")