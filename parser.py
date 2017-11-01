import ply.yacc as yacc
import os
import codecs
import re
from scanner import tokens
from sys import stdin

precedence = (
    ('right','ASSIGN'),
    ('right','UPDATE'),
    ('left','NE'),
    ('left','LT','LTE','GT','GTE'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('left','LPARENT','RPARENT'),
)
# 1
def p_program(p):
    '''program : declarationList'''
    print("program")
    # p[0] = program(p[1],"program")
# 2
def p_declarationList1(p):
    '''declarationList : declarationList declaration'''
    print ("declaration-list")
# 2
def p_declarationList2(p):
    '''declarationList : declaration'''
    print ("declaration-list")
# 3
def p_declaration1(p):
    '''declaration : varDeclaration'''
    print ("declaration")

# 3
def p_declaration2(p):
    '''declaration : funDeclaration'''
    print ("declaration")
# 4

def p_varDeclaration1(p):
    '''varDeclaration : typeSpecifier ID ;'''
    print ("varDeclaration")
# 4
def p_varDeclaration2(p):
    '''varDeclaration : typeSpecifier ID [ NUM ] ;'''
    print ("varDeclaration")
# 5
def p_typeSpecifier1(p):
    '''typeSpecifier : int'''
    print ("typeSpecifier")
# 5
def p_typeSpecifier2(p):
    '''typeSpecifier : void'''
    print ("typeSpecifier")

def p_empty(p):
    '''empty : '''
    pass

def p_error(p):
    print("Error de sintaxis",p)
    print("Error en la linea"+str(p.lineno))





def buscarArchivos(path):
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
        fileNum = input('\nDigite el número  del archivo de prueba que desea analizar')
        for file in files:
            if file == files[int(fileNum)-1]:
                answer = True
                break

    print("Ha escogido \"%s\" \n" %files[int(fileNum)-1])

    return files[int(fileNum)-1]

path = os.path.dirname(__file__) + '/tests/'
file = buscarArchivos(path)
test = path + file
fp = codecs.open(test,"r","utf-8")
message = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(message)

print(result)