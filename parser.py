import ply.yacc as yacc
import os
import codecs
import re
from scanner import *
from sys import stdin
from semantic import *

precedence = (
    ('right','ID','IF','WHILE'),
    ('right','ASSIGN'),
    ('left','LT','LEQ','GT','GEQ'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('left','LPARENT','RPARENT'),
)
# Tokens especiales



# 1
def p_program(p):
    '''program : declarationList'''
    p[0] = program(p[1],"program")
    print("program")
# 2
def p_declarationList1(p):
    '''declarationList : declarationList declaration'''

    p[0] = declarationList1(p[1],p[2],"declarationList1")
    print ("declaration-list")
# 2
def p_declarationList2(p):
    '''declarationList : declaration'''
    p[0] = declarationList2(p[1],"declarationList2")
    # print ("declaration-list")
# 3
def p_declaration1(p):
    '''declaration : varDeclaration'''
    p[0] = declaration1(p[1], "declaration1")
    print ("declaration1")

# 3
def p_declaration2(p):
    '''declaration : funDeclaration'''
    p[0] = declaration2(p[1],"declaration2")
    print ("declaration2")
# 4

def p_varDeclaration1(p):
    '''varDeclaration : typeSpecifier ID SEMICOLON'''
    p[0] = varDeclaration1(p[1],ID(p[2]),SEMICOLON(p[3]),"varDeclaration1")
    print ("varDeclaration1")
# 4
def p_varDeclaration2(p):
    '''varDeclaration : typeSpecifier ID LBRACKET NUMBER RBRACKET SEMICOLON'''
    p[0] = varDeclaration2(p[1], ID(p[2]), LBRACKET(p[3]), "varDeclaration2")
    print ("varDeclaration2")
# 5
def p_typeSpecifier1(p):
    '''typeSpecifier : INT'''
    p[0] = typeSpecifier1(p[1],"typeSpecifier1")
    print ("typeSpecifier1")
# 5
def p_typeSpecifier2(p):
    '''typeSpecifier : VOID'''
    p[0] = typeSpecifier2(p[1],"typeSpecifier2")
    print ("typeSpecifier2")
# 6
def p_funDeclaration(p):
    '''funDeclaration : typeSpecifier ID LPARENT params RPARENT compoundStmt'''
    print ("funDeclaration")

# 7
def p_params1(p):
    '''params : paramList'''
    print ("params1")

# 7
def p_params2(p):
    '''params : VOID'''
    print ("params2")

# 8
def p_paramList1(p):
    '''paramList : paramList COMMA param'''
    print ("param-list1")
# 8
def p_paramList2(p):
    '''paramList : param'''
    print ("param-list2")

# 9
def p_param1(p):
    '''param : typeSpecifier ID'''
    print ("param1")

# 9
def p_param2(p):
    '''param : typeSpecifier ID LBRACKET RBRACKET '''
    print ("param2")

# 10
def p_compoundStmt(p):
    '''compoundStmt : LBRACE localDeclarations statementList RBRACE'''
    print ("compound-stmt")

# 11
def p_localDeclarations1(p):
    '''localDeclarations : localDeclarations varDeclaration'''
    print ("local-declarations1")

# 11
def p_localDeclarations2(p):
    '''localDeclarations : empty'''
    p[0] = Null()
    print ("local-declarations2")

# 12
def p_statementList1(p):
    '''statementList : statementList statement'''
    print ("statement-list1")

# 12
def p_statementList2(p):
    '''statementList : empty'''
    p[0] = Null()
    print("statementList2")

# 13
def p_statement1(p):
    '''statement : expressionStmt'''
    print ("statement1")

# 13
def p_statement2(p):
    '''statement : compoundStmt'''
    print ("statement2")
# 13
def p_statement3(p):
    '''statement : selectionStmt'''
    print ("statement3")
# 13
def p_statement4(p):
    '''statement : iterationStmt'''
    print ("statement1")
# 13
def p_statement5(p):
    '''statement : returnStmt'''
    print ("statement2")

# 14
def p_expressionStmt1(p):
    '''expressionStmt : expression SEMICOLON '''
    print ("expression-stmt1")

# 14
def p_expressionStmt2(p):
    '''expressionStmt :  SEMICOLON '''
    print ("expression-stmt2")

# 15
def p_selectionStmt1(p):
    '''selectionStmt : IF LPARENT expression RPARENT statement'''
    print ("selectionStmt1")
# 15
def p_selectionStmt2(p):
    '''selectionStmt : IF LPARENT expression RPARENT statement ELSE statement'''
    print ("selectionStmt2")

# 16
def p_iterationStmt(p):
    '''iterationStmt : WHILE LPARENT expression RPARENT statement'''
    p[0] = iterationStmt()
    print ("iterationStmt")

# 17
def p_returnStmt1(p):
    '''returnStmt : RETURN SEMICOLON'''
    print ("returnStmt1")

# 17
def p_returnStmt2(p):
    '''returnStmt : RETURN expression SEMICOLON'''
    print ("returnStmt2")

# 18
def p_expression1(p):
    '''expression : var EQ expression'''
    print ("expression1")

# 18
def p_expression2(p):
    '''expression : simpleExpression'''
    print ("expression2")

# 19
def p_var1(p):
    '''var : ID'''
    print ("var1")

# 19
def p_var2(p):
    '''var : ID LBRACKET expression RBRACKET'''
    print ("var2")

# 20
def p_simpleExpression1(p):
    '''simpleExpression : additiveExpression relop additiveExpression'''
    print ("simple-expression1")

# 20
def p_simpleExpression2(p):
    '''simpleExpression : additiveExpression'''
    print ("simple-expression2")

# 21
def p_relop1(p):
    '''relop : LEQ'''
    print ("relop1")

# 21
def p_relop2(p):
    '''relop : LT'''
    print ("relop2")

# 21
def p_relop3(p):
    '''relop : GT'''
    print ("relop3")

# 21
def p_relop4(p):
    '''relop : GEQ'''
    print ("relop4")

# 21
def p_relop5(p):
    '''relop : EQ '''
    print ("relop5")

# 21
def p_relop6(p):
    '''relop : NEQ'''
    print ("relop6")

# 22
def p_additiveExpression1(p):
    '''additiveExpression : additiveExpression addop term'''
    print ("additiveExpression1")

# 22
def p_additiveExpression2(p):
    '''additiveExpression : term'''
    print ("additiveExpression2")

# 23
def p_addop1(p):
    '''addop : PLUS'''
    print ("addop1")

# 23
def p_addop2(p):
    '''addop : MINUS'''
    print ("addop2")

# 24
def p_term1(p):
    '''term : term mulop factor'''
    print ("term1")

# 24
def p_term2(p):
    '''term : factor'''
    print ("term2")

# 25
def p_mulop1(p):
    '''mulop : TIMES'''
    print ("mulop1")

# 25
def p_mulop2(p):
    '''mulop : DIVIDE'''
    print ("mulop2")

# 26
def p_factor1(p):
    '''factor : factor powop exp'''
    print ("factor1")

# 26
def p_factor2(p):
    '''factor : exp'''
    print ("factor2")

# 27
def p_powop1(p):
    '''powop : POWOP1'''
    print ("powop1")

# 27
def p_powop2(p):
    '''powop : POWOP2'''
    print ("powop2")

# 28
def p_exp1(p):
    '''exp : LPARENT expression RPARENT'''
    print ("exp1")

# 28
def p_exp2(p):
    '''exp : var'''
    print ("exp2")

# 28
def p_exp3(p):
    '''exp : call'''
    print ("exp3")

# 28
def p_exp4(p):
    '''exp : NUMBER'''
    print ("exp4")

# 29
def p_call(p):
    '''call : ID LPARENT args RPARENT'''
    print ("call")

# 30
def p_args1(p):
    '''args : argList'''
    print ("args1")

# 30
def p_args2(p):
    '''args : empty'''
    p[0] = Null()
    print ("args2")

# 31
def p_argList1(p):
    '''argList : argList COMMA expression'''
    print ("argList1")

# 31
def p_argList2(p):
    '''argList : expression'''
    print ("argList2")

# 32
def p_empty(p):
    '''empty : '''
    pass


def p_error(p):
    print("Error de sintaxis" , p)
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


analyzer = lex.lex()
analyzer.input(message)



parser = yacc.yacc()
result = parser.parse(message)

# result.imprimir(" ")
# print(result.traducir())

graphFile = open('graphviztree.dot','w')
graphFile.write(result.traducir())
#.traducir()

graphFile.close()
print("Se ha guardado el programa traducido (graphviztree.dot")

print(result)

while True:
    tok = analyzer.token()
    if not tok: break
    print(tok)