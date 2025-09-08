import os
import time
import winsound

# קובץ סיגנל שמראה שהworkflow הצליח
signal_file = "success_signal.txt"

# קובץ WAV מקומי שלך
sound_file = "celebrate.wav"

# משך ההשמעה בשניות
duration_seconds = 16

print("🎉 Celebrate.py רץ ברקע וממתין לסיגנל...")

# דמו: נייצר את הסיגנל מיד כדי להדגים
if not os.path.exists(signal_file):
    print("יוצר סיגנל לדמו...")
    with open(signal_file, "w") as f:
        f.write("demo signal")

# מחכה עד שהסיגנל יופיע
while not os.path.exists(signal_file):
    time.sleep(1)

print(f"✅ סיגנל זוהה! נשמיע את הצליל למשך {duration_seconds} שניות 🎶")

# השמעת הצליל פעם אחת
winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)

# מחכים את משך הזמן הרצוי
time.sleep(duration_seconds)

# מפסיקים את הצליל
winsound.PlaySound(None, winsound.SND_PURGE)

# מסירים את קובץ הסיגנל
os.remove(signal_file)

print("🎊 דמו הסתיים 🎊")
