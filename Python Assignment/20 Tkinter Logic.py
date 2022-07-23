import tkinter
import random

screen = tkinter.Tk()
screen.title("MY APP")
screen.config(background="white")
screen.geometry("540x450")


var_com_sel = tkinter.StringVar()
var_com_score = tkinter.IntVar()

var_user_sel = tkinter.StringVar()
var_user_score = tkinter.IntVar()

var_result = tkinter.StringVar()
var_result.set("RESULT")


GAME_LIST = ["ROCK","PAPER","SCISSOR"]

u_count = 0
c_count = 0
def myfun(user_sel):
    global u_count , c_count
    com = random.choice(GAME_LIST)
    var_user_sel.set(user_sel)
    var_com_sel.set(com)

    if user_sel=="ROCK" and com=="PAPER":
        var_result.set("COMPUTER WON !!!")
        c_count+=1
    elif user_sel=="ROCK" and com=="SCISSOR":
        u_count+=1
        var_result.set("USER WON !!!")

    elif user_sel=="PAPER" and com=="ROCK":
        u_count+=1
        var_result.set("USER WON !!!")
    elif user_sel=="PAPER" and com=="SCISSOR":
        c_count+=1
        var_result.set("COMPUTER WON !!!")

    elif user_sel=="SCISSOR" and com=="ROCK":
        c_count+=1
        var_result.set("COMPUTER WON !!!")
    elif user_sel=="SCISSOR" and com=="PAPER":
        u_count+=1
        var_result.set("USER WON !!!")
    else:
        var_result.set("TIE !!!")
    var_com_score.set(c_count)
    var_user_score.set(u_count)
