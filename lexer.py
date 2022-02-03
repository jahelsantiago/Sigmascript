import ply.lex as lex
import ply.yacc as yacc
import numpy as np
import sys



reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'sin' : 'SIN',
    'cos' : 'COS',
    'tan' : 'TAN',
    'sqrt' : 'SQRT',
    'log' : 'LOG',
    'exp' : 'EXP',
    'pi' : 'PI',
    'e' : 'E',
    'arcsin' : 'ARCSIN',
    'arccos' : 'ARCCOS',
    'arctan' : 'ARCTAN',
    'abs' : 'ABS',
    'floor' : 'FLOOR',
    'round' : 'ROUND',
    'ceil' : 'CEIL',
    'env' : 'ENV',
    'print' : 'PRINT',
    'and' : 'AND',
    'or' : 'OR',
 }

# Create a list to hold all of the token names
tokens = [
    'INT',
    'FLOAT',
    'NAME',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'POWER',
    'GTE',
    'LTE',
    'GT',
    'LT',
    'NE',
    'EQ',
    'NOT', 
]


tokens = tokens + list(reserved.values())



# Use regular expressions to define what each token is
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_POWER = r'\^'
t_EQUALS = r'\='
t_GTE = r'>='
t_LTE = r'<='
t_GT = r'>'
t_LT = r'<'
t_NE = r'!='
t_EQ = r'=='


t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r'\,'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ply's special t_ignore variable allows us to define characters the lexer will ignore.
# We're ignoring spaces.
t_ignore = r' '

# More complicated tokens, such as tokens that are more than 1 character in length
# are defined using functions.
# A float is 1 or more numbers followed by a dot (.) followed by 1 or more numbers again.
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# An int is 1 or more numbers.
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# A NAME is a variable name. A variable can be 1 or more characters in length.
# The first character must be in the ranges a-z A-Z or be an underscore.
# Any character following the first character can be a-z A-Z 0-9 or an underscore.
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    else:
        t.type = 'NAME'
    return t


# Skip the current token and output 'Illegal characters' using the special Ply t_error function.
def t_error(t):
    print("Illegal character '%s' " % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()