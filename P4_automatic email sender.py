import time                              #引入time模組,先進入讓使用者輸入的步驟

MailSub=input("1)請輸入提醒事項：")         #設置變量儲存提醒事項和備註
MailContent=input("2)備註：")
GapMinute=input("3)要在幾分鐘後提醒：")     #設置變量儲存時間，即多久後提醒
Gaptime=int(GapMinute)                  #把時間str轉成int,同時也轉成秒

time.sleep(Gaptime)                     #讓程式暫停一段時間,才繼續執行電郵程序

from email.mime.multipart import MIMEMultipart      #以下開始進入撰寫電郵步驟，先引入MIMEMultipart(多用途網際網路郵件擴展)
from email.mime.text import MIMEText                #引入MIMEText,以便撰寫電郵內容

content = MIMEMultipart()                           #定義變量content為MIMEMultipart物件
content["from"] = "uyn990905@gmail.com"             #指定寄件者
content["to"] = "e94117013@gs.ncku.edu.tw"          #指定收件者
content["subject"] = MailSub                        #連接使用者的提醒事項作為郵件標題
content.attach(MIMEText(MailContent))               #通過MIMEText,把使用者想備註的內容作為郵件內容,引入content內

import smtplib                          #以下開始進入發電郵程序，先引入smtplib模組,以便寄發郵件
Server=smtplib.SMTP(host="smtp.gmail.com", port="587")  #設置SMTP伺服器,確定host和port
Server.ehlo()                           #驗證SMTP伺服器
Server.starttls()                       #使用starttls方法來建立加密傳輸
Server.login("uyn990905@gmail.com", "dplzqwokghzftjgs") #登入伺服器(即寄件者gmail)
Server.send_message(content)            #把剛剛包裝好的郵件內容(content)寄送出去
Server.quit()                           #切斷SMTP伺服器的連接
print("成功發送電郵提醒！內容是：","\n","提醒標題：",MailSub,"\n","提醒內容：",MailContent)
#在程序中提醒使用者,電郵已發送，程序完成

#這是一個簡易的備忘提醒程序：首先，需要一些變量儲存電郵的標題和內容，並問使用者需要多久後發電郵提醒。