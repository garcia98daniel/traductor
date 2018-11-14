import ply.lex as lex

tokens = [
    'VERBOSPRERUN', 'VERBOSPREEAT','VERBOSPRESLEEP',
    'VERBOSPREDRINK','VERBOSPREWATCH','VERBOSPREPLAY',
    'VERBOSPRETALK','VERBOSPREUSE','VERBOSPRELOVE',
    'VERBOSPREWANT',

    'PronombrePI','PronombrePYOU',
    'PronombrePHE','PronombrePISHE','PronombrePIIT',
    'PronombrePWE','PronombrePTHEY',

    'AdjetivoHEAVY','AdjetivoFAST',
    'AdjetivoBIG','AdjetivoSMALL',
    'AdjetivoHAPPY','AdjetivoGOOD','AdjetivoBAD',
    'AdjetivoFAT','AdjetivoBLACK','AdjetivoSAD',
    'AdjetivoWHITE','AdjetivoTALL','AdjetivoSHORT'
    ]

t_VERBOSPRERUN = r'[rR][uU][nN]'
t_VERBOSPREEAT = r'[eE][aA][tT]'
t_VERBOSPRESLEEP = r'[sS][lL][eE][eE][pP]'
t_VERBOSPREDRINK = r'[dD][rR][iI][nN][kK]'
t_VERBOSPREWATCH = r'[wW][aA][tT][cC][hH]'
t_VERBOSPREPLAY = r'[pP][lL][aA][yY]'
t_VERBOSPRETALK = r'[tT][aA][lL][kK]' 
t_VERBOSPREUSE = r'[uU][sS][eE]'
t_VERBOSPRELOVE = r'[lL][oO][vV][eE]'
t_VERBOSPREWANT = r'[wW][aA][nN][tT]'

t_PronombrePI  = r'[iI]'
t_PronombrePYOU = r'[yY][oO][uU]'
t_PronombrePHE = r'[hH][eE]'
t_PronombrePISHE = r'[sS][hH][eE]'
t_PronombrePIIT = r'[iI][tT]'
t_PronombrePWE = r'[wW][eE]'
t_PronombrePTHEY = r'[tT][hH][eE][yY]'

t_AdjetivoBIG = r'[bB][iI][gG]'
t_AdjetivoSMALL = r'[sS][mM][aA][lL][lL]'
t_AdjetivoHAPPY = r'[hH][aA][pP][pP][yY]'
t_AdjetivoGOOD = r'[gG][oO][oO][dD]'
t_AdjetivoBAD = r'[bB][aA][dD]'
t_AdjetivoFAT = r'[fF][aA][tT]'
t_AdjetivoBLACK = r'[bB][lL][aA][cC][kK]'
t_AdjetivoSAD = r'[sS][aA][dD]'
t_AdjetivoWHITE = r'[wW][hH][iI][tT][eE]'
t_AdjetivoTALL = r'[tT][aA][lL][lL]'
t_AdjetivoSHORT = r'[sS][hH][oO][rR][tT]'
t_AdjetivoHEAVY = r'[hH][eE][aA][vV][yY]'
t_AdjetivoFAST = r'[fF][aA][sS][tT]'

t_ignore = " "

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

contenido = open("codigo.txt")
while contenido != "":
    lexer.input(contenido.readline())
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)