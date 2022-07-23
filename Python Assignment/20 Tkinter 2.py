from tkinter_logic import * 

lbl_title = tkinter.Label(screen,text="WELCOME TO ROCK PAPER SCISSOR GAME",font=("arial",12,"bold"),bg="white",fg="purple")
lbl_title.place(x=80,y=20)

btn_rock = tkinter.Button(screen,text="ROCK",font=("arial",18,"bold"),bg="purple",fg="white",command= lambda : myfun("ROCK"))
btn_rock.place(x=50,y=80)

btn_paper = tkinter.Button(screen,text="PAPER",font=("arial",18,"bold"),bg="purple",fg="white",command= lambda : myfun("PAPER"))
btn_paper.place(x=200,y=80)

btn_scissor = tkinter.Button(screen,text="SCISSOR",font=("arial",18,"bold"),bg="purple",fg="white",command= lambda : myfun("SCISSOR"))
btn_scissor.place(x=350,y=80)

# begin-------------         user view -------------
lbl_user = tkinter.Label(screen,text="USER",font=("arial",12,"bold"),bg="white",fg="purple")
lbl_user.place(x=50,y=180)

lbl_user_sel = tkinter.Label(screen,textvariable=var_user_sel,font=("arial",12,"bold"),bg="white",fg="purple")
lbl_user_sel.place(x=200,y=180)

lbl_user_score = tkinter.Label(screen,textvariable=var_user_score,font=("arial",12,"bold"),bg="white",fg="purple")
lbl_user_score.place(x=350,y=180)
# end -------------         user view -------------


# begin-------------         comp view -------------
lbl_comp = tkinter.Label(screen,text="COMPUTER",font=("arial",12,"bold"),bg="white",fg="purple")
lbl_comp.place(x=50,y=230)

lbl_comp_sel = tkinter.Label(screen,textvariable=var_com_sel,font=("arial",12,"bold"),bg="white",fg="purple")
lbl_comp_sel.place(x=200,y=230)

lbl_comp_score = tkinter.Label(screen,textvariable=var_com_score,font=("arial",12,"bold"),bg="white",fg="purple")
lbl_comp_score.place(x=350,y=230)
# end -------------         comp view -------------


btn_result = tkinter.Button(screen,textvariable=var_result,font=("arial",26,"bold"),bg="white",fg="purple",bd=5,width=20)
btn_result.place(x=50,y=280)

screen.mainloop()

