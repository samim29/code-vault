''' Create a user-defined function trafficLight() that prompts the user for input. If the input is not "RED", 
"YELLOW", or "GREEN", display an error message. Then, call the function light(). Depending on the return 
value of light(), display one of the following messages: 


a) "STOP, your life is precious" if the return vaAle is 0
b) "Please Wait, till the light is Green" if the return value is 1
c) "GO! Thank you for being patient" if the return value is 2'''
def light(colour):
    if colour=="RED": return  0
    elif colour=="YELLOW": return 1
    else: return 2

def trafficLight():
    colour=input("Enter the colour of traffic light (RED,GREEN,YELLOW):").upper()
    if colour not in ["RED","YELLOW","GREEN"]:
        print("Error: Invalid input! Please enter either RED, YELLOW, or GREEN.")
        return
    
    if light(colour)==0 : print("STOP, your life is precious")
    elif light(colour)==1:print("Please Wait, till the light is Green")
    else: print("GO! Thank you for being patient")
trafficLight()
