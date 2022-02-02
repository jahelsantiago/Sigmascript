
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYDIVIDEABS ARCCOS ARCSIN ARCTAN CEIL COS DIVIDE E ELSE EQUALS EXP FLOAT FLOOR IF INT LBRACE LBRACKET LOG LPAREN MINUS MULTIPLY NAME PI PLUS POWER RBRACE RBRACKET ROUND RPAREN SIN SQRT TAN THEN WHILE\n    calc : expression\n         | var_assign\n         | empty\n    \n    var_assign : NAME EQUALS expression\n    \n    expression : SIN LPAREN expression RPAREN\n                | COS LPAREN expression RPAREN\n                | TAN LPAREN expression RPAREN\n                | SQRT LPAREN expression RPAREN\n                | ARCSIN LPAREN expression RPAREN\n                | ARCCOS LPAREN expression RPAREN\n                | ARCTAN LPAREN expression RPAREN\n                | ABS LPAREN expression RPAREN\n                | FLOOR LPAREN expression RPAREN\n                | ROUND LPAREN expression RPAREN\n                | CEIL LPAREN expression RPAREN\n\n    \n    expression : expression MULTIPLY expression\n               | expression DIVIDE expression\n               | expression PLUS expression\n               | expression MINUS expression\n    \n    expression : INT\n               | FLOAT\n    \n    expression : NAME\n    \n    empty :\n    '
    
_lr_action_items = {'SIN':([0,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'COS':([0,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'TAN':([0,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'SQRT':([0,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'ARCSIN':([0,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'ARCCOS':([0,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'ARCTAN':([0,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'ABS':([0,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'FLOOR':([0,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'ROUND':([0,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'CEIL':([0,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'INT':([0,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'FLOAT':([0,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'NAME':([0,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[18,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'$end':([0,1,2,3,4,16,17,18,35,36,37,38,39,51,52,53,54,55,56,57,58,59,60,61,62,],[-23,0,-1,-2,-3,-20,-21,-22,-16,-22,-17,-18,-19,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'MULTIPLY':([2,16,17,18,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,],[19,-20,-21,-22,-16,-22,-17,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'DIVIDE':([2,16,17,18,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,],[20,-20,-21,-22,-16,-22,-17,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'PLUS':([2,16,17,18,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,],[21,-20,-21,-22,-16,-22,-17,-18,-19,21,21,21,21,21,21,21,21,21,21,21,21,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'MINUS':([2,16,17,18,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,],[22,-20,-21,-22,-16,-22,-17,-18,-19,22,22,22,22,22,22,22,22,22,22,22,22,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'LPAREN':([5,6,7,8,9,10,11,12,13,14,15,],[23,24,25,26,27,28,29,30,31,32,33,]),'RPAREN':([16,17,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,61,62,],[-20,-21,-16,-22,-17,-18,-19,52,53,54,55,56,57,58,59,60,61,62,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'EQUALS':([18,],[34,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'calc':([0,],[1,]),'expression':([0,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[2,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,]),'var_assign':([0,],[3,]),'empty':([0,],[4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> calc","S'",1,None,None,None),
  ('calc -> expression','calc',1,'p_calc','calc.py',117),
  ('calc -> var_assign','calc',1,'p_calc','calc.py',118),
  ('calc -> empty','calc',1,'p_calc','calc.py',119),
  ('var_assign -> NAME EQUALS expression','var_assign',3,'p_var_assign','calc.py',125),
  ('expression -> SIN LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',132),
  ('expression -> COS LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',133),
  ('expression -> TAN LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',134),
  ('expression -> SQRT LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',135),
  ('expression -> ARCSIN LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',136),
  ('expression -> ARCCOS LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',137),
  ('expression -> ARCTAN LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',138),
  ('expression -> ABS LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',139),
  ('expression -> FLOOR LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',140),
  ('expression -> ROUND LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',141),
  ('expression -> CEIL LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',142),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression','calc.py',153),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','calc.py',154),
  ('expression -> expression PLUS expression','expression',3,'p_expression','calc.py',155),
  ('expression -> expression MINUS expression','expression',3,'p_expression','calc.py',156),
  ('expression -> INT','expression',1,'p_expression_int_float','calc.py',163),
  ('expression -> FLOAT','expression',1,'p_expression_int_float','calc.py',164),
  ('expression -> NAME','expression',1,'p_expression_var','calc.py',170),
  ('empty -> <empty>','empty',0,'p_empty','calc.py',181),
]
