
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORANDleftGTELTEGTLTNEEQleftPLUSMINUSleftMULTIPLYDIVIDEleftPOWERABS AND ARCCOS ARCSIN ARCTAN CALL CEIL COMMA COS DIVIDE DOT E ELSE ENV EQ EQUALS EXP FALSE FLOAT FLOOR FUNCTION GT GTE IF INT LBRACE LBRACKET LEN LOG LPAREN LT LTE MINUS MODEL MULTIPLY NAME NE NOT NOT OR PI PLUS POWER PRINT RBRACE RBRACKET ROUND RPAREN SEMICOLON SIN SQRT TAN THEN TRUE WHILE\n    code : if_expression\n            | block\n    \n    while_statement : WHILE LPAREN expression RPAREN LBRACE block RBRACE\n    \n    if_expression : IF LPAREN expression RPAREN LBRACE block RBRACE\n    | IF LPAREN expression RPAREN LBRACE block RBRACE ELSE LBRACE block RBRACE\n    \n    function_declaration : FUNCTION  NAME LPAREN function_parameters RPAREN LBRACE block RBRACE\n    \n    function_call : CALL NAME LPAREN function_parameters RPAREN\n    \n    function_parameters : NAME\n                        | NAME COMMA function_parameters\n    \n    expression : NAME LBRACKET expression RBRACKET\n    \n    block :  line block\n            | line\n    \n    line : expression SEMICOLON\n         | var_assign SEMICOLON\n         | function_print SEMICOLON\n         | if_expression SEMICOLON\n         | while_statement SEMICOLON \n         | function_declaration SEMICOLON\n         | function_call SEMICOLON \n         | model SEMICOLON\n    \n    function_print : PRINT LPAREN expression RPAREN\n    \n    expression : LBRACKET array_elements RBRACKET\n    \n    array_elements : array_elements COMMA expression\n                   | expression\n    \n    model : MODEL LPAREN NAME COMMA NAME COMMA NAME COMMA NAME RPAREN\n    \n    expression : LEN LPAREN expression RPAREN\n    \n    var_assign : NAME EQUALS expression\n                 | NAME EQUALS model\n    \n    expression : NAME DOT NAME LPAREN model_parameters RPAREN\n    \n    model_parameters : string\n                     | string COMMA model_parameters\n    \n    string : NAME \n           | DOT \n           | INT\n           | empty\n\n    \n    expression : SIN LPAREN expression RPAREN\n                | COS LPAREN expression RPAREN\n                | TAN LPAREN expression RPAREN\n                | SQRT LPAREN expression RPAREN\n                | ARCSIN LPAREN expression RPAREN\n                | ARCCOS LPAREN expression RPAREN\n                | ARCTAN LPAREN expression RPAREN\n                | ABS LPAREN expression RPAREN\n                | FLOOR LPAREN expression RPAREN\n                | ROUND LPAREN expression RPAREN\n                | CEIL LPAREN expression RPAREN\n\n    \n    expression : expression MULTIPLY expression\n                | expression DIVIDE expression\n                | expression PLUS expression\n                | expression MINUS expression\n                | expression POWER expression\n                | expression GTE expression\n                | expression LTE expression\n                | expression GT expression\n                | expression LT expression\n                | expression EQ expression\n                | expression NE expression\n                | expression AND expression\n                | expression OR expression\n    \n    expression : INT\n               | FLOAT\n    \n    expression : TRUE\n               | FALSE\n    \n    expression : NAME\n    \n    empty :\n    '
    
_lr_action_items = {'IF':([0,6,36,38,54,55,56,57,58,59,142,149,159,169,],[4,4,-16,-13,-14,-15,-17,-18,-19,-20,4,4,4,4,]),'NAME':([0,6,14,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,102,117,118,122,141,142,149,150,156,159,160,168,169,],[13,13,65,80,81,-16,65,-13,65,65,65,65,65,65,65,65,65,65,65,65,65,-14,-15,-17,-18,-19,-20,65,98,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,119,65,138,138,143,153,13,13,138,143,13,165,170,13,]),'LBRACKET':([0,6,13,14,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,62,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,142,149,159,169,],[14,14,60,14,-16,14,-13,14,14,14,14,14,14,14,14,14,14,14,14,14,-14,-15,-17,-18,-19,-20,14,14,60,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'LEN':([0,6,14,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,142,149,159,169,],[15,15,15,-16,15,-13,15,15,15,15,15,15,15,15,15,15,15,15,15,-14,-15,-17,-18,-19,-20,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'SIN':([0,6,14,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,142,149,159,169,],[16,16,16,-16,16,-13,16,16,16,16,16,16,16,16,16,16,16,16,16,-14,-15,-17,-18,-19,-20,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'COS':([0,6,14,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,142,149,159,169,],[17,17,17,-16,17,-13,17,17,17,17,17,17,17,17,17,17,17,17,17,-14,-15,-17,-18,-19,-20,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'TAN':([0,6,14,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,142,149,159,169,],[18,18,18,-16,18,-13,18,18,18,18,18,18,18,18,18,18,18,18,18,-14,-15,-17,-18,-19,-20,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'SQRT':([0,6,14,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,142,149,159,169,],[19,19,19,-16,19,-13,19,19,19,19,19,19,19,19,19,19,19,19,19,-14,-15,-17,-18,-19,-20,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'ARCSIN':([0,6,14,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,142,149,159,169,],[20,20,20,-16,20,-13,20,20,20,20,20,20,20,20,20,20,20,20,20,-14,-15,-17,-18,-19,-20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'ARCCOS':([0,6,14,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,142,149,159,169,],[21,21,21,-16,21,-13,21,21,21,21,21,21,21,21,21,21,21,21,21,-14,-15,-17,-18,-19,-20,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'ARCTAN':([0,6,14,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,142,149,159,169,],[22,22,22,-16,22,-13,22,22,22,22,22,22,22,22,22,22,22,22,22,-14,-15,-17,-18,-19,-20,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'ABS':([0,6,14,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,142,149,159,169,],[23,23,23,-16,23,-13,23,23,23,23,23,23,23,23,23,23,23,23,23,-14,-15,-17,-18,-19,-20,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'FLOOR':([0,6,14,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,142,149,159,169,],[24,24,24,-16,24,-13,24,24,24,24,24,24,24,24,24,24,24,24,24,-14,-15,-17,-18,-19,-20,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'ROUND':([0,6,14,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,142,149,159,169,],[25,25,25,-16,25,-13,25,25,25,25,25,25,25,25,25,25,25,25,25,-14,-15,-17,-18,-19,-20,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'CEIL':([0,6,14,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,142,149,159,169,],[26,26,26,-16,26,-13,26,26,26,26,26,26,26,26,26,26,26,26,26,-14,-15,-17,-18,-19,-20,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'INT':([0,6,14,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,122,142,149,156,159,169,],[27,27,27,-16,27,-13,27,27,27,27,27,27,27,27,27,27,27,27,27,-14,-15,-17,-18,-19,-20,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,147,27,27,147,27,27,]),'FLOAT':([0,6,14,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,142,149,159,169,],[28,28,28,-16,28,-13,28,28,28,28,28,28,28,28,28,28,28,28,28,-14,-15,-17,-18,-19,-20,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'TRUE':([0,6,14,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,142,149,159,169,],[29,29,29,-16,29,-13,29,29,29,29,29,29,29,29,29,29,29,29,29,-14,-15,-17,-18,-19,-20,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'FALSE':([0,6,14,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,58,59,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,142,149,159,169,],[30,30,30,-16,30,-13,30,30,30,30,30,30,30,30,30,30,30,30,30,-14,-15,-17,-18,-19,-20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'PRINT':([0,6,36,38,54,55,56,57,58,59,142,149,159,169,],[31,31,-16,-13,-14,-15,-17,-18,-19,-20,31,31,31,31,]),'WHILE':([0,6,36,38,54,55,56,57,58,59,142,149,159,169,],[32,32,-16,-13,-14,-15,-17,-18,-19,-20,32,32,32,32,]),'FUNCTION':([0,6,36,38,54,55,56,57,58,59,142,149,159,169,],[33,33,-16,-13,-14,-15,-17,-18,-19,-20,33,33,33,33,]),'CALL':([0,6,36,38,54,55,56,57,58,59,142,149,159,169,],[34,34,-16,-13,-14,-15,-17,-18,-19,-20,34,34,34,34,]),'MODEL':([0,6,36,38,54,55,56,57,58,59,62,142,149,159,169,],[35,35,-16,-13,-14,-15,-17,-18,-19,-20,35,35,35,35,35,]),'$end':([1,2,3,6,36,38,52,54,55,56,57,58,59,161,173,],[0,-1,-2,-12,-16,-13,-11,-14,-15,-17,-18,-19,-20,-4,-5,]),'SEMICOLON':([2,5,7,8,9,10,11,12,13,27,28,29,30,53,65,84,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,121,124,125,126,127,128,129,130,131,132,133,134,135,136,152,155,161,163,167,172,173,],[36,38,54,55,56,57,58,59,-64,-60,-61,-62,-63,36,-64,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-27,-28,-22,-10,-26,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-21,-7,-29,-4,-3,-6,-25,-5,]),'LPAREN':([4,15,16,17,18,19,20,21,22,23,24,25,26,31,32,35,80,81,98,],[37,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,117,118,122,]),'MULTIPLY':([5,13,27,28,29,30,64,65,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,121,123,124,125,126,127,128,129,130,131,132,133,134,135,155,],[39,-64,-60,-61,-62,-63,39,-64,39,-47,-48,39,39,-51,39,39,39,39,39,39,39,39,39,39,-22,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-10,39,-26,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-29,]),'DIVIDE':([5,13,27,28,29,30,64,65,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,121,123,124,125,126,127,128,129,130,131,132,133,134,135,155,],[40,-64,-60,-61,-62,-63,40,-64,40,-47,-48,40,40,-51,40,40,40,40,40,40,40,40,40,40,-22,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-10,40,-26,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-29,]),'PLUS':([5,13,27,28,29,30,64,65,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,121,123,124,125,126,127,128,129,130,131,132,133,134,135,155,],[41,-64,-60,-61,-62,-63,41,-64,41,-47,-48,-49,-50,-51,41,41,41,41,41,41,41,41,41,41,-22,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-10,41,-26,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-29,]),'MINUS':([5,13,27,28,29,30,64,65,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,121,123,124,125,126,127,128,129,130,131,132,133,134,135,155,],[42,-64,-60,-61,-62,-63,42,-64,42,-47,-48,-49,-50,-51,42,42,42,42,42,42,42,42,42,42,-22,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-10,42,-26,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-29,]),'POWER':([5,13,27,28,29,30,64,65,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,121,123,124,125,126,127,128,129,130,131,132,133,134,135,155,],[43,-64,-60,-61,-62,-63,43,-64,43,43,43,43,43,-51,43,43,43,43,43,43,43,43,43,43,-22,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-10,43,-26,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-29,]),'GTE':([5,13,27,28,29,30,64,65,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,121,123,124,125,126,127,128,129,130,131,132,133,134,135,155,],[44,-64,-60,-61,-62,-63,44,-64,44,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,44,44,44,44,-22,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-10,44,-26,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-29,]),'LTE':([5,13,27,28,29,30,64,65,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,121,123,124,125,126,127,128,129,130,131,132,133,134,135,155,],[45,-64,-60,-61,-62,-63,45,-64,45,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,45,45,45,45,-22,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-10,45,-26,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-29,]),'GT':([5,13,27,28,29,30,64,65,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,121,123,124,125,126,127,128,129,130,131,132,133,134,135,155,],[46,-64,-60,-61,-62,-63,46,-64,46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,46,46,46,46,-22,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-10,46,-26,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-29,]),'LT':([5,13,27,28,29,30,64,65,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,121,123,124,125,126,127,128,129,130,131,132,133,134,135,155,],[47,-64,-60,-61,-62,-63,47,-64,47,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,47,47,47,47,-22,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-10,47,-26,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-29,]),'EQ':([5,13,27,28,29,30,64,65,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,121,123,124,125,126,127,128,129,130,131,132,133,134,135,155,],[48,-64,-60,-61,-62,-63,48,-64,48,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,48,48,48,48,-22,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-10,48,-26,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-29,]),'NE':([5,13,27,28,29,30,64,65,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,121,123,124,125,126,127,128,129,130,131,132,133,134,135,155,],[49,-64,-60,-61,-62,-63,49,-64,49,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,49,49,49,49,-22,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-10,49,-26,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-29,]),'AND':([5,13,27,28,29,30,64,65,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,121,123,124,125,126,127,128,129,130,131,132,133,134,135,155,],[50,-64,-60,-61,-62,-63,50,-64,50,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,50,50,-22,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-10,50,-26,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-29,]),'OR':([5,13,27,28,29,30,64,65,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,121,123,124,125,126,127,128,129,130,131,132,133,134,135,155,],[51,-64,-60,-61,-62,-63,51,-64,51,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,51,51,-22,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-10,51,-26,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-29,]),'RBRACE':([6,36,38,52,54,55,56,57,58,59,154,157,164,171,],[-12,-16,-13,-11,-14,-15,-17,-18,-19,-20,161,163,167,173,]),'DOT':([13,65,122,156,],[61,61,144,144,]),'EQUALS':([13,],[62,]),'RBRACKET':([27,28,29,30,63,64,65,84,85,86,87,88,89,90,91,92,93,94,95,96,97,101,121,123,124,125,126,127,128,129,130,131,132,133,134,135,155,],[-60,-61,-62,-63,101,-24,-64,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,121,-22,-10,-23,-26,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-29,]),'COMMA':([27,28,29,30,63,64,65,84,85,86,87,88,89,90,91,92,93,94,95,96,101,119,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,138,143,144,146,147,148,153,155,156,165,],[-60,-61,-62,-63,102,-24,-64,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-22,141,-10,-65,-23,-26,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,150,-32,-33,156,-34,-35,160,-29,-65,168,]),'RPAREN':([27,28,29,30,65,83,84,85,86,87,88,89,90,91,92,93,94,95,96,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,121,122,124,125,126,127,128,129,130,131,132,133,134,135,138,139,140,143,144,145,146,147,148,155,156,158,162,170,],[-60,-61,-62,-63,-64,120,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-22,124,125,126,127,128,129,130,131,132,133,134,135,136,137,-10,-65,-26,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-8,151,152,-32,-33,155,-30,-34,-35,-29,-65,-9,-31,172,]),'LBRACE':([120,137,151,166,],[142,149,159,169,]),'ELSE':([161,],[166,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'code':([0,],[1,]),'if_expression':([0,6,142,149,159,169,],[2,53,53,53,53,53,]),'block':([0,6,142,149,159,169,],[3,52,154,157,164,171,]),'expression':([0,6,14,37,39,40,41,42,43,44,45,46,47,48,49,50,51,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,142,149,159,169,],[5,5,64,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,103,104,105,106,107,108,109,110,111,112,113,114,115,116,123,5,5,5,5,]),'line':([0,6,142,149,159,169,],[6,6,6,6,6,6,]),'var_assign':([0,6,142,149,159,169,],[7,7,7,7,7,7,]),'function_print':([0,6,142,149,159,169,],[8,8,8,8,8,8,]),'while_statement':([0,6,142,149,159,169,],[9,9,9,9,9,9,]),'function_declaration':([0,6,142,149,159,169,],[10,10,10,10,10,10,]),'function_call':([0,6,142,149,159,169,],[11,11,11,11,11,11,]),'model':([0,6,62,142,149,159,169,],[12,12,100,12,12,12,12,]),'array_elements':([14,],[63,]),'function_parameters':([117,118,150,],[139,140,158,]),'model_parameters':([122,156,],[145,162,]),'string':([122,156,],[146,146,]),'empty':([122,156,],[148,148,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> code","S'",1,None,None,None),
  ('code -> if_expression','code',1,'p_code','calc.py',158),
  ('code -> block','code',1,'p_code','calc.py',159),
  ('while_statement -> WHILE LPAREN expression RPAREN LBRACE block RBRACE','while_statement',7,'p_while_statement','calc.py',166),
  ('if_expression -> IF LPAREN expression RPAREN LBRACE block RBRACE','if_expression',7,'p_if_statement','calc.py',172),
  ('if_expression -> IF LPAREN expression RPAREN LBRACE block RBRACE ELSE LBRACE block RBRACE','if_expression',11,'p_if_statement','calc.py',173),
  ('function_declaration -> FUNCTION NAME LPAREN function_parameters RPAREN LBRACE block RBRACE','function_declaration',8,'p_function_declaration','calc.py',182),
  ('function_call -> CALL NAME LPAREN function_parameters RPAREN','function_call',5,'p_function_call','calc.py',188),
  ('function_parameters -> NAME','function_parameters',1,'p_function_parameters','calc.py',196),
  ('function_parameters -> NAME COMMA function_parameters','function_parameters',3,'p_function_parameters','calc.py',197),
  ('expression -> NAME LBRACKET expression RBRACKET','expression',4,'p_array_get','calc.py',206),
  ('block -> line block','block',2,'p_block','calc.py',212),
  ('block -> line','block',1,'p_block','calc.py',213),
  ('line -> expression SEMICOLON','line',2,'p_line','calc.py',223),
  ('line -> var_assign SEMICOLON','line',2,'p_line','calc.py',224),
  ('line -> function_print SEMICOLON','line',2,'p_line','calc.py',225),
  ('line -> if_expression SEMICOLON','line',2,'p_line','calc.py',226),
  ('line -> while_statement SEMICOLON','line',2,'p_line','calc.py',227),
  ('line -> function_declaration SEMICOLON','line',2,'p_line','calc.py',228),
  ('line -> function_call SEMICOLON','line',2,'p_line','calc.py',229),
  ('line -> model SEMICOLON','line',2,'p_line','calc.py',230),
  ('function_print -> PRINT LPAREN expression RPAREN','function_print',4,'p_function_print','calc.py',236),
  ('expression -> LBRACKET array_elements RBRACKET','expression',3,'p_array','calc.py',242),
  ('array_elements -> array_elements COMMA expression','array_elements',3,'p_array_elements','calc.py',250),
  ('array_elements -> expression','array_elements',1,'p_array_elements','calc.py',251),
  ('model -> MODEL LPAREN NAME COMMA NAME COMMA NAME COMMA NAME RPAREN','model',10,'p_declare_mode','calc.py',261),
  ('expression -> LEN LPAREN expression RPAREN','expression',4,'p_len','calc.py',267),
  ('var_assign -> NAME EQUALS expression','var_assign',3,'p_var_assign','calc.py',273),
  ('var_assign -> NAME EQUALS model','var_assign',3,'p_var_assign','calc.py',274),
  ('expression -> NAME DOT NAME LPAREN model_parameters RPAREN','expression',6,'p_model_operations','calc.py',281),
  ('model_parameters -> string','model_parameters',1,'p_model_parameters','calc.py',290),
  ('model_parameters -> string COMMA model_parameters','model_parameters',3,'p_model_parameters','calc.py',291),
  ('string -> NAME','string',1,'p_string','calc.py',300),
  ('string -> DOT','string',1,'p_string','calc.py',301),
  ('string -> INT','string',1,'p_string','calc.py',302),
  ('string -> empty','string',1,'p_string','calc.py',303),
  ('expression -> SIN LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',311),
  ('expression -> COS LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',312),
  ('expression -> TAN LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',313),
  ('expression -> SQRT LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',314),
  ('expression -> ARCSIN LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',315),
  ('expression -> ARCCOS LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',316),
  ('expression -> ARCTAN LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',317),
  ('expression -> ABS LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',318),
  ('expression -> FLOOR LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',319),
  ('expression -> ROUND LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',320),
  ('expression -> CEIL LPAREN expression RPAREN','expression',4,'p_expression_function','calc.py',321),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression','calc.py',331),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','calc.py',332),
  ('expression -> expression PLUS expression','expression',3,'p_expression','calc.py',333),
  ('expression -> expression MINUS expression','expression',3,'p_expression','calc.py',334),
  ('expression -> expression POWER expression','expression',3,'p_expression','calc.py',335),
  ('expression -> expression GTE expression','expression',3,'p_expression','calc.py',336),
  ('expression -> expression LTE expression','expression',3,'p_expression','calc.py',337),
  ('expression -> expression GT expression','expression',3,'p_expression','calc.py',338),
  ('expression -> expression LT expression','expression',3,'p_expression','calc.py',339),
  ('expression -> expression EQ expression','expression',3,'p_expression','calc.py',340),
  ('expression -> expression NE expression','expression',3,'p_expression','calc.py',341),
  ('expression -> expression AND expression','expression',3,'p_expression','calc.py',342),
  ('expression -> expression OR expression','expression',3,'p_expression','calc.py',343),
  ('expression -> INT','expression',1,'p_expression_int_float','calc.py',351),
  ('expression -> FLOAT','expression',1,'p_expression_int_float','calc.py',352),
  ('expression -> TRUE','expression',1,'p_expression_bool','calc.py',358),
  ('expression -> FALSE','expression',1,'p_expression_bool','calc.py',359),
  ('expression -> NAME','expression',1,'p_expression_var','calc.py',368),
  ('empty -> <empty>','empty',0,'p_empty','calc.py',379),
]
