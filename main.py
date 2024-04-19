from datetime import datetime

name=input("Enter your name:")

list='''
rice   Rs 20/kg
sugar  Rs 30/kg
salt   Rs 80/kg
oil    Rs 90/liter
panner Rs 110/kg
Maggi  Rs 90/kg
Boost  Rs 90/each
bresh  Rs 30/each
'''
#declaration
price=0
pricelist=[]
totalprice=0
finalprince=0
ilist=[]
qlist=[]
plist=[]

#rates fir items
items={'rice':20,
       'salt':80,
       'sugar':30,
       'oil':90,
       'panner':110,
       'Maggi':90,
       'bresh':30}

option=int(input("for list of items press1:"))
if option==1:
    print(list)
for i in range(len(items)):
    inp1=int(input("if you want to buypress 1 or 2 for exit"))
    if inp1==2:
        break
    if inp1==1:
        item =input("enter the items")
        quantity=int(input("Enter quantity:"))
        if item  in items.keys():
                price=quantity*(items[item])
                pricelist.append((item,quantity,items,price))
                totalprice+=price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
                gst=(totalprice*5)/100
                finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","rakesh super marker",25*"=")
            print(20*"=","Gadwal")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"_")
            print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],plist[i])
            print(75*"_")
            print(50*" ",'totalammount:','Rs',totalprice)
            print("gst ammount",50*" ",'Rs',gst)
            print(75*"_")
            print(50*" ",'fianlamount:','Rs',finalamount)
            print(75*"_")
            print(50*" ","Thanks for visiting")
