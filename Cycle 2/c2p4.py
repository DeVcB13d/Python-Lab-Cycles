# -*- coding: utf-8 -*-
"""c2p4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qUgnST50gAmwI6dqAlAWQLNPQN6FW9ix

Problem Statement

Write a program to create a class Box with data members length,
breadth, height, area, and volume. Provider constructor that enables
initialization with one parameter (for cube), two parameters (for
square prism) three parameters (rectangular prism). Also, provide
functions to calculate area and volume.
Create a list of N boxes with random measurements and print the
details of the box with maximum volume: area ratio.
"""

class Box:
  def __init__(self,lens):
    if len(lens) == 3:
      self.length = lens[0]
      self.breadth = lens[1]
      self.height = lens[2]
    elif len(lens) == 1:
      self.length = lens[0]
      self.breadth = lens[0]
      self.height = lens[0]
    elif len(lens) == 2:
      self.length = lens[1]
      self.breadth = lens[1]
      self.height = lens[0]
    self.area = self.length * self.breadth
    self.volume = self.length * self.breadth * self.height
    self.AVratio = self.area/self.volume
  def get_area(self):
    self.area = self.length * self.breadth
  def get_volume(self):
    self.volume = self.length * self.breadth * self.height
  def show(self):
    print("Dimensions : ",self.length,self.breadth,self.height,sep = " ")
    print("Area       : ",self.area)
    print("Volume     : ",self.volume)

#Creating Boxes with Random dimensions
import random
N = int(input("Enter Number of boxes to create ; "))
Boxlist = [i for i in range(0,N)]
AVRatios = [i for i in range(0,N)]
for i in range(0,N):
  Usize = random.randint(1,3)
  l = []
  for j in range(1,Usize+1):
    l.append(random.randint(1,21))
  Boxlist[i] = Box(l)
  AVRatios[i] = Boxlist[i].AVratio

#To print the details of the box with maximum volume: area ratio
max_dim = AVRatios.index(max(AVRatios))
Boxlist[max_dim].show()