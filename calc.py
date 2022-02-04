from operator import le
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
    'not' : 'NOT',
    'true' : 'TRUE',
    'false' : 'FALSE',
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
    'SEMICOLON',
]


tokens = tokens + list(reserved.values())



# Use regular expressions to define what each token is
t_GTE = r'>='
t_LTE = r'<='
t_GT = r'>'
t_LT = r'<'
t_NE = r'!='
t_EQ = r'=='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_POWER = r'\^'
t_EQUALS = r'\='


t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'

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


# Ensure our parser understands the correct order of operations.
# The precedence variable is a special Ply variable.
precedence = (
    ('left', 'OR', 'AND'),
    ('left', 'GTE', 'LTE', 'GT', 'LT', 'NE', 'EQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('left', 'POWER'),
)
def p_code(p):
    '''
    code : if_expression
            | block
    '''
    for i in p[1][1]:
        run(i)

def p_while_statement(p):
    '''
    while_statement : WHILE LPAREN expression RPAREN LBRACE block RBRACE
    '''
    p[0] = ("while", p[3], p[6])

def p_if_statement(p):
    '''
    if_expression : IF LPAREN expression RPAREN LBRACE block RBRACE
    | IF LPAREN expression RPAREN LBRACE block RBRACE ELSE LBRACE block RBRACE
    '''
    if len(p) == 8:
        p[0] = ('if', p[3], p[6])
    else:
        p[0] = ('if', p[3], p[6], p[10])



def p_block(p):
    '''
    block :  line block
            | line
    '''
    if len(p) == 2:
        p[0] = ("block", [p[1]])
    else:
        p[0] = ("block", [p[1]] + p[2][1])
        

def p_line(p):
    '''
    line : expression SEMICOLON
         | var_assign SEMICOLON
         | function_print SEMICOLON
         | if_expression SEMICOLON
         | while_statement SEMICOLON 
    '''
    p[0] = p[1]

def p_function_print(p):
    '''
    function_print : PRINT LPAREN expression RPAREN
    '''
    p[0] = ('print', p[3])

def p_array(p):
    '''
    expression : LBRACKET array_elements RBRACKET
    '''
    p[0] = np.array(p[2], dtype=np.float64)

def p_array_elements(p):
    '''
    array_elements : array_elements COMMA expression
                   | expression
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]
    

def p_var_assign(p):
    '''
    var_assign : NAME EQUALS expression
    '''
    # Build our tree
    p[0] = ('=', p[1], p[3])



def p_expression_function(p):
    '''
    expression : SIN LPAREN expression RPAREN
                | COS LPAREN expression RPAREN
                | TAN LPAREN expression RPAREN
                | SQRT LPAREN expression RPAREN
                | ARCSIN LPAREN expression RPAREN
                | ARCCOS LPAREN expression RPAREN
                | ARCTAN LPAREN expression RPAREN
                | ABS LPAREN expression RPAREN
                | FLOOR LPAREN expression RPAREN
                | ROUND LPAREN expression RPAREN
                | CEIL LPAREN expression RPAREN

    '''
    p[0] = (p[1], p[3])



# Expressions are recursive.
def p_expression(p):
    '''
    expression : expression MULTIPLY expression
                | expression DIVIDE expression
                | expression PLUS expression
                | expression MINUS expression
                | expression POWER expression
                | expression GTE expression
                | expression LTE expression
                | expression GT expression
                | expression LT expression
                | expression EQ expression
                | expression NE expression
                | expression AND expression
                | expression OR expression
    '''
    # Build our tree.
    p[0] = (p[2], p[1], p[3])


def p_expression_int_float(p):
    '''
    expression : INT
               | FLOAT
    '''
    p[0] = p[1]

def p_expression_bool(p):
    '''
    expression : TRUE
               | FALSE
    '''
    if p[1] == 'true':
        p[0] = True
    else:
        p[0] = False

def p_expression_var(p):
    '''
    expression : NAME
    '''
    p[0] = ('var', p[1])

# Output to the user that there is an error in the input as it doesn't conform to our grammar.
# p_error is another special Ply function.
def p_error(p):
    print("Syntax error found: ", p)

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

# Build the parser
parser = yacc.yacc()
# Create the environment upon which we will store and retreive variables from.
env = {}
# The run function is our recursive function that 'walks' the tree generated by our parser.
def run(p):
    global env
    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == 'sin':
            return np.sin(run(p[1]))
        elif p[0] == 'cos':
            return np.cos(run(p[1]))
        elif p[0] == 'tan':
            return np.tan(run(p[1]))
        elif p[0] == 'sqrt':
            return np.sqrt(run(p[1]))
        elif p[0] == 'arcsin':
            return np.arcsin(run(p[1]))
        elif p[0] == 'arccos':
            return np.arccos(run(p[1]))
        elif p[0] == 'arctan':
            return np.arctan(run(p[1]))
        elif p[0] == 'abs':
            return np.abs(run(p[1]))
        elif p[0] == 'floor':
            return np.floor(run(p[1]))
        elif p[0] == 'round':
            return np.round(run(p[1]))
        elif p[0] == 'ceil':
            return np.ceil(run(p[1]))
        elif p[0] == '^':
            return run(p[1]) ** run(p[2])
        elif p[0] == '>=':
            return run(p[1]) >= run(p[2])
        elif p[0] == '<=':
            return run(p[1]) <= run(p[2])
        elif p[0] == '>':
            return run(p[1]) > run(p[2])
        elif p[0] == '<':
            return run(p[1]) < run(p[2])
        elif p[0] == '==':
            return run(p[1]) == run(p[2])
        elif p[0] == 'and':
            return run(p[1]) and run(p[2])
        elif p[0] == 'or':
            return run(p[1]) or run(p[2])
        elif p[0] == '=':
            env[p[1]] = run(p[2])
        elif p[0] == 'print':
            print(run(p[1]))      
        elif p[0] == 'if':
            if run(p[1]):
                return run(p[2])
            else:
                if len(p) > 3:
                    return run(p[3])
        elif p[0] == 'block':
            for x in p[1]:
                run(x)
        elif p[0] == 'while':
            while run(p[1]):
                run(p[2])
        elif p[0] == 'var':
            if p[1] not in env:
                return 'Undeclared variable found!'
            else:
                return env[p[1]]
    else:
        return p

# Create a REPL to provide a way to interface with our calculator.
tokenize = False
acces_by_file = True


while not acces_by_file:
    try:
        s = input('Sigma>> ')
    except EOFError:
        break
    if not tokenize: 
        parser.parse(s)
    else:
        lexer.input(s)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)

##read a file and parse it
if acces_by_file:
    code = ""
    with open('test.txt') as f:
        for line in f:
            code += line
    code = code.replace('\n', '')
    code = code.replace(' ', '')

    parser.parse(code)


    
