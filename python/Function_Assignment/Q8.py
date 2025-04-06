def payable_amount(shopping):
    member=input("Are you a PW member: enter 1 if yes otherwise enter 0")
    if shopping<2500: print(f"your payable amount is {shopping}")
    if 2500<=shopping<3000:
        discount= shopping*0.05
        pay=shopping-discount
        if member ==1 :
            pay *=0.05
            print(f"You got 5% discount,and as a member extra 5% and net payable amaount is {pay}")
        print(f"You got 5% discount and net payable amaount is {pay}")
    elif 3000<=shopping<4500:
        discount= shopping*0.08
        pay=shopping-discount
        if member ==1 :
            pay *=0.05
            print(f"You got 5% discount,and as a member extra 8% and net payable amaount is {pay}")
        print(f"You got 8% discount and net payable amaount is {pay}")
    elif shopping>=4500:
        discount= shopping*0.10
        pay=shopping-discount
        if member ==1 :
            pay *=0.05
            print(f"You got 5% discount,and as a member extra 10% and net payable amaount is {pay}")
        print(f"You got 10% discount and net payable amaount is {pay}")
payable_amount(float(input("Enter your shopping amount: ")))
