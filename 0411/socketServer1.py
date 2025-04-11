import socket

HOST = '192.168.1.11'  # 本機位址 (localhost)
PORT = 1234        # 通訊埠

# 建立 TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)  # 最多允許 1 個連線等待

print(f"伺服器啟動，等待來自 {HOST}:{PORT} 的連線...")
while True:
    conn, addr = server_socket.accept()
    print(f"已連線：{addr}")
    
    while True:
        data = conn.recv(1024)  # 接收最多 1024 bytes
        if not data:
            print("disconnect")
            break
        print("收到客戶端資料：", data.decode())
        msg = "哈囉伺服器，我是用戶端！"
        conn.sendall(msg.encode("utf-8"))
        #conn.sendall(b"伺服器回應：收到您的訊息")

    conn.close()
server_socket.close()
