#1st method to import a module and function
# import abcd.hdfc

# abcd.hdfc.change_pin()
# abcd.hdfc.deposit()
# abcd.hdfc.fund_transfer()
# abcd.hdfc.change_pin()

# 2nd way to import a module
# from abcd.hdfc import change_pin,deposit,withdrawal

# change_pin()
# deposit()
# withdrawal()

# 3rd ways to import package 
from abcd.hdfc import *
withdrawal()
deposit()
change_pin()

def super(arg):
    def inner():
        print("Welcome to SBI")
        arg()
    return inner

val=super(change_pin)
val()