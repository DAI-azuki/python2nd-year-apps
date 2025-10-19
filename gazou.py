import FreeSimpleGUI as sg        
from PIL import Image
import io

sg.theme("DarkBrown3")

layout = [
    [sg.Button("ファイルを開く", key="btn1"), sg.Text("", key="txt")],
    [sg.Image(key="img")]
]
win = sg.Window("画像ファイルを表示", layout, size=(320, 380))

def loadimage():
    loadname = sg.popup_get_file("画像ファイルを選択してください。")
    if not loadname:         
        return
    try:
        img = Image.open(loadname)   
        img.thumbnail((300, 300))   
        bio = io.BytesIO()          
        img.save(bio, format="PNG") 
        win["img"].update(data=bio.getvalue()) 
        win["txt"].update(loadname)             
    except Exception as e:
        win["img"].update()                    
        win["txt"].update(f"失敗しました… {e}")  

while True:
    e, v = win.read()
    if e in (sg.WIN_CLOSED, None):
        break
    if e == "btn1":
        loadimage()

win.close()
