# 图片处理：

import socket
from threading import Thread

# 绑定地址和端口号
host = '127.0.0.1'
port = 8080

# 创建socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))

# 存放用户数据
client = {}
address = {}

# 可接受的客户端数
acc_num = 2

#  广播
def Brodcast(message,nickname=''):
    for conn in client:
        conn.send(bytes(nickname,'utf-8')+message)
# 用户消息处理方法
def handle_client_in(conn,address):
    nickname = conn.recv(1024).decode('utf-8')
    welcome = f'welcome {nickname} come into!'
    client[conn] = nickname
    Brodcast(bytes(welcome,'utf-8'))




if __name__ == '__main__':
    s.listen(acc_num)
    print("服务器已开启，正在监听用户请求")
    while True:
        conn,address=s.accept()
        print(address,'已建立连接')
        conn.send('welcome to here，'
                  'please input your name:'.encode('utf-8'))
        address[conn] = address
        Thread(target=handle_client_in,args=(conn,address)).start()


