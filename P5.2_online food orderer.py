"""部分基本的連接和收發信息功能已經在Test6.1.py，這裏僅簡述過其他功能部分"""
import socket
HOST = "140.116.118.129" #設置和食堂一樣的IP
PORT = 8000

SocketB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SocketB.connect((HOST, PORT))   #與食堂端產生串接

while True:         ##設置while true循環,讓loop無限循環直到強制停止
    InData = SocketB.recv(1024)                 #設變量,儲存server傳來的消息,並打印出來
    print(InData.decode())
    InData = SocketB.recv(1024)                 #同上
    print(InData.decode())
    if InData.decode() == "謝謝惠顧，歡迎再來！":   #設置結束串接的條件,即當對象傳來"謝謝惠顧，歡迎再來！"時，斷開連接
        print("系統已結束連接")
        SocketB.close()
        break
    OutData = input('請輸入點餐號碼： ')            #讓客人點餐
    print('您選擇的是: ' + OutData)                #回饋客人點餐信息
    SocketB.send(OutData.encode())               #發送