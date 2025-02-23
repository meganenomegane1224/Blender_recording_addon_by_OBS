import time
from obswebsocket import obsws, requests

#接続設定
host = "localhost"
port = 4455
password = "yHPa0r92bcMzF6OA"

#OBSに接続
ws=obsws(host, port, password)
ws.connect
print("ここまできた")
#各種設定のインポート
scene_collection_path="C:\\Callage\\blender アドオン制作\\タイムラプスアドオン\\OBS部分\\json\\シーンコレクション.json"
profile_path= "C:\\Callage\\blender アドオン制作\\タイムラプスアドオン\\OBS部分\\test\\basic.ini"

#ws.call(requests.ImportSceneCollection(scene_collection_path))
#ws.call(requests.ImportProfile(profile_path))