from tkinter import *
from car_class import car 
import pickle

#Constants

scr = Tk()

def set_screen():
    scr.geometry("900x600+20+30")
    scr.configure(bg = "#CCE5FF")
    scr.title("Vehicle Sale Data")
def InputFrame():
    IFrame = Frame(scr)
    IFrame.pack(side = "top")
    I1 = Entry(IFrame)
    I1.insert(0,"Engine No : ")
    I1.pack()
    In_EngNo = I1.get() 
    I2 = Entry(IFrame)
    I2.insert(0,"Car Model : ")
    I2.pack()
    In_CarModel = I2.get()
    I3 = Entry(IFrame)
    I3.insert(0,"Car Type : ")
    I3.pack()
    In_CarModel = I2.get()   
    I4 = Entry(IFrame)
    I4.insert(0,"Mileage : ")
    I4.pack()
    In_Mileage = I4.get()  
    I5 = Entry(IFrame)
    I5.insert(0,"Vendor : ")
    I5.pack()
    In_Vendor = I5.get()     
    I6 = Entry(IFrame)
    I6.insert(0,"Reg No : ")
    I6.pack()
    In_RegNo = Entry(IFrame)
    



def main():
    set_screen()
    InputFrame()
    scr.mainloop()


main()