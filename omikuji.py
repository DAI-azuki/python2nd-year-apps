import FreeSimpleGUI as sg
import random

sg.theme("DarkBrown3")

layout = [
    [sg.T("さあ、おみくじを引きましょう")],
    [sg.B("おみくじ", k="btn")],
    [sg.T(k="txt")],
]

win = sg.Window("おみくじアプリ", layout, font=(None, 14))


def omikuji():
    list = ["大吉", "中吉", "小吉"]
    kan = random.choice(list)
    txt = f"{kan}です。おめでとう"
    win["txt"].update(txt)


while True:
    e, v = win.read()
    if e == "btn":
        omikuji()
    if e == None:
        break

win.close()
