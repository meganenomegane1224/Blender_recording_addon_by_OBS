import bpy
import atexit
import os
import subprocess

def on_blender_exit():
    print("Blenderが終了します。指定の関数を実行します。")
    # ここに実行したい関数を追加
    # your_function()


def start_obs(self):
    obs_path="C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
    obs_dir_path="C:\\Program Files\\obs-studio\\bin\\64bit"

    try:
        os.chdir(obs_dir_path)
        subprocess.Popen([obs_path])
    except FileNotFoundError:
        self.report({'ERROR'}, "指定されたパスでは動作しません")
    else:
        self.report({'INFO'}, "OBSを起動しました")
    

def register():
    atexit.register(on_blender_exit)

def unregister():
    atexit.unregister(on_blender_exit)

if __name__ == "__main__":
    register()
