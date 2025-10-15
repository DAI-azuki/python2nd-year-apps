import FreeSimpleGUI as sg
sg.theme("DarkBrown3")

layout =[[sg.Text("身長と体重を入力してください")],
         [sg.Text("身長cm"),sg.Input("170",key="in1")],
         [sg.Text("体重kg"),sg.Input("60",key="in2")],
         [sg.Button("実行",key="btn"),sg.Text(key="txt")]]

win=sg.Window("BMI計算アプリ",layout,
              font=(None,14),size=(320,150))

def execute():
    in1=int(values["in1"])
    in2=int(values["in2"])
    bmi=in2/((in1/100)**2)
    txt=f"BMI値は{bmi:.2f}です"
    win["txt"].update(txt)
    


while True:
    event,values = win.read()
    if event == "btn":
        execute()
    if event == None:
        break

win.close()
