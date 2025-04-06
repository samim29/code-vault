
user_id="IRONMAN"
password="Tony_$t@rk3000"


def login(uid,pwd):
        max_attempt=1
    
        if uid==user_id and pwd==password:
                return("Login Successful")
        if max_attempt==3 :
             print("Maximum attemt Exeed:")
             return
        print("Enter correct user id and password:")
        uid=input("Enter correct user id :")
        pwd=input("Enter correct password")
        max_attempt=max_attempt+1
        
        return
         
your_id=input("Enter your id")
your_password=input("Enter your password")

login(your_id,your_password)