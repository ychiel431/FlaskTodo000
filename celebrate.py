import os
import time
import winsound

signal_file = "success_signal.txt"
sound_file = "celebrate.wav"
duration_seconds = 15

print("🎉 Celebrate.py רץ ברקע וממתין לסיגנל מה-Workflow...")

# מחכה עד שהסיגנל יופיע
while not os.path.exists(signal_file):
    time.sleep(1)

print(f"✅ סיגנל זוהה! נשמיע את הצליל למשך {duration_seconds} שניות 🎶")

winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
time.sleep(duration_seconds)
winsound.PlaySound(None, winsound.SND_PURGE)

os.remove(signal_file)
print("🎊 Celebrate הסתיים 🎊")
