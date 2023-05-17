"""根據預算決定午餐的機器。"""
import random as r                             #引入亂數模組，命名為r

"""以下字典通過預算的不同，分別分成低中高預算的字典"""
"""字典的key為食物/店名，value為平均消費價格"""
LowBudgetFood={"土":0,"白飯配醬油":10,"維力炸醬麵":35,"飯糰":50,"成大館":60,"墨爾漢堡":60,"王記雞肉":65,"學餐":70,"小茂屋":70,"響亮冰舖":70}
MediumBudgetFood={"東馬海南雞飯":80,"大醬川麵館":80,"七海魚皮":90,"余家刀切面":110,"肉肉控丼飯":120,"麥當勞":120,"花語鐵板燒":120,"元味屋":120}
HighBudgetFood={"憶品鍋":180,"五鮮級":200,"磕牛排":200,"孫東寶":250,"陶板屋":600}

Ask1=input("你今天的午餐預算是?(回答低/中/高)")      #詢問使用者的午餐預算

if Ask1 == "低":                                #用if判斷使用者回答的預算程度
    ListA = list(LowBudgetFood.keys())          #將LowBudgetFood字典的keys放入一個新的ListA
    print("我們推薦的店有:")
    for i in ListA:                             #通過for循環，先打印出每一個店名選項
        print(i)
    Ask2 = input("想要我們幫你選午餐嗎?(回答Y/N)")   #詢問使用者是否需要幫忙決定午餐
    if Ask2 == "Y":
        ListB = list(LowBudgetFood.items())     #將LowBudgetFood字典的item放入一個新的ListB,此時每一個元素形態為元組
        Tuple = ListB[r.randint(0, len(ListB))] #用變數Tuple儲存從ListB通過隨機數挑選出來的元組
        print("我們幫你選的店是:", Tuple[0], "平均消費是", Tuple[1])  #打印指定元組的0號及1號位，即店名和平均消費
    elif Ask2 == "N":
        print("好的")                            #若使用者不需要我們幫忙決定，則回復"好的"，並pass
        pass

elif Ask1 == "中":                                #方法同上
    ListA = list(MediumBudgetFood.keys())
    print("我們推薦的店有:")
    for i in ListA:
        print(i)
    Ask3 = input("想要我們幫你選午餐嗎?(回答Y/N)")
    if Ask3 == "Y":
        ListB = list(MediumBudgetFood.items())
        Tuple = ListB[r.randint(0, len(ListB))]
        print("我們幫你選的店是:", Tuple[0], "平均消費是", Tuple[1])
    elif Ask3 == "N":
        print("好的")
        pass

elif Ask1 == "高":                                #方法同上
    ListA = list(HighBudgetFood.keys())
    print("我們推薦的店有:")
    for i in ListA:
        print(i)
    Ask4 = input("想要我們幫你選午餐嗎?(回答Y/N)")
    if Ask4 == "Y":
        ListB = list(HighBudgetFood.items())
        Tuple = ListB[r.randint(0, len(ListB))]
        print("我們幫你選的店是:", Tuple[0], "平均消費是", Tuple[1])
    elif Ask4 == "N":
        print("好的")
        pass
else:
    print("輸入錯誤，請重新回答")                     #若使用者輸入錯誤，則回饋給使用者
