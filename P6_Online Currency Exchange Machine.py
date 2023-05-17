listA=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
listB=['\ufeff幣別', 'USD', 'HKD', 'GBP', 'AUD', 'CAD', 'SGD', 'CHF', 'JPY', 'ZAR', 'SEK', 'NZD', 'THB', 'PHP', 'IDR', 'EUR', 'KRW', 'VND', 'MYR', 'CNY']
listC=['現金', '30.98000', '3.99400', '38.22000', '20.92000', '22.84000', '22.93000', '33.29000', '0.22940', '0.00000', '3.09000', '19.98000', '0.94390', '0.61260', '0.00228', '33.04000', '0.02561', '0.00147', '7.40900', '4.46800']
print(listA)
print(listB)
print(listC)
print("兌換的幣種如下：")
for i in listA:
  print(i+1,listB[i+1])
  if i+1==19:
    break
Type=input("請選擇幣種：")
print("你選擇的幣種是",listB[int(Type)])
print("匯率是",float(listC[int(Type)]))
Change=input("請輸入金額：")
Amount=int(Change)/float(listC[int(Type)])
print("兌換成",Amount,listB[int(Type)])