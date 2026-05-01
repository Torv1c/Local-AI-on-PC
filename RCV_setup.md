# 🎭 Alternative Setup: RVC Voice Masking & Virtual Cables

While the main branch of this project uses **XTTSv2** for direct zero-shot voice cloning, earlier versions (and lighter setups) relied on real-time voice conversion using **RVC (Retrieval-based Voice Conversion)** and virtual audio routing. 

This method is recommended for users with less VRAM who still want high-quality character voices.

## ⚙️ How the "Voice Mask" Architecture Works
Instead of generating the character's voice directly, we use a basic TTS (like Microsoft Edge-TTS) to generate a neutral voice, and then "mask" it in real-time.

1. **Python (Edge-TTS):** Generates the base audio (e.g., a neutral male voice).
2. **Audio Routing:** Python sends this audio to a **Virtual Audio Cable** (e.g., VB-Cable) instead of the default speakers.
3. **RVC GUI:** Listens to the Virtual Cable, applies the character's `.pth` voice model in real-time, and outputs the final audio to your headset.

## 🛠️ Required Tools
* **[VB-Audio Virtual Cable](https://vb-audio.com/Cable/):** To route the audio between Python and RVC.
* **RVC Local Setup:** Any local fork of RVC WebUI (e.g., Mangio-RVC) running the real-time GUI.
* **Character Models:** The `.pth` (weights) and `.index` files of your desired character.

## 🎛️ Recommended RVC Settings for Best Quality
To avoid robotic or "scratchy" audio during real-time conversion, configure your RVC GUI as follows:
* **Pitch Extraction Algorithm:** `rmvpe` (Best clarity, removes robotic artifacts).
* **Index Rate:** `0.70` (Brings out the character's original accent and nuances).
* **Pitch Settings:** 
  * `+12` for high-pitched characters (e.g., Veigar).
  * `-5` to `-12` for deep-voiced characters (e.g., Blitzcrank).
* **Sample Length / Delay:** `0.50` (Balances processing speed and audio stability).

## 💻 Python Code Modification
To use this setup, change the output device in your `buddy.py` script to match the Virtual Cable input (usually device ID `9` for MME Virtual Cable):
```python
import sounddevice as sd
# 9 = CABLE Input (VB-Audio Virtual Cable)
sd.play(audio_data, sample_rate, device=9)