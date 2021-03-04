price=0
item= input("請點餐:(A,B,C)")
item= item.upper() #轉大寫
'''
item= item.lower() #轉小寫
'''
if item == "A":
    price=130
    food=input("是否加購可樂(Y/N):")
    if food == "Y":
       price += 30
elif item == "B":
    price=115
elif item == "C":
    price=80
    food=input("是否換大薯(Y/N):")
    if food == "Y":
        price += 15
    q=input("捐款:")
    if q == "Y":
        money=int(input("金額:"))
        price += money
else:
    print("選項錯誤")
print(price)




    
        