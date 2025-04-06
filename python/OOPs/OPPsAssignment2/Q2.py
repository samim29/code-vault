"""#### 3.Define a class Calculator with overloaded methods add() to perform addition with different numbers of arguments. Test the calculator
 by adding numbers using different numbers of arguments.

"""
class Calculator:
    def add(self,*args):
        total=0
        for arg in args:
            total+=arg
        return total

def main():
    calculator=Calculator()
    result=calculator.add(1,2,3)
    print("Sum is: ",result)
    result=calculator.add(1,2)
    print("Sum is: ",result)
    result=calculator.add(1,2,3,4,5)
    print("Sum is: ",result)

if __name__=="__main__":
    main()