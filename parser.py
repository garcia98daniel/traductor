import ply.yacc as yacc
import lexer
import traductor
#-------------------------parser----------------------#
tokens = lexer.tokens


def p_oracion(p):
    '''
    oracion : palabra 
            | palabra oracion
    '''
    pass

def p_palabra(p):
    '''
    palabra : SUJETO 
            | VERBOPRESENTE
            | OBJETODIRECTO
    '''
    pass

def p_oracionin(p):
    '''
    oracion : VERBOPRESENTE SUJETO OBJETODIRECTO
            | SUJETO OBJETODIRECTO VERBOPRESENTE
            | OBJETODIRECTO VERBOPRESENTE SUJETO
            | OBJETODIRECTO SUJETO VERBOPRESENTE
    '''
    p[0] = "gramatica incorrecta"  



def p_oracionc(p):
    '''
    oracion : SUJETO VERBOPRESENTE OBJETODIRECTO
    '''
    p[0] = "GRAMATICA CORRECTA"
    #print("holaaaaaaaaaaaaaaaaaaaaaaaa")
    #traducir(p.SUJETO,p.VERBOPRESENTE,p.OBJETODIRECTO)  


parser = yacc.yacc()


while True:
  try:
    s = input('intro ----->')
  except EOFError:
    break
  print(parser.parse(s))
 