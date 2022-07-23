# import tkinter
#
# screen = tkinter.Tk()
# screen.title("My App")
# screen.mainloop()



# import tkinter
#
# screen = tkinter.Tk()
# screen.title("My App")
# screen.geometry("500x500")
# screen.mainloop()



# import tkinter
#
# screen = tkinter.Tk()
# screen.title("My App")
# screen.geometry("500x500")
# btn = tkinter.Button(screen,text="Click here",bg="Blue",fg="white",height=3,width=10,font=("arial",16,"bold"),activebackground="black",activeforeground="white",bd=10)
# btn.pack(side=tkinter.LEFT)
# screen.mainloop()



# import tkinter
#
# screen = tkinter.Tk()
# screen.title("My App")
# screen.geometry("500x500")
# btn = tkinter.Button(screen,text="Click Here",bg="Blue",fg="White",height=3,width=10,font=("arial",16,"bold"),activebackground="Black",activeforeground="white",bd=10)
# btn.place(x=100,y=200)
# screen.mainloop()



# import tkinter
#
# screen = tkinter.Tk()
# screen.title("My App")
# screen.geometry("500x500")
# btn1 = tkinter.Button(screen,text="Click here 1",bg="blue",fg="white",height=3,width=10,font=("arial",16,"bold"),activebackground="black",activeforeground="white",bd=10)
# btn2 = tkinter.Button(screen,text="Click Here 2",bg="blue",fg="white",height=3,width=10,font=("arial",16,"bold"),activebackground="black",activeforeground="white",bd=10)
#
# btn1.grid(row=0,column=0)
# btn2.grid(row=0,column=1)
# screen.mainloop()



# import tkinter
#
# screen = tkinter.Tk()
# screen.title("My App")
# screen.geometry("500x500")
# -------------Python Code----------------
# def myfun():
#     print("Button 1 Cliiked")
# -------------Python Code----------------
# btn1 = tkinter.Button(screen,text="Click Here 1",bg="blue",fg="white",height=3,width=10,font=("arial",16,"bold"),activebackground="black",activeforeground="white",bd=10,command=myfun)
#
# btn1.grid(row=0,column=0)
# screen.mainloop()



# import tkinter
#
# screen = tkinter.Tk()
# screen.title("My App")
# screen.geometry("500x500")
# -------------Python Code----------------
# def myfun1():
#     print("Button 1 Clicked")
# def myfun2():
#     print("Button 2 Clicked")
# -------------Python Code----------------
# btn1 = tkinter.Button(screen,text="Click Here 1",bg="blue",fg="white",height=3,width=10,font=("arial",16,"bold"),activebackground="black",activeforeground="white",bd=10,command=myfun1)
# btn2 = tkinter.Button(screen,text="Click Here 2",bg="blue",fg="white",height=3,width=10,font=("arial",16,"bold"),activebackground="black",activeforeground="white",bd=10,command=myfun2)
#
# btn1.grid(row=0,column=0)
# btn2.grid(row=0,column=1)
# screen.mainloop()
import tkinter

# from tkinter_logic import *
#
# btn1 = tkinter.Button(screen,text="+",bg="Blue",fg="white",height=1,width=4,font=("arial",16,"bold"),activebackground="black",activeforeground="white",bd=10,command=myfun)
# btn2 = tkinter.Button(screen,text="-",bg="Blue",fg="white",height=1,width=4,font=("arial",16,"bold"),activebackground="black",activeforeground="white",bd=10,command=myfun2)
#
# result = tkinter.Label(screen,textvariable=var_result,font=("arial",15,"bold"))
#
# btn1.grid(row=0,column=0)
# result.grid(row=0,column=1)
# btn2.grid(row=0,column=2)
#
# screen.mainloop()



# from tkinter_logic import *
#
# mybox = tkinter.Entry(screen,textvariable=var_box)
#
# btn1 = tkinter.Button(screen,text="Submit",bg="Blue",fg="white",height=1,width=10,font=("arial",16,"bold"),activebackground="black",activeforeground="white",bd=10,command=submit)
#
# result = tkinter.Label(screen,textvariable=var_result,font=("arial",15,"bold"))
#
# mybox.grid(row=0,column=0,columnspan=2)
# result.grid(row=1,column=0)
# btn1.grid(row=1,column=1)
#
# screen.mainloop()