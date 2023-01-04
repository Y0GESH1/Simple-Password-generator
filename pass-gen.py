#!/bin/python3 
import string 
import random 
import pyfiglet as pfg
import argparse

banner = pfg.figlet_format("Simple Password Generator",font="slant")
print(banner)

parser = argparse.ArgumentParser(description="Simple Password Generator")
parser.add_argument('arguments',metavar='Length of the password',type=int,help="Enter the length of the password")
# type is optional if you want to specify the type of daa you want
args = parser.parse_args()

pass_len=args.arguments

def pass_gen():
    alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num="1234567890"
    con1= random.choice(num)
    sym="#!@$%^^%&*"
    con2= random.choice(sym)
    passw=""

    for x in range(pass_len):
        var=random.choice(alpha)
        passw += var 
    passw = passw+con1+con2
    return passw

x =  pass_gen()
print(x)