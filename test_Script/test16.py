import asyncio
from obswebsocket import obsws, requests

def shutdown_obs(host, port, password):
    ws = obsws(host, port, password)
    ws.connect()
    ws.call(requests.Quit())
    ws.disconnect()
    print("OBSにシャットダウンリクエストを送信しました。")

if __name__ == "__main__":
    host = "localhost"
    port = 4455
    password = "KQH5Ze21mvypZUkU"  # OBS WebSocketのパスワードを設定している場合はここに入力
    shutdown_obs(host, port, password)