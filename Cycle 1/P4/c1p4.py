# -*- coding: utf-8 -*-
"""c1p4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nxgQixSXY6Xam-KZ4hh6J_LV1jaaRw0l
"""


def HappyCheck(n):
    tn = n
    sum = 0
    isHappy = False
    ctrl = 0
    while ctrl <= 100:
        tn2 = tn
        sum = 0
        while tn2:
            rem = tn2 % 10
            sum += rem**2
            tn2 = tn2//10
        if sum == 1:
            isHappy = True
            break
        else:
            tn = sum
        ctrl += 1
    return isHappy


def HappyRange(ll, ul):
    for i in range(ll, ul+1):
        if HappyCheck(i) == True:
            print(i, end=",")


def firstHappy(N):
    for i in range(1, N):
        if HappyCheck(i) == True:
            print(i, end=",")


LL = int(input("Enter Lower Limit : "))
UL = int(input("Enter Upper Limit : "))
print("\nHappy numbers between ", LL, " and ", UL, end="\n")
HappyRange(LL, UL)

n = int(input("Enter N : "))
print("First N Happy Numbers are : ")
firstHappy(n)
