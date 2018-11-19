import ply.yacc as yacc
import lexer
import traductor 
#-------------------------parser----------------------#
tokens = lexer.tokens


# def p_oracion(p):
#     '''
#     oracion : palabra 
#             | palabra oracion
#     '''
#     pass

# def p_palabra(p):
#     '''
#     palabra : SUJETO 
#             | VERBOPP
            
#     '''
#     pass

#--------------------INCORRECT----------------------#

def p_oracionin(p):
    '''
    oracion : VERBOPP SUJETO SUSTANTIVOS
            | VERBOTP SUSTANTIVOS SUJETO
            | SUJETO SUSTANTIVOS VERBOPP
            | SUSTANTIVOS VERBOPP SUJETO
            | SUSTANTIVOS SUJETO VERBOPP
    '''
    p[0] = "gramatica incorrecta"  

#-------------------------1------------------------#
def p_oracion1(p):
    '''
    oracion : SUJETO
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
    p[0] = "GRAMATICA CORRECTA"
    palabras_a_traducir = [];
    palabras_a_traducir.append(p[1]);
    traductor.traducir(palabras_a_traducir)  


#-------------------------2------------------------#
def p_oracion2(p):
    '''
    oracion : SUJETO VERBOPP
            | SUJETO VERBOTP
    '''
    p[0] = "GRAMATICA CORRECTA"
    palabras_a_traducir = [];
    palabras_a_traducir.append(p[1]);
    palabras_a_traducir.append(p[2]);
    traductor.traducir(palabras_a_traducir)  

#-------------------------3------------------------#

def p_oracion3(p):
    '''
    oracion : SUJETO VERBOPP ADJETIVO
            | SUJETO VERBOTP ADJETIVO
            | SUJETO VERBOTP SUSTANTIVOS
    '''
    p[0] = "GRAMATICA CORRECTA"
    palabras_a_traducir = [];
    palabras_a_traducir.append(p[1]);
    palabras_a_traducir.append(p[2]);
    palabras_a_traducir.append(p[3]);
    traductor.traducir(palabras_a_traducir)  

#-------------------------4------------------------#

def p_oracion4(p):
    '''
    oracion : SUJETO VERBOPP SUSTANTIVOS SUSTANTIVOS
            | SUJETO VERBOTP SUSTANTIVOS SUSTANTIVOS
            | SUSTANTIVOS SUJETO VERBOPP SUSTANTIVOS
            | SUSTANTIVOS SUJETO VERBOTP SUSTANTIVOS
            | SUJETO VERBOPP PREPOSICIONES SUSTANTIVOS
            | SUJETO VERBOTP PREPOSICIONES SUSTANTIVOS
            | SUJETO VERBOPP ADVERBIOS SUSTANTIVOS
            | SUJETO VERBOTP ADVERBIOS SUSTANTIVOS
            | SUJETO VERBOPP PREPOSICIONES PRONOMBRES
            | SUJETO VERBOTP PREPOSICIONES PRONOMBRES
            | SUJETO VERBOPP ARTICULOS SUSTANTIVOS
            | SUJETO VERBOTP ARTICULOS SUSTANTIVOS
    '''
    p[0] = "GRAMATICA CORRECTA"
    palabras_a_traducir = [];
    palabras_a_traducir.append(p[1]);
    palabras_a_traducir.append(p[2]);
    palabras_a_traducir.append(p[3]);
    palabras_a_traducir.append(p[4]);
    traductor.traducir(palabras_a_traducir)  


parser = yacc.yacc()



while True:
  try:
    s = input('intro ----->')
  except EOFError:
    break
  print(parser.parse(s.lower()))
 