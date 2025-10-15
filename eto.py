import FreeSimpleGUI as sg
sg.theme("DarkBrown3")

layout =[[sg.Text("指定された年の干支を調べます。")],
         [sg.Text("西暦何年生まれですか?"),sg.Input("2000",key="in1")],
         [sg.Button("実行",key="btn"),sg.Text(key="txt")]]

win=sg.Window("干支調べアプリ",layout,
              font=(None,14),size=(320,150))

def execute():
    in1=int(values["in1"])
    eto=["子","丑","寅","卯","辰","巳","午","末","申","酉","戌","亥"]
    number=int((in1-4)%12)
    txt=(f"{in1}は、{eto[number]}年です。")
    win["txt"].update(txt)
    

while True:
    event,values = win.read()
    if event == "btn":
        execute()
    if event == None:
        break

win.close()
