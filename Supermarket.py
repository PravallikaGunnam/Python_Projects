#For bill generation we need time
from datetime import datetime

name=input("Enter your Name:")

#List of items in the supermarket
Lists='''
Rice                 :100Rs/Kg
Sugar                :70Rs/Kg
Wheat Flour          :45Rs/Kg
Eggs                 :5Rs/each
salt                 :10Rs/Packet
oil                  :100Rs/packet
Ground Nuts          :80Rs/Kg
cofee Powder         :70Rs/Kg
Colgate              :50Rs/Each
Maggie               :14Rs/Each
'''

#Declaration
price=0
item=0
pricelist=[]
totalprice=0
itemlist=[]
quantitylist=[]
plist=[]
finalprice=0
gst=0

#for calculating those using product need to write that in dict format
items={"Rice":100,
"Sugar":70,
"Wheat Flour":45,
"Eggs":5,
"salt":10,
"oil":100,
"Ground Nuts":80,
"cofee Powder":70,
"Colgate":50,
"Maggie":14,}


#chooseing that  list using some yes/no options
option=int(input("For List of items Press 1: "))
if option==1:
    print(Lists)

#it is for selecting the items and quantity if u want to buy items
for i in range(len(items)):
    inpu1=int(input("If u want to Buy item Press 1 or 2 for Exit:"))
    if inpu1==2:
        break
    if inpu1==1:
        item=input("Enter the Item: ")
        quantity=int(input("Enter the Quantity: "))
        if item in items.keys():
#this is calculating only one item here
            price=quantity*(items[item])
#here we append those and calculete multiple items
            pricelist.append((item,quantity,price))
            totalprice+=price
            itemlist.append(item)
            quantitylist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalprice=gst+totalprice
        else:
            print("SORRY.....!Your entered item is not available")
    else:
        print("Please.....!check the number u entered wrong number")
    inp=input("u want to calculate the bill yes/no :")
    if inp=='yes':
        pass
        if finalprice!=0:
            print(25*"=","Apple SuperMarket",25*"=")
            print(28*" ","Bangalore")
            print("Name :",name,30*" ","Date :",datetime.now())
            print(75*"_")
            print("S_no",10*" ","items",10*" ","Quantity",10*" ","price")
            print(25*"=","Apple SuperMarket",25*"=")
            for i in range(len(pricelist)):
                print(i,10*" ",itemlist[i],15*" ",quantitylist[i],15*" ",plist[i])
            print(75*"_")
            print(50*" ","Total Amount","Rs",totalprice)
            print("Gst:",50*" ","Rs",gst)
            print(75*"_")
            print(50 * " ", "Final Amount", "Rs", finalprice)
            print(75 * "_")
            print(20 * " ", "THANKS FOR VISITING")
            print(20 * " ", "KEEP SHOPPING WITH US")

