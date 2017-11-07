import ply.lex as lex
import re
import codecs
import os
import sys

# Lista de tokens
tokens = ['PLUS','MINUS','TIMES','DIVIDE',
          'LT','LEQ','GT','GEQ','EQ','NEQ',
          'LPARENT','RPARENT', 'LBRACKET','RBRACKET','LBRACE','RBRACE',
            'SCOMMENT', 'BEGINCOMMENT','ENDCOMMENT', 'MCOMMENT',
          'POWOP1', 'POWOP2',
           'SEMICOLON', 'COMMA' ,'ID','ASSIGN', 'NUMBER'

          ]

# Diccionario de palabras reservadas
reservadas = {
    'else':'ELSE',
    'if':'IF',
    'int':'INT',
    'void':'VOID',
    'return':'RETURN',
    'while':'WHILE'
}

tokens = tokens+list(reservadas.values())

def t_ELSE(t) :
    r'(?i)else'
    return t
def t_IF(t) :
    r'(?i)if'
    return t
def t_INT(t) :
    r'(?i)int'
    return t
def t_RETURN(t) :
    r'(?i)return'
    return t
def t_WHILE(t) :
    r'(?i)while'
    return t

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t|\n'

# Definición de tokens
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'

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
t_LBRACE = r'\{'
t_RBRACE = r'\}'

t_POWOP1 = r'\^'
t_POWOP2 = r'\*\*'

t_SCOMMENT = r'(\?|!).*\n'
t_MCOMMENT = r'<\/([^\/]|\n)*\/>'

# t_BEGINCOMMENT = r'\<\/'
# t_ENDCOMMENT = r'\/\>'

t_SEMICOLON = r';'
t_COMMA = r','
t_ASSIGN = r'='


# r'(?i)[a-zA-Z](_?[a-zA-Z]+)*_?[a-z0-9]+'
# r'([a-zA-Z](_?[a-zA-Z]+)*_?[a-z0-9]+)|[a-z]'

def t_ID(t):
    r'[a-zA-Z](_?[a-zA-Z]+)*_?[a-z0-9]+|[a-z]'
    # if t.value.lower() in reservadas:
    #     t.value = t.value.lower()
    #     t.type = t.value.upper()
    #     return t
    return t


# Reconocimiento de números
def t_NUMBER(t):
    r'(0[0-9])|[1-9]+[0-9]+'
    t.value = int(t.value)
    return t


# Identifica caracteres ilegales
def t_error(t):
    # if t.value.lower() in reservadas:
    #     t.value = t.value.lower()
    #     t.type = t.value.upper()
    #     return t
    # else:
    print("Caracter ilegal: '%s'" % t.value[0])
    t.lexer.skip(1)

# Busca archivos de prueba en el directorio del proyecto
# def buscarArchivos(path):
#     archivos = []
#     fileNum = ''
#     answer = False
#     counter = 1
#
#     for base, dirs, files in os.walk(path):
#         archivos.append(files)
#
#     for file in files:
#         print(str(counter) + ". " + file)
#         counter = counter+1
#
#     while answer == False:
#         fileNum = input('\nDigite el número  del archivo de prueba que desea analizar')
#         for file in files:
#             if file == files[int(fileNum)-1]:
#                 answer = True
#                 break
#
#     print("Ha escogido \"%s\" \n" %files[int(fileNum)-1])
#
#     return files[int(fileNum)-1]
#
# path = os.path.dirname(__file__) + '/tests/'
# file = buscarArchivos(path)
# test = path + file
# fp = codecs.open(test,"r","utf-8")
# message = fp.read()
# fp.close()

# analyzer = lex.lex()
# analyzer.input(message)

# while True:
#     tok = analyzer.token()
#     if not tok: break
#     print(tok)
