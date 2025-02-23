import obsws_python as obs

try:
    ws = obs.ReqClient(host='localhost', port=4455, password='KQH5Ze21mvypZUkU') #パスワード設定している場合はpassword=''の''内にパスワードを記載
    ws.call_vendor_request(obs.requests.Quit())
    ws.disconnect()
    print("OBS Studioを停止しました。")
except Exception as e:
    print(f"エラーが発生しました: {e}")