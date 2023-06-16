from math_operator.addition import add
from math_operator.subtraction import sub
from math_operator.division import div
from math_operator.multipliction import multi

def order_input():
    num1=float(input("Enter your first number: "))
    num2=float(input("Enter your second number: "))
    return num1,num2


if __name__=="__main__":

    while True:
        order=input("1=div 2=multi 3=add 4=sub e=exit: ")
        if order=="e":
            break

        if order=="1":
            nums=order_input()
            print(div(nums[0],nums[1]))
        elif order=="2":
            nums=order_input()
            print(multi(nums[0],nums[1]))
        elif order=="3":
            nums=order_input()
            print(add(nums[0],nums[1]))
        elif order=="4":
            nums=order_input()
            print(sub(nums[0],nums[1]))
        else:
            print("Enter valid input!")


