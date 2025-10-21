import FreeSimpleGUI as sg
import random

sg.theme("DarkBrown3")

layout = [
    [sg.T("31ゲームをしよう。31を言ったら負け")],
    [sg.T(k="txt1")],
    [sg.T("数を入力してください", k="txt2")],
    [sg.I("1", k="in1", size=(15)), sg.B("入力", k="btn", bind_return_key=True)],
]
win = sg.Window("31ゲーム", layout, font=(None, 14), finalize=True)


def getnextnums(n):
    global nextnums, choicemsg
    nextnums = list(range(n + 1, min(32, n + 4)))
    choicemsg = f"{nextnums}から入力してください"
    win["txt2"].update(choicemsg)


def question():
    global playflag
    getnextnums(0)
    win["txt1"].update("さあゲームを始めるよ！")
    playflag = True


def com_turn(comnum):
    keynums = [2, 6, 10, 14, 18, 22, 26, 30]
    getnextnums(comnum)
    for n in nextnums:
        if n in keynums:
            comnum = n
    if random.randint(0, 1) > 0:
        comnum = nextnums[0]
    win["txt1"].update(f"私は[{comnum}]にするよ")
    getnextnums(comnum)


def my_turn():
    global playflag
    if v["in1"].isdecimal() == False:
        win["txt1"].update("数字を入力してね")
    else:
        mynum = int(v["in1"])
        if mynum in nextnums:
            if mynum == 31:
                win["txt1"].update("31!!!おまえのまけ")
                playflag = False
            elif mynum == 30:
                win["txt1"].update("おまえの勝ちだ泣")
                playflag = False
            else:
                com_turn(mynum)


question()
while True:
    e, v = win.read()
    if e == "btn":
        if playflag == False:
            question()
        else:
            my_turn()
    if e == None:
        break
win.close()
