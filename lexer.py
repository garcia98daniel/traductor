import ply.lex as lex
import sys

tokens = [
    'SUJETO','PRONOMBRES','SUSTANTIVOS',
     'VERBOS','ADJETIVO',
    'ADVERBIOS','PREPOSICIONES',
    'ARTICULOS','DEMOSTRATIVOS', 'POSESIVOS'
    
    ]
t_SUJETO = r'it|you|they|we|she|her|i|he'

t_PRONOMBRES = r'me|her|him|us|them'
t_SUSTANTIVOS = r'letter|book|car|dog|house|yesterday'

t_VERBOS = r'is|writes|dances|sings|has|am|are|write|dance|sing|have|was|were|wrote|danced|sang|had'

t_ADJETIVO =  r'fast|good|bad|large|small'
t_ADVERBIOS = r'very|late|now|never|always' 

t_PREPOSICIONES = r'and|about|after|at|between'
t_ARTICULOS = r'the|a|some|one|few|with'

t_DEMOSTRATIVOS = r'those|these|that|this'
t_POSESIVOS = r'mine|yours|his|hers|ours|yours|theirs'

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