from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import requests
from tkinter import messagebox
import random
from datetime import datetime
from tkinter import filedialog

#===============Total Button Code
def total_bills():
    #========Drink Items Price============
    MongoJuice_price      =40
    OrangeJuice_price     =50
    AppleJuice_price      =60
    Thumbsup_price        =40
    pepsi_price           =20
    RedBull_price         =1000
    kulfi_price           =70
    GreenBeer_price       =2100
    chocolate_price       =280
    coffee_price           =30
    tea_price             =20
    # ========Food Items Price============
    chicken_Biryani_price =230
    Hyderabad_Biryani_price=200
    Grilled_Chicken_price =320
    Toonduri_price        =180
    ChickenLollipops_price=160
    Kabab_price            =100
    Egg_Biryani_price      =120
    FishFry_price          =100
    mix_veg_price          =60
    roti_price             =5
    Daal_price             =20
    parata_price           =7
    # ========Drink Items quantity============

    MongoJuice_q         = MongoJuice_qty.get()
    OrangeJuice_q        = OrangeJuice_qty.get()
    AppleJuice_q         = AppleJuice_qty.get()
    Thumbsup_q           = Thumbsup_qty.get()
    pepsi_q              = pepsi_qty.get()
    RedBull_q            = RedBull_qty.get()
    kulfi_q              = kulfi_qty.get()
    GreenBeer_q          = GreenBeer_qty.get()
    chocolate_q          = chocolate_qty.get()
    coffee_q             = coffee_qty.get()
    tea_q                = tea_qty.get()

    # ========Food Items Price============
    chicken_Biryani_q     = chicken_Biryani.get()
    Hyderabad_Biryani_q   = Hyderabad_Biryani.get()
    Grilled_Chicken_q     = Grilled_Chicken_qty.get()
    Toonduri_q            = Toonduri_qty.get()
    ChickenLollipops_q    = ChickenLollipops_qty.get()
    Kabab_q               = Kabab_qty.get()
    Egg_Biryani_q         = Egg_Biryani_qty.get()
    FishFry_q             = FishFry_qty.get()
    mix_veg_q             = mix_veg_qty.get()
    roti_q                = roti_qty.get()
    Daal_q                = Daal_qty.get()
    parata_q              = parata_qty.get()

    #=============Drink item Validation==========
    if MongoJuice_var.get()==0:
        MongoJuice_q=0
    elif MongoJuice_var.get()==1 and MongoJuice_qty.get() =="":
        messagebox.showerror("error""please fill the MongoJuice quantity")
        MongoJuice_q=0

    if OrangeJuice_var.get()==0:
        OrangeJuice_q=0
    elif OrangeJuice_var.get()==1 and OrangeJuice_qty.get() =="":
        messagebox.showerror("error""please fill the OrangeJuice quantity")
        OrangeJuice_q=0

    if AppleJuice_var.get()==0:
        AppleJuice_q=0
    elif AppleJuice_var.get()==1 and AppleJuice_qty.get() =="":
        messagebox.showerror("error""please fill the AppleJuice quantity")
        AppleJuice_q=0

    if Thumbsup_var.get()==0:
        Thumbsup_q=0
    elif Thumbsup_var.get()==1 and Thumbsup_qty.get() =="":
        messagebox.showerror("error""please fill the Thumbsup quantity")
        Thumbsup_q=0

    if pepsi_var.get()==0:
        pepsi_q=0
    elif pepsi_var.get()==1 and pepsi_qty.get() =="":
        messagebox.showerror("error""please fill the pepsi quantity")
        pepsi_q=0

    if RedBull_var.get()==0:
        RedBull_q=0
    elif RedBull_var.get()==1 and RedBull_qty.get() =="":
        messagebox.showerror("error""please fill the RedBull quantity")
        RedBull_q=0

    if kulfi_var.get()==0:
        kulfi_q=0
    elif kulfi_var.get()==1 and kulfi_qty.get() =="":
        messagebox.showerror("error""please fill the kulfi quantity")
        kulfi_q=0

    if GreenBeer_var.get()==0:
        GreenBeer_q=0
    elif GreenBeer_var.get()==1 and GreenBeer_qty.get() =="":
        messagebox.showerror("error""please fill the GreenBeer quantity")
        GreenBeer_q=0

    if chocolate_var.get()==0:
        chocolate_q=0
    elif chocolate_var.get()==1 and chocolate_qty.get() =="":
        messagebox.showerror("error""please fill the chocolate quantity")
        chocolate_q=0

    if coffee_var.get()==0:
        coffee_q=0
    elif coffee_var.get()==1 and coffee_qty.get() =="":
        messagebox.showerror("error""please fill the coffee quantity")
        coffee_q=0

    if tea_var.get()==0:
        tea_q=0
    elif tea_var.get()==1 and tea_qty.get() =="":
        messagebox.showerror("error""please fill the tea quantity")
        tea_q=0
    # =============Food item Validation==========
    if chicken_Biryani_var.get()==0:
        chicken_Biryani_q=0
    elif chicken_Biryani_var.get()==1 and chicken_Biryani_qty.get() =="":
        messagebox.showerror("error""please fill the chicken_Biryani quantity")
        chicken_Biryani_q=0

    if Hyderabad_Biryani_var.get()==0:
        Hyderabad_Biryani_q=0
    elif Hyderabad_Biryani_var.get()==1 and Hyderabad_Biryani_qty.get() =="":
        messagebox.showerror("error""please fill the Hyderabad_Biryani quantity")
        Hyderabad_Biryani_q=0

    if Grilled_Chicken_var.get()==0:
        Grilled_Chicken_q=0
    elif Grilled_Chicken_var.get()==1 and Grilled_Chicken_qty.get() =="":
        messagebox.showerror("error""please fill the Grilled_Chicken quantity")
        Grilled_Chicken_q=0

    if Toonduri_var.get()==0:
        Toonduri_q=0
    elif Toonduri_var.get()==1 and Toonduri_qty.get() =="":
        messagebox.showerror("error""please fill the Toonduri quantity")
        Toonduri_q=0

    if ChickenLollipops_var.get()==0:
        ChickenLollipops_q=0
    elif ChickenLollipops_var.get()==1 and ChickenLollipops_qty.get() =="":
        messagebox.showerror("error""please fill the ChickenLollipops quantity")
        ChickenLollipops_q=0

    if Kabab_var.get()==0:
        Kabab_q=0
    elif Kabab_var.get()==1 and Kabab_qty.get() =="":
        messagebox.showerror("error""please fill the Kabab quantity")
        Kabab_q=0

    if Egg_Biryani_var.get()==0:
        Egg_Biryani_q=0
    elif Egg_Biryani_var.get()==1 and Egg_Biryani_qty.get() =="":
        messagebox.showerror("error""please fill the Egg_Biryani quantity")
        Egg_Biryani_q=0

    if FishFry_var.get()==0:
        FishFry_q=0
    elif FishFry_var.get()==1 and FishFry_qty.get() =="":
        messagebox.showerror("error""please fill the FishFry quantity")
        FishFry_q=0

    if roti_var.get()==0:
        roti_q=0
    elif roti_var.get()==1 and roti_qty.get() =="":
        messagebox.showerror("error""please fill the roti quantity")
        roti_q=0

    if mix_veg_var.get()==0:
        mix_veg_q=0
    elif mix_veg_var.get()==1 and mix_veg_qty.get() =="":
        messagebox.showerror("error""please fill the mix_veg quantity")
        mix_veg_q=0

    if Daal_var.get()==0:
        Daal_q=0
    elif Daal_var.get()==1 and Daal_qty.get() =="":
        messagebox.showerror("error""please fill the Daal quantity")
        Daal_q=0

    if parata_var.get()==0:
        parata_q=0
    elif parata_var.get()==1 and MongoJuice_qty.get() =="":
        messagebox.showerror("error""please fill the parata quantity")
        parata_q=0

    total_MongoJuice_price=MongoJuice_price*int(MongoJuice_q)
    total_OrangeJuice_price=OrangeJuice_price*int(OrangeJuice_q)
    total_AppleJuice_price=AppleJuice_price*int(AppleJuice_q)
    total_Thumbsup_price=Thumbsup_price*int(Thumbsup_q)
    total_pepsi_price=pepsi_price*int(pepsi_q)
    total_RedBull_price=RedBull_price*int(RedBull_q)
    total_kulfi_price=kulfi_price*int(kulfi_q)
    total_GreenBeer_price=GreenBeer_price*int(GreenBeer_q)
    total_chocolate_price=chocolate_price*int(chocolate_q)
    total_coffee_price=coffee_price*int(coffee_q)
    total_tea_price=tea_price*int(tea_q)
    # ==============Total Drinks cost============
    total_drinks_cost=total_MongoJuice_price+total_OrangeJuice_price+total_AppleJuice_price+\
                      total_Thumbsup_price+total_pepsi_price+total_RedBull_price+total_kulfi_price+total_GreenBeer_price+total_chocolate_price+total_coffee_price+total_tea_price

    #========after complete the bill it clear the previous data========
    if total_drinks_cost.get()!="":
        drinks_cost.delete(0,"end")
        drinks_cost.insert("end",total_drinks_cost)
    else:
        drinks_cost.insert("end",total_drinks_cost)

    # ==============Total Food cost============
    total_chicken_Biryani_price=chicken_Biryani_price*int(chicken_Biryani_q)
    total_Hyderabad_Biryani_price=Hyderabad_Biryani_price*int(Hyderabad_Biryani_q)
    total_Grilled_Chicken_price=Grilled_Chicken_price*int(Grilled_Chicken_q)
    total_Toonduri_price=Toonduri_price*int(Toonduri_q)
    total_ChickenLollipops_price=ChickenLollipops_price*int(ChickenLollipops_q)
    total_Kabab_price=Kabab_price*int(Kabab_q)
    total_Egg_Biryani_price=Egg_Biryani_price*int(Egg_Biryani_q)
    total_FishFry_price=FishFry_price*int(FishFry_q)
    total_mix_veg_price=mix_veg_price*int(mix_veg_q)
    total_roti_price=roti_price*int(roti_q)
    total_Daal_price=Daal_price*int(Daal_q)
    total_parata_price=parata_price*int(parata_q)

    #===============Total Food Price==========
    total_food_cost=total_chicken_Biryani_price+total_Hyderabad_Biryani_price+total_Grilled_Chicken_price+total_Toonduri_price+total_ChickenLollipops_price+total_Kabab_price+total_Egg_Biryani_price+total_FishFry_price+total_mix_veg_price+total_roti_price+total_Daal_price+total_parata_price

    if total_food_cost.get()!="":
        food_cost.delete(0,"end")
        food_cost.insert("end",total_food_cost)
    else:
        food_cost.insert("end",total_food_cost)

    if service_charge.get()!="":
        service_charge.delete(0,"end")
        service_charge.insert(0,"10")
    else:
        service_charge.insert(0,"10")

    fc=int(food_cost.get())
    dc=int(drinks_cost.get())

    total_paid_tax=fc+dc
    total_paid_tax=total_paid_tax*8/100

    if paid_tax_cost !="":
        paid_tax_cost.delete(0,"end")
        paid_tax_cost.insert(0,total_paid_tax)
    else:
        paid_tax_cost.insert(0,total_paid_tax)

    total_sub_cost=fc+dc+int(service_charge_cost.get())

    if sub_total_cost.get()!="":
        sub_total_cost.delete(0,"end")
        sub_total_cost.insert(0,total_sub_cost)
    else:
        sub_total_cost.insert(0,total_sub_cost)

    if total_cost_cost.get()!="":
        total_cost_cost.delete(0,"end")
        total_cost_cost.insert(0,float(total_sub_cost+total_paid_tax))
    else:
        total_cost_cost.insert(0,float(total_sub_cost+total_paid_tax))

    #=================Total Bill Recipt============================
    date=datetime.now()date()
    if bill_details.get(1.0,"end")!="":
        bill_details.delete(1.0,"end")
        bill_details.insert(1.0,f"Billno-{random.randint(100,1000)}\t{date} ====================Items(q) \t \t Amount ===================\n{'Mangojuice('+str(MongoJuice_q)+')'+'     '+str(int(MongoJuice_q)*MongoJuice_price)+'   'if MongoJuice_var.get()==1 else''}{'OrangeJuice('+str(OrangeJuice_q)+')'+' '+str(int(OrangeJuice_q)*OrangeJuice_price)+''if OrangeJuice_var.get()==1 else''}
{'OrangeJuice('+str(OrangeJuice_q)+')'+' '+str(int(OrangeJuice_q)*OrangeJuice_price)+''if OrangeJuice_var.get()==1 else''}
{'OrangeJuice('+str(OrangeJuice_q)+')'+' '+str(int(OrangeJuice_q)*OrangeJuice_price)+''if OrangeJuice_var.get()==1 else''}
")

'OrangeJuice('+str(OrangeJuice_q)+')'+' '+str(int(OrangeJuice_q)*OrangeJuice_price)+''if OrangeJuice_var.get()==1 else''

