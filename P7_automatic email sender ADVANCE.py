#阿成最近活動太多，很多課程跟不上，作業上也遇到很多問題要請教助教，但是不同的課程有不同助教電郵，一直重複寫電郵，太沒效率了。有什麼辦法可以讓阿成寫得快一點呢？
CourseList=["計算機概論","微積分","普物"]         #課程列表，和課程電郵的index相對應
MailList=["e94117013@gs.ncku.edu.tw","e94117013@gs.ncku.edu.tw","e94117013@gs.ncku.edu.tw"]
#MailList裏的電郵應該要是不同課程助教的電郵，這裏方便演示，全部設為我的電郵
for i in CourseList:
    print("|",i,"的序號是",CourseList.index(i),"|") #打印每一個課程給使用者選
print("===============================分割線===============================")

#以下5行是郵件內容的設定，皆讓使用者輸入，然後再套進去郵件發送器
CourseNum=input("1) 請輸入課程序號：")                   #輸入想問的課程
LabNum=input("2) 作業類型:")                           #課程的作業類型
KeyWord=input("3) 輸入問題的關鍵詞：")                   #問題關鍵詞
MainQuestion=input("4) 請輸入你的問題：")                #問題正文
ImageName=input("5) 請輸入有關圖片的file name：")        #有關問題的截圖

IntroMyself="助教你好，我是XXX，學號是XXX"                #郵件模板，不重要
ThanksWord="謝謝助教！"

MailSub=CourseList[int(CourseNum)]+"|有關課程"+ LabNum+"的"+KeyWord+"的疑問"      #電郵標題
MailContent=IntroMyself+"\n"+"我想詢問有關"+LabNum+"的問題"+"\n"+"請問："+MainQuestion+"\n"+ThanksWord  #電郵正文

from email.mime.multipart import MIMEMultipart      #以下開始進入撰寫電郵步驟，先引入MIMEMultipart(多用途網際網路郵件擴展)
from email.mime.text import MIMEText                #引入MIMEText,以便撰寫電郵內容
from email.mime.image import MIMEImage              ##引入MIMEImage,以便發截圖
from pathlib import Path

content = MIMEMultipart()                           #定義變量content為MIMEMultipart物件
content["from"] ="uyn990905@gmail.com"               #指定寄件者
content["to"] = MailList[int(CourseNum)]            #指定收件者：就是從MailList裏面找出你想問的課程助教的電郵
content["subject"] = MailSub                        #連接使用者的提醒事項作為郵件標題
content.attach(MIMEText(MailContent))               #通過MIMEText,把使用者想備註的內容作為郵件內容,引入content內
content.attach(MIMEImage(Path("C:/Users/USER/Pictures/Screenshots/"+ImageName+".jpg").read_bytes()))

import smtplib                          #以下開始進入發電郵程序，先引入smtplib模組,以便寄發郵件
Server=smtplib.SMTP(host="smtp.gmail.com", port="587")  #設置SMTP伺服器,確定host和port
Server.ehlo()                           #驗證SMTP伺服器
Server.starttls()                       #使用starttls方法來建立加密傳輸
Server.login("uyn990905@gmail.com", "dplzqwokghzftjgs") #登入伺服器(即寄件者gmail)
Server.send_message(content)            #把剛剛包裝好的郵件內容(content)寄送出去
Server.quit()                           #切斷SMTP伺服器的連接
print("成功發送電郵提醒！內容是：","\n","郵件標題：",MailSub,"\n","郵件內容：",MailContent)
#在程序中提醒使用者,電郵已發送，程序完成
