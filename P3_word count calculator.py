StrLimit=input("1) 請輸入你要達到的字數：")            #輸入字數規範
StrInput=input("2) 請輸入你想檢查的字數：")            #輸入要檢查的文章
#“一天晚上，阿成在寫通識課的心得報告，字數還規定必須超過1000字！他還有4篇報告要寫。於是他寫了一個計算字數的程序，打發無聊時光。”"
CountMark1=StrInput.count("，")                    #用變數暫存文章中[，]的數量，以此類推，以下分別找出不同標點符號在文章里的數量
CountMark2=StrInput.count("。")
CountMark3=StrInput.count("！")
CountMark4=StrInput.count("？")
CountMark5=StrInput.count("“")
CountMark6=StrInput.count("”")
CountWords=len(StrInput)-CountMark1-CountMark2-CountMark3-CountMark4-CountMark5-CountMark6
"""用變數CountWord來儲存文字數量，即文章原字數扣掉標點符號的數量"""
print('"，"的數量：', CountMark1)                    #統計不同標點符號在文章中出現的次數
print('"。"的數量：', CountMark2)
print('"！"的數量：', CountMark3)
print('"？"的數量：', CountMark4)
print('"“"的數量：', CountMark5)
print('"”"的數量：', CountMark6)
print("標點符號共有：",len(StrInput)-CountWords)     #同上
print("字數共有：",CountWords)                      #打印字數
if int(StrLimit) > CountWords:                    #設定條件，分別爲字數不滿足時、字數滿足時、字數剛剛好時的三種對應回答
    LessWord=int(StrLimit)-CountWords
    print("字數不夠！你還差",LessWord,"個字。")       #回饋使用者還差多少字數

elif int(StrLimit) < CountWords:
    ExtraWord = CountWords - int(StrLimit)
    print("字數足夠了！超過規定字數",ExtraWord,"個字。")       #回饋使用者超過多少字數

else:
    print("字數剛好！")