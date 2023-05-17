import socket           #引入socket模組
HOST = "140.116.118.129"    #設置IP，port隨意
PORT = 8000

SocketA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #定義SocketA,宣告TCP
SocketA.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
SocketA.bind((HOST, PORT))      #設置接入的HOST和PORT
SocketA.listen(1)               #設置最大等候數為1
i=1                             #設置計數器,用於儲存訂單號
while True:                                 #設置while true循環,讓loop無限循環
    print('等待客人中...')
    Connection, Address = SocketA.accept()  #從server端接收串接的客人和IP
    print('客人來咯！IP是 ' + str(Address))   #把串接成功的客人IP打印出來
    Connection.send("歡迎來到深夜食堂，我們的菜單如下：".encode())   #發互動信息給客人
    Connection.send("1) 控肉饭:50, 2) 锅烧意面:70, 3) 牛肉汤:100".encode())

    while True:
        indata = Connection.recv(1024)      #設變量,儲存串接對象傳來的資料
        OrderNum=str(i)                     #設置變量,儲存訂單號
        if indata.decode() == "1":
            Connection.send(("您點的1號套餐，價格是50，訂單號是"+OrderNum+"，請取餐時付款").encode())   #接收客人的回復,根據客人訂單選擇回傳確認套餐、價格訂單號
        elif indata.decode() == "2":
            Connection.send(("您點的2號套餐，價格是70，訂單號是"+OrderNum+"，請取餐時付款").encode())   #同上
        elif indata.decode() == "3":
            Connection.send(("您點的3號套餐，價格是100，訂單號是"+OrderNum+"，請取餐時付款").encode())  #同上
        print("客人點的套餐: " + indata.decode() + "號套餐" + "，訂單號是" + OrderNum)  #在server端print出客人的訂單,讓食堂老闆看到,就可以開始做菜
        Connection.send("謝謝惠顧，歡迎再來！".encode())
        i+=1     #訂單號+1,準備迎接下一個客人
        break    #這裏的break會跳出while true循環,然後重新回去上一個while true loop
        #所以Server端並不會停止運行,而是會繼續等待下一個訂單