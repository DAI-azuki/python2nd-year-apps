import FreeSimpleGUI as sg
import random

sg.theme("Darkbrown3")

layout = [
    [sg.T("私とじゃんけんしよう！")],
    [sg.T(key="txt")],
    [
        sg.B("グー", key="choise0"),
        sg.B("チョキ", key="choise1"),
        sg.B("パー", key="choise2"),
        sg.B("降参", key="choise3"),
    ],
]

win = sg.Window("じゃんけんアプリ", layout, font=(None, 30))
sort = ["グー", "チョキ", "パー", "降参"]
conclude = ["あいこ", "勝ち", "負け"]


def jyanken(mynum):

    comnum = random.randint(0, 2)
    if mynum <= 2:
        hantei = (comnum - mynum) % 3
    else:
        hantei = 2
    win["txt"].update(
        "私は" + sort[comnum] + "を出しました。あなたは" + conclude[hantei] + "です"
    )


while True:
    e, v = win.read()
    if e == "choise0":
        jyanken(0)
    if e == "choise1":
        jyanken(1)
    if e == "choise2":
        jyanken(2)
    if e == "choise3":
        jyanken(3)
    if e == None:
        break

win.close()
