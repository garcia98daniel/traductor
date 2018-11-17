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
            | VERBOPRESENTE OBJETODIRECTO SUJETO
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
    palabras_a_traducir = [];
    palabras_a_traducir.append(p[1]);
    palabras_a_traducir.append(p[2]);
    palabras_a_traducir.append(p[3]);
    traductor.traducir(palabras_a_traducir)  

parser = yacc.yacc()



while True:
  try:
    s = input('intro ----->')
  except EOFError:
    break
  print(parser.parse(s.lower()))
 