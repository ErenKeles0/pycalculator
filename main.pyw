import tkinter as tk


window=tk.Tk()
window.title("Calculator")
window.geometry("500x500")
window.resizable(width=False, height=False)
window.configure(background="black")
global x
x=""

def esittir():
    global x
    global sonuc
    try:
        x=str(eval(x))
        sonuc["text"]=x
    except SyntaxError:
        x="Error"
        sonuc["text"]=x

def C():
    global x
    global sonuc
    x=""
    sonuc["text"]=x

def basildi0():
    global x
    global sonuc
    if x=="":
        pass
    else:
        x=x+"0"
        sonuc["text"]=x

def basildi1():
    global x
    global sonuc
    x=x+"1"
    sonuc["text"]=x

def basildi2():
    global x
    global sonuc
    x=x+"2"
    sonuc["text"]=x
def basildi3():
    global x
    global sonuc
    x=x+"3"
    sonuc["text"]=x
def basildi4():
    global x
    global sonuc
    x=x+"4"
    sonuc["text"]=x
def basildi5():
    global x
    global sonuc
    x=x+"5"
    sonuc["text"]=x
def basildi6():
    global x
    global sonuc
    x=x+"6"
    sonuc["text"]=x
def basildi7():
    global x
    global sonuc
    x=x+"7"
    sonuc["text"]=x
def basildi8():
    global x
    global sonuc
    x=x+"8"
    sonuc["text"]=x
def basildi9():
    global x
    global sonuc
    x=x+"9"
    sonuc["text"]=x
def basildiplus():
    global x
    global sonuc
    x=x+"+"
    sonuc["text"]=x
def basildiminus():
    global x
    global sonuc
    x=x+"-"
    sonuc["text"]=x
def basildiimpact():
    global x
    global sonuc
    x=x+"*"
    sonuc["text"]=x
def basildidivide():
    global x
    global sonuc
    x=x+"/"
    sonuc["text"]=x
def basildinokta():
    global x
    global sonuc
    x=x+"."
    sonuc["text"]=x
def sil():
    global x
    global sonuc
    x=x[0:-1]
    sonuc["text"]=x


global sonuc
sonuc=tk.Label(text=x,fg="white",bg="black",font="Verdana 32",height=2,anchor="w")
sonuc.place(x=0,y=0)



buton1=tk.Button(text="1",command=basildi1,fg="white",bg="black",font="Verdana 28")
buton2=tk.Button(text="2",command=basildi2,fg="white",bg="black",font="Verdana 28")
buton3=tk.Button(text="3",command=basildi3,fg="white",bg="black",font="Verdana 28")
buton4=tk.Button(text="4",command=basildi4,fg="white",bg="black",font="Verdana 28")
buton5=tk.Button(text="5",command=basildi5,fg="white",bg="black",font="Verdana 28")
buton6=tk.Button(text="6",command=basildi6,fg="white",bg="black",font="Verdana 28")
buton7=tk.Button(text="7",command=basildi7,fg="white",bg="black",font="Verdana 28")
buton8=tk.Button(text="8",command=basildi8,fg="white",bg="black",font="Verdana 28")
buton9=tk.Button(text="9",command=basildi9,fg="white",bg="black",font="Verdana 28")
buton10=tk.Button(text="+",command=basildiplus,fg="white",bg="black",font="Verdana 28")
buton11=tk.Button(text="-",command=basildiminus,fg="white",bg="black",font="Verdana 28")
buton12=tk.Button(text="/",command=basildidivide,fg="white",bg="black",font="Verdana 28")
buton13=tk.Button(text="X",command=basildiimpact,fg="white",bg="black",font="Verdana 28")
buton14=tk.Button(text="=",command=esittir,fg="white",bg="black",font="Verdana 28")
buton15=tk.Button(text="C",command=C,fg="white",bg="black",font="Verdana 28")
buton16=tk.Button(text="0",command=basildi0,fg="white",bg="black",font="Verdana 28")
buton17=tk.Button(text=".",command=basildinokta,fg="white",bg="black",font="Verdana 28")
buton18=tk.Button(text="⌫",command=sil,fg="white",bg="black",font="Verdana 28")

buton1.place(x=0,y=100,width=100,height=100)
buton2.place(x=100,y=100,width=100,height=100)
buton3.place(x=200,y=100,width=100,height=100)
buton4.place(x=0,y=200,width=100,height=100)
buton5.place(x=100,y=200,width=100,height=100)
buton6.place(x=200,y=200,width=100,height=100)
buton7.place(x=0,y=300,width=100,height=100)
buton8.place(x=100,y=300,width=100,height=100)
buton9.place(x=200,y=300,width=100,height=100)
buton10.place(x=300,y=100,width=100,height=100)
buton11.place(x=300,y=200,width=100,height=100)
buton12.place(x=300,y=400,width=100,height=100)
buton13.place(x=300,y=300,width=100,height=100)
buton17.place(x=200,y=400,width=100,height=100)
buton15.place(x=0,y=400,width=100,height=100)
buton16.place(x=100,y=400,width=100,height=100)
buton14.place(x=400,y=300,width=100,height=200)
buton18.place(x=400,y=100,width=100,height=200)


























window.mainloop()
