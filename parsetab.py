
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADJETIVO ADVERBIOS ARTICULOS DEMOSTRATIVOS POSESIVOS PREPOSICIONES PRONOMBRES SUJETO SUSTANTIVOS VERBOPP VERBOTP\n    oracion : VERBOPP SUJETO SUSTANTIVOS\n            | VERBOTP SUSTANTIVOS SUJETO\n            | SUJETO SUSTANTIVOS VERBOPP\n            | SUSTANTIVOS VERBOPP SUJETO\n            | SUSTANTIVOS SUJETO VERBOPP\n    \n    oracion : SUJETO\n            | PRONOMBRES\n            | SUSTANTIVOS\n            | VERBOPP\n            | VERBOTP\n            | ADJETIVO\n            | ADVERBIOS\n            | PREPOSICIONES\n            | ARTICULOS\n            | DEMOSTRATIVOS\n            | POSESIVOS\n    \n    oracion : SUJETO VERBOPP\n            | SUJETO VERBOTP\n    \n    oracion : SUJETO VERBOPP ADJETIVO\n            | SUJETO VERBOTP ADJETIVO\n            | SUJETO VERBOTP SUSTANTIVOS\n    \n    oracion : SUJETO VERBOPP SUSTANTIVOS SUSTANTIVOS\n            | SUJETO VERBOTP SUSTANTIVOS SUSTANTIVOS\n            | SUSTANTIVOS SUJETO VERBOPP SUSTANTIVOS\n            | SUSTANTIVOS SUJETO VERBOTP SUSTANTIVOS\n            | SUJETO VERBOPP PREPOSICIONES SUSTANTIVOS\n            | SUJETO VERBOTP PREPOSICIONES SUSTANTIVOS\n            | SUJETO VERBOPP ADVERBIOS SUSTANTIVOS\n            | SUJETO VERBOTP ADVERBIOS SUSTANTIVOS\n            | SUJETO VERBOPP PREPOSICIONES PRONOMBRES\n            | SUJETO VERBOTP PREPOSICIONES PRONOMBRES\n            | SUJETO VERBOPP ARTICULOS SUSTANTIVOS\n            | SUJETO VERBOTP ARTICULOS SUSTANTIVOS\n    '
    
_lr_action_items = {'VERBOPP':([0,3,4,14,18,],[2,15,17,21,33,]),'VERBOTP':([0,3,18,],[5,16,34,]),'SUJETO':([0,2,4,17,19,],[3,13,18,32,35,]),'SUSTANTIVOS':([0,3,5,13,15,16,23,24,25,26,28,29,30,31,33,34,],[4,14,19,20,23,28,36,37,39,40,41,42,44,45,46,47,]),'PRONOMBRES':([0,24,29,],[6,38,43,]),'ADJETIVO':([0,15,16,],[7,22,27,]),'ADVERBIOS':([0,15,16,],[8,25,30,]),'PREPOSICIONES':([0,15,16,],[9,24,29,]),'ARTICULOS':([0,15,16,],[10,26,31,]),'DEMOSTRATIVOS':([0,],[11,]),'POSESIVOS':([0,],[12,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,15,16,20,21,22,27,28,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,],[0,-9,-6,-8,-10,-7,-11,-12,-13,-14,-15,-16,-17,-18,-1,-3,-19,-20,-21,-4,-5,-2,-22,-26,-30,-28,-32,-23,-27,-31,-29,-33,-24,-25,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'oracion':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> oracion","S'",1,None,None,None),
  ('oracion -> VERBOPP SUJETO SUSTANTIVOS','oracion',3,'p_oracionin','parser.py',27),
  ('oracion -> VERBOTP SUSTANTIVOS SUJETO','oracion',3,'p_oracionin','parser.py',28),
  ('oracion -> SUJETO SUSTANTIVOS VERBOPP','oracion',3,'p_oracionin','parser.py',29),
  ('oracion -> SUSTANTIVOS VERBOPP SUJETO','oracion',3,'p_oracionin','parser.py',30),
  ('oracion -> SUSTANTIVOS SUJETO VERBOPP','oracion',3,'p_oracionin','parser.py',31),
  ('oracion -> SUJETO','oracion',1,'p_oracion1','parser.py',38),
  ('oracion -> PRONOMBRES','oracion',1,'p_oracion1','parser.py',39),
  ('oracion -> SUSTANTIVOS','oracion',1,'p_oracion1','parser.py',40),
  ('oracion -> VERBOPP','oracion',1,'p_oracion1','parser.py',41),
  ('oracion -> VERBOTP','oracion',1,'p_oracion1','parser.py',42),
  ('oracion -> ADJETIVO','oracion',1,'p_oracion1','parser.py',43),
  ('oracion -> ADVERBIOS','oracion',1,'p_oracion1','parser.py',44),
  ('oracion -> PREPOSICIONES','oracion',1,'p_oracion1','parser.py',45),
  ('oracion -> ARTICULOS','oracion',1,'p_oracion1','parser.py',46),
  ('oracion -> DEMOSTRATIVOS','oracion',1,'p_oracion1','parser.py',47),
  ('oracion -> POSESIVOS','oracion',1,'p_oracion1','parser.py',48),
  ('oracion -> SUJETO VERBOPP','oracion',2,'p_oracion2','parser.py',59),
  ('oracion -> SUJETO VERBOTP','oracion',2,'p_oracion2','parser.py',60),
  ('oracion -> SUJETO VERBOPP ADJETIVO','oracion',3,'p_oracion3','parser.py',72),
  ('oracion -> SUJETO VERBOTP ADJETIVO','oracion',3,'p_oracion3','parser.py',73),
  ('oracion -> SUJETO VERBOTP SUSTANTIVOS','oracion',3,'p_oracion3','parser.py',74),
  ('oracion -> SUJETO VERBOPP SUSTANTIVOS SUSTANTIVOS','oracion',4,'p_oracion4','parser.py',87),
  ('oracion -> SUJETO VERBOTP SUSTANTIVOS SUSTANTIVOS','oracion',4,'p_oracion4','parser.py',88),
  ('oracion -> SUSTANTIVOS SUJETO VERBOPP SUSTANTIVOS','oracion',4,'p_oracion4','parser.py',89),
  ('oracion -> SUSTANTIVOS SUJETO VERBOTP SUSTANTIVOS','oracion',4,'p_oracion4','parser.py',90),
  ('oracion -> SUJETO VERBOPP PREPOSICIONES SUSTANTIVOS','oracion',4,'p_oracion4','parser.py',91),
  ('oracion -> SUJETO VERBOTP PREPOSICIONES SUSTANTIVOS','oracion',4,'p_oracion4','parser.py',92),
  ('oracion -> SUJETO VERBOPP ADVERBIOS SUSTANTIVOS','oracion',4,'p_oracion4','parser.py',93),
  ('oracion -> SUJETO VERBOTP ADVERBIOS SUSTANTIVOS','oracion',4,'p_oracion4','parser.py',94),
  ('oracion -> SUJETO VERBOPP PREPOSICIONES PRONOMBRES','oracion',4,'p_oracion4','parser.py',95),
  ('oracion -> SUJETO VERBOTP PREPOSICIONES PRONOMBRES','oracion',4,'p_oracion4','parser.py',96),
  ('oracion -> SUJETO VERBOPP ARTICULOS SUSTANTIVOS','oracion',4,'p_oracion4','parser.py',97),
  ('oracion -> SUJETO VERBOTP ARTICULOS SUSTANTIVOS','oracion',4,'p_oracion4','parser.py',98),
]
