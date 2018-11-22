
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADJETIVO ADVERBIOS ARTICULOS DEMOSTRATIVOS POSESIVOS PREPOSICIONES PRONOMBRES SUJETO SUSTANTIVOS VERBOS\n    oracion : TEXTO\n    \n      TEXTO : SUJETO\n            | PRONOMBRES\n            | SUSTANTIVOS\n            | VERBOS\n            | ADJETIVO\n            | ADVERBIOS\n            | PREPOSICIONES\n            | ARTICULOS\n            | DEMOSTRATIVOS\n            | POSESIVOS\n    \n    oracion : SUJETO VERBOS\n            | TEXTO TEXTO\n    \n    oracion : SUJETO VERBOS TEXTO\n            | TEXTO TEXTO TEXTO \n    \n    oracion : SUJETO VERBOS TEXTO TEXTO\n            | TEXTO TEXTO TEXTO TEXTO\n    \n    oracion : SUJETO VERBOS TEXTO TEXTO TEXTO\n            | TEXTO TEXTO TEXTO TEXTO TEXTO\n    \n    oracion : SUJETO VERBOS TEXTO TEXTO TEXTO TEXTO\n            | TEXTO TEXTO TEXTO TEXTO TEXTO TEXTO\n    '
    
_lr_action_items = {'SUJETO':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[3,14,-2,-5,-3,-4,-6,-7,-8,-9,-10,-11,14,-2,14,14,14,14,14,14,14,]),'PRONOMBRES':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[5,5,-2,-5,-3,-4,-6,-7,-8,-9,-10,-11,5,-2,5,5,5,5,5,5,5,]),'SUSTANTIVOS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[6,6,-2,-5,-3,-4,-6,-7,-8,-9,-10,-11,6,-2,6,6,6,6,6,6,6,]),'VERBOS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[4,4,15,-5,-3,-4,-6,-7,-8,-9,-10,-11,4,-2,4,4,4,4,4,4,4,]),'ADJETIVO':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[7,7,-2,-5,-3,-4,-6,-7,-8,-9,-10,-11,7,-2,7,7,7,7,7,7,7,]),'ADVERBIOS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[8,8,-2,-5,-3,-4,-6,-7,-8,-9,-10,-11,8,-2,8,8,8,8,8,8,8,]),'PREPOSICIONES':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[9,9,-2,-5,-3,-4,-6,-7,-8,-9,-10,-11,9,-2,9,9,9,9,9,9,9,]),'ARTICULOS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[10,10,-2,-5,-3,-4,-6,-7,-8,-9,-10,-11,10,-2,10,10,10,10,10,10,10,]),'DEMOSTRATIVOS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[11,11,-2,-5,-3,-4,-6,-7,-8,-9,-10,-11,11,-2,11,11,11,11,11,11,11,]),'POSESIVOS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[12,12,-2,-5,-3,-4,-6,-7,-8,-9,-10,-11,12,-2,12,12,12,12,12,12,12,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,],[0,-1,-2,-5,-3,-4,-6,-7,-8,-9,-10,-11,-13,-2,-12,-15,-14,-17,-16,-19,-18,-21,-20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'oracion':([0,],[1,]),'TEXTO':([0,2,13,15,16,17,18,19,20,21,],[2,13,16,17,18,19,20,21,22,23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> oracion","S'",1,None,None,None),
  ('oracion -> TEXTO','oracion',1,'p_oracion1','parser.py',25),
  ('TEXTO -> SUJETO','TEXTO',1,'p_oracion0','parser.py',36),
  ('TEXTO -> PRONOMBRES','TEXTO',1,'p_oracion0','parser.py',37),
  ('TEXTO -> SUSTANTIVOS','TEXTO',1,'p_oracion0','parser.py',38),
  ('TEXTO -> VERBOS','TEXTO',1,'p_oracion0','parser.py',39),
  ('TEXTO -> ADJETIVO','TEXTO',1,'p_oracion0','parser.py',40),
  ('TEXTO -> ADVERBIOS','TEXTO',1,'p_oracion0','parser.py',41),
  ('TEXTO -> PREPOSICIONES','TEXTO',1,'p_oracion0','parser.py',42),
  ('TEXTO -> ARTICULOS','TEXTO',1,'p_oracion0','parser.py',43),
  ('TEXTO -> DEMOSTRATIVOS','TEXTO',1,'p_oracion0','parser.py',44),
  ('TEXTO -> POSESIVOS','TEXTO',1,'p_oracion0','parser.py',45),
  ('oracion -> SUJETO VERBOS','oracion',2,'p_oracion2','parser.py',53),
  ('oracion -> TEXTO TEXTO','oracion',2,'p_oracion2','parser.py',54),
  ('oracion -> SUJETO VERBOS TEXTO','oracion',3,'p_oracion3','parser.py',68),
  ('oracion -> TEXTO TEXTO TEXTO','oracion',3,'p_oracion3','parser.py',69),
  ('oracion -> SUJETO VERBOS TEXTO TEXTO','oracion',4,'p_oracion4','parser.py',83),
  ('oracion -> TEXTO TEXTO TEXTO TEXTO','oracion',4,'p_oracion4','parser.py',84),
  ('oracion -> SUJETO VERBOS TEXTO TEXTO TEXTO','oracion',5,'p_oracion5','parser.py',97),
  ('oracion -> TEXTO TEXTO TEXTO TEXTO TEXTO','oracion',5,'p_oracion5','parser.py',98),
  ('oracion -> SUJETO VERBOS TEXTO TEXTO TEXTO TEXTO','oracion',6,'p_oracion6','parser.py',112),
  ('oracion -> TEXTO TEXTO TEXTO TEXTO TEXTO TEXTO','oracion',6,'p_oracion6','parser.py',113),
]
