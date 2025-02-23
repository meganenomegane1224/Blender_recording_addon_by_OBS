import subprocess
import os

def start_obs():
    obs_path="C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
    obs_dir_path="C:\\Program Files\\obs-studio\\bin\\64bit"

    try:
        os.chdir(obs_dir_path)
        subprocess.Popen([obs_path])
    except FileNotFoundError:
        print(f"指定されたパスにOBSが見つかりませんでした: {obs_path}")
    else:
        print("OBSを起動しました")

if __name__ == "__main__":
    start_obs()