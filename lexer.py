import ply.lex as lex
import sys

tokens = [
    'SUJETO', 'VERBOPRESENTE', 'OBJETODIRECTO' 
    ]


t_SUJETO = r'[iI][tT]|[yY][oO][uU]|[hH][eE]|[sS][hH][eE]|[iI]|[wW][eE]|[tT][hH][eE][yY]'

t_VERBOPRESENTE = r'[rR][uU][nN]|[eE][aA][tT]|[sS][lL][eE][eE][pP]|[dD][rR][iI][nN][kK]|[wW][aA][tT][cC][hH]|[pP][lL][aA][yY]|[tT][aA][lL][kK]|[uU][sS][eE]|[jJ][uU][mM][pP]|[lL][oO][vV][eE]|[wW][aA][nN][tT]'

t_OBJETODIRECTO =  r'[tT][vV]|[fF][aA][sS][tT]|[fF][uU][tT][bB][oO][lL]|[pP][iI][zZ][zZ][aA]|[aA][lL][oO][nN][eE]|[gG][oO][oO][dD]'
    

t_ignore = " "

def t_error(t):
    print("Illegal character ")
    t.lexer.skip(1)

lexer = lex.lex()


# lexer.input('I fast eat')
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)

