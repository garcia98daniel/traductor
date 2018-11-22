import ply.yacc as yacc
import lexer
import traductor 
#-------------------------parser----------------------#
tokens = lexer.tokens



#--------------------INCORRECT----------------------#

# def p_oracionin(p):
#     '''
#     oracion : VERBOPP SUJETO SUSTANTIVOS
#             | VERBOTP SUSTANTIVOS SUJETO
#             | SUJETO SUSTANTIVOS VERBOPP
#             | SUSTANTIVOS VERBOPP SUJETO
#             | SUSTANTIVOS SUJETO VERBOPP
#     '''
#     p[0] = "gramatica incorrecta"  


#-------------------------1------------------------#
def p_oracion1(p):
    '''
    oracion : TEXTO
    '''
    p[0] = "GRAMATICA CORRECTA"
    print(p[0])
    palabras_a_traducir = [];
    palabras_a_traducir.append(p[1]);
    p[0] = traductor.traducir(palabras_a_traducir)  


def p_oracion0(p):
    '''
      TEXTO : SUJETO
            | PRONOMBRES
            | SUSTANTIVOS
            | VERBOPP
            | VERBOTP
            | ADJETIVO
            | ADVERBIOS
            | PREPOSICIONES
            | ARTICULOS
            | DEMOSTRATIVOS
            | POSESIVOS
    '''
    p[0] = p[1]


#-------------------------2------------------------#
def p_oracion2(p):
    '''
    oracion : SUJETO VERBOPP
            | SUJETO VERBOTP
            | TEXTO TEXTO
    '''
    p[0] = "GRAMATICA CORRECTA"
    print(p[0])
    palabras_a_traducir = [];
    palabras_a_traducir.append(p[1]);
    palabras_a_traducir.append(p[2]);
    p[0] = traductor.traducir(palabras_a_traducir)  
    

#-------------------------3------------------------#

def p_oracion3(p):
    '''
    oracion : SUJETO VERBOTP TEXTO
            | SUJETO VERBOPP TEXTO 
            | TEXTO TEXTO TEXTO 
    '''
    p[0] = "GRAMATICA CORRECTA"
    print(p[0])
    palabras_a_traducir = [];
    palabras_a_traducir.append(p[1]);
    palabras_a_traducir.append(p[2]);
    palabras_a_traducir.append(p[3]);
    p[0] = traductor.traducir(palabras_a_traducir)  

#-------------------------4------------------------#

def p_oracion4(p):
    '''
    oracion : SUJETO VERBOPP TEXTO TEXTO
            | SUJETO VERBOTP TEXTO TEXTO
            | TEXTO TEXTO TEXTO TEXTO
    '''
    p[0] = "GRAMATICA CORRECTA"
    print(p[0])
    palabras_a_traducir = [];
    palabras_a_traducir.append(p[1]);
    palabras_a_traducir.append(p[2]);
    palabras_a_traducir.append(p[3]);
    palabras_a_traducir.append(p[4]);
    p[0] = resultadotraducion=traductor.traducir(palabras_a_traducir) 

def p_oracion5(p):
    '''
    oracion : SUJETO VERBOPP TEXTO TEXTO TEXTO
            | SUJETO VERBOTP TEXTO TEXTO TEXTO
            | TEXTO TEXTO TEXTO TEXTO TEXTO
    '''
    p[0] = "GRAMATICA CORRECTA"
    print(p[0])
    palabras_a_traducir = [];
    palabras_a_traducir.append(p[1]);
    palabras_a_traducir.append(p[2]);
    palabras_a_traducir.append(p[3]);
    palabras_a_traducir.append(p[4]);
    palabras_a_traducir.append(p[5]);
    p[0] = resultadotraducion=traductor.traducir(palabras_a_traducir) 

def p_oracion6(p):
    '''
    oracion : SUJETO VERBOPP TEXTO TEXTO TEXTO TEXTO
            | SUJETO VERBOTP TEXTO TEXTO TEXTO TEXTO
            | TEXTO TEXTO TEXTO TEXTO TEXTO TEXTO
    '''
    p[0] = "GRAMATICA CORRECTA"
    print(p[0])
    palabras_a_traducir = [];
    palabras_a_traducir.append(p[1]);
    palabras_a_traducir.append(p[2]);
    palabras_a_traducir.append(p[3]);
    palabras_a_traducir.append(p[4]);
    palabras_a_traducir.append(p[5]);
    palabras_a_traducir.append(p[6]);
    p[0] = resultadotraducion=traductor.traducir(palabras_a_traducir)    




from tkinter import *
import pyttsx3

def mein():
    mtext = ment.get()
    parser = yacc.yacc()
    en = pyttsx3.init()
    listadevoces = en.getProperty('voices')
    en.setProperty('rate',150)
    en.setProperty('voice',listadevoces[3].id)
    en.say(mtext)
    en.runAndWait()
    result = parser.parse(mtext.lower())
    mlabel2 = Label(mGui,text=result,font=100,bg="yellow").pack()
  
mGui = Tk()
ment = StringVar()

mGui.geometry("2000x1000")
mGui.title("TRADUCTOR")


mlabel = Label(mGui,text="CAMILO GARCIA Y DANIEL GARCIA",bg="orange",relief=RAISED, font=10).pack()

mbutton = Button(mGui,text = "TRADUCIR", command = mein, fg="blue",bg="lightblue", font=10).pack()

mEntry = Entry(mGui,textvariable=ment,width=50, font=10).pack()


mGui.mainloop()