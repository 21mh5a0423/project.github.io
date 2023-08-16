#!/usr/bin/env python
# coding: utf-8

# In[6]:


from datetime import datetime
name=input("enter your name:")
lists='''
Rice     Rs = 20/kg
Sugar    Rs = 30/kg
salt     Rs = 20/kg
oil      Rs = 80/ltr
paneer   Rs = 110/kg
maggi    Rs = 50/each
colgate  Rs = 85/each
lays     Rs = 10/each
'''
price=0
pricelist=[]
totalprice=0
finalamount=0
ilist=[]
qlist=[]
plist=[]

items={'rice':20,'sugar':20,'oil':80,'paneer':110,'maggi':50,'colgate':85,'salt':20,'lays':10}
option=int(input('for list of items press 1'))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your item name:")
        quantity=int(input('enter quantity:'))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry the item is unavailable")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items: yes or no :")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*'=',"manu supermarket",25*"=")
            print(28*' ',"rajahmundry")
            print("name:",name,30*" ","date:",datetime.now())
            print(75*"-")
            print("sno",6*" ",'items',10*" ",'quantity',5*" ",'price')
            for i in range(len(pricelist)):
                print((i+1),8*' ',ilist[i],12*' ',qlist[i],11*" ",plist[i])
            print(75*"-")
            print(50*" ",'totalamount:','rs',totalprice)
            print(51*" ","gst amount:",'rs',gst)
            print(75*"-")
            print(50*" ",'finalamount:','rs',finalamount)
            print(75*"-")
            print(25*" ",'thanks for visiting')
            print(75*"-")
            break


# In[ ]:




