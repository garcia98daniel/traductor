import ply.lex as lex
import sys

tokens = [
    'SUJETO','PRONOMBRES','SUSTANTIVOS',
    'VERBOPP', 'VERBOTP','ADJETIVO',
    'ADVERBIOS','PREPOSICIONES','ARTICULOS',
    'DEMOSTRATIVOS', 'POSESIVOS'
    ]
t_SUJETO = r'it|you|they|we|he|she|i'

t_PRONOMBRES = r'me|him|her|us|them'
t_SUSTANTIVOS = r'today|day|family|monday|tuesday|wednesday|thursday|friday|saturday|sunday|bed|arm|aircraft|blood|bone|book|bread|bull|bus|car|cat|dog|doll|chair|chicken|coin|face|gall|hat|hand|house|kid|lady|leg|man|mouse|ring|sun|table|woman|exam'

t_VERBOPP = r'am|are|study|cry|travel|pull|cook|dress|learn|listen|ask|call|run|eat|sleep|drink|watch|play|talk|use|jump|love|want|take'
t_VERBOTP = r'is|studies|cries|travels|pulls|cooks|dresses|lerns|listens|asks|calls|runs|eats|sleeps|drinks|watches|plays|talks|uses|takes|jumps|loves|wants'

t_ADJETIVO =  r'fast|good|bad|large|small|long|short|thick|narrow|deep|low|high|near|far|quick|slow|early|late|dark|clear|sunny|cloud|warm|cool|hot|wet'
t_ADVERBIOS = r'very|today|yesterday|tomorrow|late|early|now|never|always|often|sometimes|here|there|everywhere|inside|outside|every' 

t_PREPOSICIONES = r'and|about|after|at|behind|between|by|from|over|without|above|before|below|but|down|for|in|like|of|on|since|to|up|with'
t_ARTICULOS = r'the|a|some|one|few'

#t_DEMOSTRATIVOS = r'those|these|that|this'
#t_POSESIVOS = r'mine|yours|his|hers|ours|yours|theirs'

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