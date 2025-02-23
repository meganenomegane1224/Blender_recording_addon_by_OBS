import time
from obswebsocket import obsws, requests

#接続設定
host = "localhost"
port = 4455
password = "ja3QZZHqfZxWs7Fr"

#OBSに接続
ws=obsws(host, port, password)
ws.connect()
print("ここまできた")

# シーンコレクションを設定
scene_collection_name = "tt"
ws.call(requests.SetCurrentSceneCollection({"sc-name": scene_collection_name}))

# プロファイルを設定
profile_name = "test"
ws.call(requests.SetCurrentProfile({"profile-name": profile_name}))

ws.call(requests.StartRecord())
time.sleep(10)

ws.call(requests.StopRecord())
ws.disconnect()
print("すべての操作を終了しました")
