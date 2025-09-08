import os
import time
import winsound
import subprocess
from plyer import notification

# -----------------------------
# הגדרות
# -----------------------------
repo_path = "C:/Users/LENOVO/Desktop/projects/FlaskTodo-main"
signal_file = "success_signal.txt"
sound_file = "celebrate.wav"
duration_seconds = 5

print("🎉 Celebrate.py מאזין כל הזמן לסיגנלים מ-GitHub...")

# -----------------------------
# פונקציות עזר
# -----------------------------
def get_latest_commit_info():
    """מחזיר את ה-hash וההודעה של ה-commit האחרון"""
    try:
        commit_hash = subprocess.check_output(
            ["git", "-C", repo_path, "rev-parse", "--short", "HEAD"],
            universal_newlines=True
        ).strip()
        commit_msg = subprocess.check_output(
            ["git", "-C", repo_path, "log", "-1", "--pretty=%s"],
            universal_newlines=True
        ).strip()
        branch_name = subprocess.check_output(
            ["git", "-C", repo_path, "rev-parse", "--abbrev-ref", "HEAD"],
            universal_newlines=True
        ).strip()
        return branch_name, commit_hash, commit_msg
    except Exception as e:
        return "unknown", "unknown", f"Error getting commit info: {e}"

# -----------------------------
# לולאה אינסופית
# -----------------------------
while True:
    try:
        # מושך את כל השינויים מ-GitHub
        subprocess.run(
            ["git", "-C", repo_path, "pull"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except Exception as e:
        print(f"⚠️ שגיאת git pull: {e}")

    # בודק אם קובץ הסיגנל קיים
    signal_path = os.path.join(repo_path, signal_file)
    if os.path.exists(signal_path):
        branch, commit_hash, commit_msg = get_latest_commit_info()
        print(f"✅ סיגנל זוהה! Branch: {branch}, Commit: {commit_hash}, Msg: {commit_msg}")

        # השמעת הצליל
        winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)

        # הודעה קופצת עם פרטי ה-commit
        notification.notify(
            title=f"🎉 Workflow הצליח! ({branch})",
            message=f"Commit {commit_hash}: {commit_msg}\nCelebrate.py מפעיל צליל 🎶",
            timeout=duration_seconds
        )

        # מחכה למשך הצליל ואז מפסיק
        time.sleep(duration_seconds)
        winsound.PlaySound(None, winsound.SND_PURGE)

        # מסיר את קובץ הסיגנל
        os.remove(signal_path)
        print("🎊 Celebrate הסתיים, ממתין לסיגנל הבא...")

    # מחכה שניה אחת לפני הפול הבא
    time.sleep(1)
