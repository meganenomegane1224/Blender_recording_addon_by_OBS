import bpy
import obsws_python as obs

HOST="localhost"
PORT="4455"
PASSWORD="KQH5Ze21mvypZUkU"
SEENCOLLECTION_NAME="megane_MIKU"

# カスタム関数を定義
@bpy.app.handlers.persistent
def my_custom_function():
    client = obs.ReqClient(host=HOST, port=PORT, password=PASSWORD)
    client.start_record()

# 関数を閉じるハンドラーに追加
def register():
    bpy.app.handlers.load_post.append(my_custom_function)

def unregister():
    bpy.app.handlers.save_pre.remove(my_custom_function)

# Blenderにスクリプトを登録
if __name__ == "__main__":
    register()
