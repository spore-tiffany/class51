import socket
from time import sleep

HOST = '192.168.1.11'  # 伺服器位址
PORT = 1234        # 通訊埠

# 建立 TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
for i in range(5):
    msg = "哈囉伺服器，我是用戶端！:"+str(i)
    client_socket.sendall(msg.encode("utf-8"))
    
    data = client_socket.recv(1024)
    print("收到伺服器回應：", data.decode())
    sleep(2)

client_socket.close()
