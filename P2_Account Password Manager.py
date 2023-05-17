"""現在的App越來越多，我經常忘記賬密，用網上的自動記賬密軟件又感覺不太安全，所以設計了一個記錄器"""
import os                                   #引入os模組
ListAccID=["SAMPLE"]                        #建立List存放賬號,裏面有預設的賬號,僅供等下示範用
ListPwd=["hELLOwORLD123"]                   #建立List存放密碼,裏面有預設的密碼,僅供等下示範用
DictRemark={"成功入口":0}                     #建立Dict,以Key存放備註,Value存放數字,而數字對應著賬密List的相應位置
path = 'NoteAcc&Pwd.txt'                    #建立記事本在電腦裏，存放等下新加入的賬密數據，以防程序跑完數據就清空的情況,起真正記錄的作用
f = open(path, 'w')
f.write("1)" + "賬號：" + "SAMPLE" + os.linesep)   #這三步只是將預設的賬密先加到記事本
f.write("密碼：" + "hELLOwORLD123" + os.linesep)
f.write("備註：" + "成功入口" + os.linesep)
i=1
while i <=100:                              #以i為計數器,用while loop循環100次,意即一次循環可以操作100次
    Ask=input("你是想記錄賬密還是搜索賬密？(回答record/search/end)")    #詢問使用者要進行的功能
    if Ask == "record":                                          #若使用者輸入record,則進入記錄功能
        AccountID=input("1.請輸入你的賬號：")                       #程式會要求使用者輸入賬密,並將新加入的賬密加入到List中
        Password=input("2.請輸入你的密碼：")
        ListAccID.append(AccountID)
        ListPwd.append(Password)
        Remark=input("3.有什麼需要備註的嗎：")                       #使用者可以輸入備註,程序會加入到Dict的Key中,並以ListAccID的長度減1來決定value(以便用數字搜索List)
        DictRemark[Remark]=len(ListAccID)-1
        f.write(str(i+1)+")"+"賬號："+AccountID+os.linesep)        #這三步將新加入的賬密加到記事本
        f.write("密碼："+Password+os.linesep)
        f.write("備註："+Remark+os.linesep)

    elif Ask == "search":                                         #若使用者輸入search,則進入搜索功能
        print("你的記事本的備註目前有：")
        j=1
        for k in list(DictRemark.keys()):                         #將備註Dict轉成List,分行打印出來,讓使用者選擇要檢查哪一個賬號
            print(j,")",k)
            j+=1

        Search=input("請輸入備註：")
        print("你的",Search,"的賬號是",ListAccID[int(DictRemark[Search])])    #通過使用者輸入的備註，對應到Dict中的Key,再用該Key的Value對應會去ListAccID來輸出賬密
        print("你的",Search,"的密碼是",ListPwd[int(DictRemark[Search])])
    elif Ask == "end":                                              #若使用者輸入end,則結束程序
        print("程式結束")
        break
    else:                                                           #若使用者輸入其他字眼,則提示重新輸入,並讓i-1以表示該循環無效
        print("輸入錯誤，請重新輸入")
        i-=1
    i+=1                                                            #i+1作為循環的結束

f.close()