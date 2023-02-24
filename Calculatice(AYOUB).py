########################################################BY_AYOUB#################################################
#                                                                                                               #
#                AAA          YYYYYYY       YYYYYYY    OOOOOOOOO    UUUUUUUU     UUUUUUUBBBBBBBBBBBBBBBBB       #
#               A:::A         Y:::::Y       Y:::::Y  OO:::::::::OO  U::::::U     U::::::B::::::::::::::::B      #
#              A:::::A        Y:::::Y       Y:::::YOO:::::::::::::OOU::::::U     U::::::B::::::BBBBBB:::::B     #
#             A:::::::A       Y::::::Y     Y::::::O:::::::OOO:::::::UU:::::U     U:::::UBB:::::B     B:::::     #
#            A:::::::::A      YYY:::::Y   Y:::::YYO::::::O   O::::::OU:::::U     U:::::U  B::::B     B:::::     #
#           A:::::A:::::A        Y:::::Y Y:::::Y  O:::::O     O:::::OU:::::D     D:::::U  B::::B     B:::::     #
#          A:::::A A:::::A        Y:::::Y:::::Y   O:::::O     O:::::OU:::::D     D:::::U  B::::BBBBBB:::::B     #
#         A:::::A   A:::::A        Y:::::::::Y    O:::::O     O:::::OU:::::D     D:::::U  B:::::::::::::BB      #
#        A:::::A     A:::::A        Y:::::::Y     O:::::O     O:::::OU:::::D     D:::::U  B::::BBBBBB:::::B     #
#       A:::::AAAAAAAAA:::::A        Y:::::Y      O:::::O     O:::::OU:::::D     D:::::U  B::::B     B:::::     #
#      A:::::::::::::::::::::A       Y:::::Y      O:::::O     O:::::OU:::::D     D:::::U  B::::B     B:::::     #
#     A:::::AAAAAAAAAAAAA:::::A      Y:::::Y      O::::::O   O::::::OU::::::U   U::::::U  B::::B     B:::::     #
#    A:::::A             A:::::A     Y:::::Y      O:::::::OOO:::::::OU:::::::UUU:::::::UBB:::::BBBBBB::::::     #
#   A:::::A               A:::::A YYYY:::::YYYY    OO:::::::::::::OO  UU:::::::::::::UU B:::::::::::::::::B     #
#  A:::::A                 A:::::AY:::::::::::Y      OO:::::::::OO      UU:::::::::UU   B::::::::::::::::B      #
# AAAAAAA                   AAAAAAYYYYYYYYYYYYY        OOOOOOOOO          UUUUUUUUU     BBBBBBBBBBBBBBBBB       #
#                                                                                                               #
########################################################BY_AYOUB#################################################                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
from asyncio.proactor_events import _ProactorDuplexPipeTransport
from tkinter import *
import tkinter as tk




root=tk.Tk()
root.title("Calculatrice")
root.geometry("313x394")
root.maxsize(313,394)
root.minsize(313,394)

root.iconbitmap("C:/Users/ayoub/Downloads/calculatrice.ico")
root.config(background="#626060")

# creat ecran
text_resultat=tk.Text(root, height=3, bg="#1A1A1A", fg= "white", width=int(19), font=("Courrier", 22))
text_resultat.grid(columnspan=10)

# Create Frame
frame1 = Frame(root, bg="#626060")
frame1.grid()

# calcul
calcul=""

def add_calcul(symbol):
    global calcul
    calcul += str(symbol)
    text_resultat.delete(1.0,"end")
    text_resultat.insert(1.0, calcul)  
def eval_calcul():
    global calcul
    try:
        calcul=str(eval(calcul))
        text_resultat.delete(1.0,"end")
        text_resultat.insert(1.0, calcul)
    except:
        effacer_ecran()
        text_resultat.insert(1.0, "Erreur")
def effacer_ecran():
    global calcul
    calcul = ""
    text_resultat.delete(1.0,"end")


# Add buttons
button1 = Button( frame1, text ="７",bg="#1A1A1A",fg="white", font=("Courrier", 22), width=4, command=lambda:add_calcul(7))
button1.grid(row=2, column=1)
button1.grid()

button2 = Button( frame1, text ="８",bg="#1A1A1A",fg="white", font=("Courrier", 22), width=4, command=lambda:add_calcul(8))
button2.grid(row=2, column=2)
button2.grid()

button3 = Button( frame1, text ="９",bg="#1A1A1A",fg="white", font=("Courrier", 22), width=4, command=lambda:add_calcul(9))
button3.grid(row=2, column=3)
button3.grid()

buttonX = Button( frame1, text ="x",bg="#3D3D3D",fg="white", font=("Courrier", 22), width=4, command=lambda:add_calcul("*"))
buttonX.grid(row=2, column=4)
buttonX.grid()

button4 = Button( frame1, text ="４",bg="#1A1A1A",fg="white", font=("Courrier", 22), width=4, command=lambda:add_calcul(4))
button4.grid(row=3, column=1)
button4.grid()

button5 = Button( frame1, text ="５",bg="#1A1A1A",fg="white", font=("Courrier", 22), width=4, command=lambda:add_calcul(5))
button5.grid(row=3, column=2)
button5.grid()

button6 = Button( frame1, text ="６",bg="#1A1A1A",fg="white", font=("Courrier", 22), width=4, command=lambda:add_calcul(6))
button6.grid(row=3, column=3)
button6.grid()

button7 = Button( frame1, text ="１",bg="#1A1A1A",fg="white", font=("Courrier", 22), width=4, command=lambda:add_calcul(1))
button7.grid(row=4, column=1)
button7.grid()

button8 = Button( frame1, text ="２",bg="#1A1A1A",fg="white", font=("Courrier", 22), width=4, command=lambda:add_calcul(2))
button8.grid(row=4, column=2)
button8.grid()

button9 = Button( frame1, text ="３",bg="#1A1A1A",fg="white", font=("Courrier", 22), width=4, command=lambda:add_calcul(3))
button9.grid(row=4, column=3)
button9.grid()

button0 = Button( frame1, text ="０",bg="#1A1A1A",fg="white", font=("Courrier", 22), width=4, command=lambda:add_calcul(0))
button0.grid(row=5, column=2)
button0.grid()

buttonA = Button( frame1, text =",",bg="#1A1A1A",fg="white", font=("Courrier", 22), width=4, command=lambda:add_calcul(","))
buttonA.grid(row=5, column=3)
buttonA.grid()

buttonB = Button( frame1, text ="＝",bg="#9F1818",fg="white", font=("Courrier", 22), width=4, command=lambda:eval_calcul())
buttonB.grid(row=5, column=4)
buttonB.grid()

buttonC = Button( frame1, text ="AC",bg="#9F1818",fg="white", font=("courrier", 22), width=4, command=lambda:effacer_ecran())
buttonC.grid(row=5, column=1)
buttonC.grid()

buttonD = Button( frame1, text ="–",bg="#3D3D3D",fg="white", font=("Courrier", 22), width=4, command=lambda:add_calcul("-"))
buttonD.grid(row=3, column=4)
buttonD.grid()

buttonE = Button( frame1, text ="+",bg="#3D3D3D",fg="white", font=("Courrier", 22), width=4, command=lambda:add_calcul("+"))
buttonE.grid(row=4, column=4)
buttonE.grid()

buttonF = Button( frame1, text ="%",bg="#3D3D3D",fg="white", font=("Courrier", 22), width=4, command=lambda:add_calcul("%"))
buttonF.grid(row=1, column=1)
buttonF.grid()

buttonJ = Button( frame1, text ="(",bg="#3D3D3D",fg="white", font=("Courrier", 22), width=4, command=lambda:add_calcul("("))
buttonJ.grid(row=1, column=2)
buttonJ.grid()

buttonH = Button( frame1, text =")",bg="#3D3D3D",fg="white", font=("Courrier", 22), width=4, command=lambda:add_calcul(")"))
buttonH.grid(row=1, column=3)
buttonH.grid()

buttonI = Button( frame1, text ="÷",bg="#3D3D3D",fg="white", font=("Courrier", 22), width=4, command=lambda:add_calcul("/"))
buttonI.grid(row=1, column=4)
buttonI.grid()

# affichage
root.mainloop()



















