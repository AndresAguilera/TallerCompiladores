import ply.lex as lex
import re
import codecs
import os
import sys

tokens = ['PLUS','MINUS','TIMES','DIVIDE','EXP','EXPD',
          'LT','LEQ','GT','GEQ','EQ','NEQ',
          'LPARENT','RPARENT', 'LBRACKET','RBRACKET','LKEY','RKEY',
            'SCOMMENT', 'BEGINCOMMENT','ENDCOMMENT',
           'SEMICOLON', 'COMMA' ,'ID','ASSIGN', 'NUMBER'

          ]
reservadas = {
    'else':'ELSE',
    'if':'IF',
    'int':'INT',
    'void':'VOID',
    'return':'RETURN',
    'while':'WHILE',
    'for':'FOR'
}

tokens = tokens+list(reservadas.values())


t_ignore = ' \t'

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_EXP = r'\^'
# t_EXPP = r'\\**'

t_LT = r'<'
t_LEQ = r'<='
t_GT = r'>'
t_GEQ = r'>='
t_EQ = r'=='
t_NEQ = r'<>'

t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LKEY = r'/{'
t_RKEY = r'/}'


t_SCOMMENT = r'\%'
# t_BEGINCOMMENT = r'\/#'
# t_ENDCOMMENT = r'\#/'

t_SEMICOLON = r';'
t_COMMA = r','
t_ASSIGN = r'::=='

# t_ID = r'[a-z][a-zA-Z0-9]*[_]?[a-zA-Z0-9]'
# def t_ID(t):
#     r'[a-z][a-zA-Z0-9]*[_]?[a-zA-Z0-9]'
#     if t.value.upper() in reservadas:
#         t.value = t.value.upper()
#         t.type = t.value
#
#         return t



t_NUMBER = r'[0-9]|([1-9]+)'
# def t_NUMBER(t):
#     r'/d+'
#     t.value = int(t.value)
#     return t



def t_error(t):
    print("Caracter ilegal: '%s'" % t.value[0])
    t.lexer.skip(1)

def t_VAR(t):
    # r'[a-zA-Z_][\w_]*'
    r'[a-z][a-zA-Z0-9]*[_]?[a-zA-Z0-9]'
    t.type = reservadas.get(t.value,'ID')
    return t

def searchFiles(path):
    archivos = []
    fileNum = ''
    answer = False
    counter = 1

    for base, dirs, files in os.walk(path):
        archivos.append(files)

    for file in files:
        print(str(counter) + ". " + file)
        counter = counter+1

    while answer == False:
        fileNum = input('\nTest Number')
        for file in files:
            if file == files[int(fileNum)-1]:
                answer = True
                break

    print("Has escogido \"%s\" \n" %files[int(fileNum)-1])

    return files[int(fileNum)-1]

path = os.path.dirname(__file__) + '/tests/'
file = searchFiles(path)
test = path + file
fp = codecs.open(test,"r","utf-8")
message = fp.read()
fp.close()

analyzer = lex.lex()

analyzer.input(message)

while True:
    tok = analyzer.token()
    if not tok: break
    print(tok)
