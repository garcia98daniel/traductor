diccionarioENG={'i':1, 'you':2, 'they':3, 'we':4, 'he':5, 'she':6, 'it':7,
                    'me':101, 'you':102, 'him':103, 'her':104, 'us':105, 'them':106, 'it':107,
                    'letter':201, 'book':202, 'car':203, 'dog':204, 'house':205, 'yesterday':206,
                    'am':301, 'are':302, 'write':303, 'dance':304, 'sing':305, 'have':306, 'was':307, 'were':308, 'wrote':309, 'danced':310, 'sang':311, 'had':312,
                    'is':401, 'writes':402, 'dances':403, 'sings':404, 'has':405,
                    'fast':501, 'good':502, 'bad':503, 'large':504, 'small':505,
                    'very':601, 'late':602, 'now':603, 'never':604, 'always':605,
                    'and':701, 'about':702, 'after':703, 'at':704, 'between':705, 
                    'the':801, 'a':802, 'some':803, 'one':804, 'few':805,'with':806,
                    'those':901, 'these':902, 'that':903, 'this':904,
                    'mine':1001, 'your':1002, 'his':1003, 'hers':1004, 'ours':1005, 'theirs':1006};

diccionarioSPA={1:'yo', 2:'tu' , 3:'ellos' , 4:'nosotros', 5:'el', 6:'ella', 7:'eso', 
                101:'me' , 102:'tu' , 103:'el' , 104:'ella', 105:'nosotros', 106:'ellos', 'eso':107, 
                201:'carta' , 202:'libro', 203:'carro' , 204:'perro', 205:'casa', 206:'ayer',
                301:'soy o estoy' , 302:'eres o estas', 303:'escribir', 304:'bailar', 305:'cantar', 306:'tener', 307:'era o estaba' , 308:'fueron', 309:'escribio', 310:'bailo', 311:'canto', 312:'tenia',
                401:'es o esta' , 402:'escribe', 403:'baila' , 404:'canta', 405:'tiene',
                501:'rapido' , 502:'bueno', 503:'malo' , 504:'largo', 505:'pequeño', 
                601:'muy', 602:'tarde', 603:'ahora', 604:'nunca', 605:'siempre',                                                                                                                                                                
                701:'y' , 702:'acerca de', 703:'despues' , 704:'en', 705:'entre', 
                801:'el, o, la' , 802:'un, o, una', 803:'algun' , 804:'un@', 805:'algunos',806:'con',
                901:'esos' , 902:'estos', 903:'eso' , 904:'esto',
                1001:'mio' , 1002:'tuyo', 1003:'su' , 1004:'su', 1005:'nuestro', 1006:'sus'};

diccionarioYO={301:'soy o estoy', 303:'escribo', 304:'bailo', 305:'canto', 306:'tengo', 307:'era o estaba', 309:'escribi', 310:'baile', 311:'cante', 312:'tenia'}
diccionarioTU={302:'eres o estas', 303:'escribes', 304:'bailas', 305:'cantas', 306:'tienes', 308:'eras o estabas', 309:'escribiste', 310:'bailaste', 311:'cantaste', 312:'tenias'}
diccionarioELLOS={302:'son o estan', 303:'escriben', 304:'bailan', 305:'cantan', 306:'tienen', 308:'eran o estaban', 309:'escribieron', 310:'bailaron', 311:'cantaron', 312:'tenian'}
diccionarioNOSOTROS={302:'somos o estamos', 303:'escribimos', 304:'bailamos', 305:'cantamos', 306:'tenemos', 308:'eramos o estabamos', 309:'escribimos', 310:'bailamos', 311:'cantamos', 312:'teniamos'}
diccionarioTERCERAP={401:'es o esta', 303:'escribe', 403:'baila', 404:'canta', 405:'tiene', 307:'era o estaba', 309:'escribio', 310:'bailo', 311:'canto', 312:'tenia'}
listaVerbos=['am', 'are', 'write', 'dance', 'sing', 'have', 'was', 'were', 'wrote', 'danced', 'sang', 'had', 'is', 'writes', 'dances', 'sings' ]

import pyttsx3

def traducir(palabras_a_traducir):
    en = pyttsx3.init()
    cadenaTraducida=""
    x=0
    while x < len(palabras_a_traducir):
      # print(x)
      # print(palabras_a_traducir[x])    
      
      if(len(palabras_a_traducir)==1 and (palabras_a_traducir[x]=="i" or palabras_a_traducir[x]=="you" or palabras_a_traducir[x]=="he" or palabras_a_traducir[x]=="she" or palabras_a_traducir[x]=="it" or palabras_a_traducir[x]=="we" or palabras_a_traducir[x]=="they")):
          cadenaTraducida+=" "+diccionarioSPA[diccionarioENG[palabras_a_traducir[x]]]
          break
      else:
        cadenaTraducida+=" "+diccionarioSPA[diccionarioENG[palabras_a_traducir[x]]]
        if(palabras_a_traducir[x]=='i'):
          
          if(es_verbo(x+1,palabras_a_traducir)):
            x+=1
            sig=palabras_a_traducir[x]
            cadenaTraducida+=" "+diccionarioYO[diccionarioENG[sig]]
        elif(palabras_a_traducir[x]=='you'):
          
          if(es_verbo(x+1,palabras_a_traducir)):
            x+=1
            sig=palabras_a_traducir[x]
            cadenaTraducida+=" "+diccionarioTU[diccionarioENG[sig]]
        elif(palabras_a_traducir[x]=='he'):
          
          if(es_verbo(x+1,palabras_a_traducir)):
            x+=1
            sig=palabras_a_traducir[x]
            cadenaTraducida+=" "+diccionarioTERCERAP[diccionarioENG[sig]]
        elif(palabras_a_traducir[x]=='she'):
          
          if(es_verbo(x+1,palabras_a_traducir)):
            x+=1
            sig=palabras_a_traducir[x]
            cadenaTraducida+=" "+diccionarioTERCERAP[diccionarioENG[sig]]
        elif(palabras_a_traducir[x]=='it'):
          
          if(es_verbo(x+1,palabras_a_traducir)):
            x+=1
            sig=palabras_a_traducir[x]
            cadenaTraducida+=" "+diccionarioTERCERAP[diccionarioENG[sig]]
        elif(palabras_a_traducir[x]=='we'):
          
          if(es_verbo(x+1,palabras_a_traducir)):
            x+=1
            sig=palabras_a_traducir[x]
            cadenaTraducida+=" "+diccionarioNOSOTROS[diccionarioENG[sig]]
        elif(palabras_a_traducir[x]=='they'):
          
          if(es_verbo(x+1,palabras_a_traducir)):
            x+=1
            sig=palabras_a_traducir[x]
            cadenaTraducida+=" "+diccionarioELLOS[diccionarioENG[sig]]
        

      x=x+1;


    listadevoces = en.getProperty('voices')
    en.setProperty('rate',130)
    en.setProperty('voice',listadevoces[0].id)
    en.say(cadenaTraducida)
    en.runAndWait()
    print(cadenaTraducida);
    return cadenaTraducida
 

def es_verbo(indice,palabras_a_traducir):

    if(listaVerbos.index(palabras_a_traducir[indice]) >= 0):
      return True
    else:
      return False
     

