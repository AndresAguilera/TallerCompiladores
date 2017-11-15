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
    p[0] = program(p[1],  "program")
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
    p[0] = varDeclaration2(p[1], ID(p[2]),LBRACKET(p[3]), NUMBER(p[4]), RBRACKET(p[5]),SEMICOLON(p[6]), "varDeclaration2")
    print ("varDeclaration2")
# 5
def p_typeSpecifier1(p):
    '''typeSpecifier : INT'''
    p[0] = typeSpecifier1(INT(p[1]),"typeSpecifier1")
    print ("typeSpecifier1")
# 5
def p_typeSpecifier2(p):
    '''typeSpecifier : VOID'''
    p[0] = typeSpecifier2(VOID(p[1]),"typeSpecifier2")
    print ("typeSpecifier2")
# 6
def p_funDeclaration(p):
    '''funDeclaration : typeSpecifier ID LPARENT params RPARENT compoundStmt'''
    p[0] = funDeclaration(p[1],ID(p[2]),LPARENT(p[3]),p[4],RPARENT(p[5]),p[6],"funDeclaration")
    print ("funDeclaration")

# 7
def p_params1(p):
    '''params : paramList'''
    p[0] = params1(p[1],"params1")
    print ("params1")

# 7
def p_params2(p):
    '''params : VOID'''
    p[0] = params2(VOID(p[1]), "params2")
    print ("params2")

# 8
def p_paramList1(p):
    '''paramList : paramList COMMA param'''
    p[0] = paramList1(p[1],COMMA(p[2]),p[3],"paramList1")
    print ("paramList1")
# 8
def p_paramList2(p):
    '''paramList : param'''
    p[0] = paramList2(p[1], "paramList2")
    print ("paramList2")

# 9
def p_param1(p):
    '''param : typeSpecifier ID'''
    p[0] = param1(p[1],ID(p[2]), "paramList2")
    print ("param1")

# 9
def p_param2(p):
    '''param : typeSpecifier ID LBRACKET RBRACKET '''
    p[0] = param2(p[1],ID(p[2]),LBRACKET(p[3]),RBRACKET(p[4]),"param2")
    print ("param2")

# 10
def p_compoundStmt(p):
    '''compoundStmt : LBRACE localDeclarations statementList RBRACE'''
    p[0] = compoundStmt(LBRACE(p[1]),p[2],p[3],RBRACE(p[4]),"compoundStmt")
    print ("compound-stmt")

# 11
def p_localDeclarations1(p):
    '''localDeclarations : localDeclarations varDeclaration'''
    p[0] = localDeclarations1(p[1],p[2],"localDeclarations1")
    print ("local-declarations1")

# 11
def p_localDeclarations2(p):
    '''localDeclarations : empty'''
    p[0] = Null()
    print ("local-declarations2")

# 12
def p_statementList1(p):
    '''statementList : statementList statement'''
    p[0] = statementList1(p[1],p[2],"statementList1")
    print ("statement-list1")

# 12
def p_statementList2(p):
    '''statementList : empty'''
    p[0] = Null()
    print("statementList2")

# 13
def p_statement1(p):
    '''statement : expressionStmt'''
    p[0] = statement1(p[1],"statement1")
    print ("statement1")

# 13
def p_statement2(p):
    '''statement : compoundStmt'''
    p[0] = statement2(p[1],"statement2")
    print ("statement2")
# 13
def p_statement3(p):
    '''statement : selectionStmt'''
    p[0] = statement3(p[1], "statement3")
    print ("statement3")
# 13
def p_statement4(p):
    '''statement : iterationStmt'''
    p[0] = statement4(p[1], "statement4")
    print ("statement4")
# 13
def p_statement5(p):
    '''statement : returnStmt'''
    p[0] = statement5(p[1], "statement5")
    print ("statement5")

# 14
def p_expressionStmt1(p):
    '''expressionStmt : expression SEMICOLON '''
    p[0] = expressionStmt1(p[1],SEMICOLON(p[2]), "statement2")
    print ("expression-stmt1")

# 14
def p_expressionStmt2(p):
    '''expressionStmt :  SEMICOLON '''
    p[0] = expressionStmt2(SEMICOLON(p[1]), "statement2")
    print ("expression-stmt2")

# 15
def p_selectionStmt1(p):
    '''selectionStmt : IF LPARENT expression RPARENT statement'''
    p[0] = selectionStmt1(IF(p[1]),LPARENT(p[2]),p[3],RPARENT(p[4]),p[5],"selectionStmt1")
    print ("selectionStmt1")
# 15
def p_selectionStmt2(p):
    '''selectionStmt : IF LPARENT expression RPARENT statement ELSE statement'''
    p[0] = selectionStmt2(IF(p[1]), LPARENT(p[2]), p[3], RPARENT(p[4]), ELSE(p[5]),p[6], "selectionStmt2")
    print ("selectionStmt2")

# 16
def p_iterationStmt(p):
    '''iterationStmt : WHILE LPARENT expression RPARENT statement'''
    p[0] = iterationStmt(WHILE(p[1]),LPARENT(p[2]),p[3],RPARENT(p[4]),p[5],"iterationStmt")
    print ("iterationStmt")

# 17
def p_returnStmt1(p):
    '''returnStmt : RETURN SEMICOLON'''
    p[0] = returnStmt1(RETURN(p[1]),SEMICOLON(p[2]),"returnStmt1")
    print ("returnStmt1")

# 17
def p_returnStmt2(p):
    '''returnStmt : RETURN expression SEMICOLON'''
    p[0] = returnStmt2(RETURN(p[1]),p[2], SEMICOLON(p[3]), "returnStmt2")
    print ("returnStmt2")

# 18
def p_expression1(p):
    '''expression : var EQ expression'''
    p[0] = expression1(p[1], EQ(p[2]),p[3],"expression1")
    print ("expression1")

# 18
def p_expression2(p):
    '''expression : simpleExpression'''
    p[0] = expression2(p[1],"expression2")
    print ("expression2")

# 19
def p_var1(p):
    '''var : ID'''
    p[0] = var1(ID(p[1]),"var1")
    print ("var1")

# 19
def p_var2(p):
    '''var : ID LBRACKET expression RBRACKET'''
    p[0] = var2(ID(p[1]),LBRACKET(p[2]),p[3],RBRACKET[4], "var2")
    print ("var2")

# 20
def p_simpleExpression1(p):
    '''simpleExpression : additiveExpression relop additiveExpression'''
    p[0] = simpleExpression1(p[1], p[2], p[3], "simpleExpression1")
    print ("simple-expression1")

# 20
def p_simpleExpression2(p):
    '''simpleExpression : additiveExpression'''
    p[0] = simpleExpression2(p[1], "simpleExpression2")
    print ("simple-expression2")

# 21
def p_relop1(p):
    '''relop : LEQ'''
    p[0] = relop1(LEQ(p[1]),"relop1")
    print ("relop1")

# 21
def p_relop2(p):
    '''relop : LT'''
    p[0] = relop2(LT(p[1]), "relop2")
    print ("relop2")

# 21
def p_relop3(p):
    '''relop : GT'''
    p[0] = relop3(GT(p[1]), "relop3")
    print ("relop3")

# 21
def p_relop4(p):
    '''relop : GEQ'''
    p[0] = relop4(GEQ(p[1]), "relop4")
    print ("relop4")

# 21
def p_relop5(p):
    '''relop : EQ '''
    p[0] = relop5(EQ(p[1]), "relop5")
    print ("relop5")

# 21
def p_relop6(p):
    '''relop : NEQ'''
    p[0] = relop6(NEQ(p[1]), "relop6")
    print ("relop6")

# 22
def p_additiveExpression1(p):
    '''additiveExpression : additiveExpression addop term'''
    p[0] = additiveExpression1(p[1],p[2],p[3], "additiveExpression1")
    print ("additiveExpression1")

# 22
def p_additiveExpression2(p):
    '''additiveExpression : term'''
    p[0] = additiveExpression2(p[1], "additiveExpression2")
    print ("additiveExpression2")

# 23
def p_addop1(p):
    '''addop : PLUS'''
    p[0] = addop1(PLUS(p[1]),"addop1")
    print ("addop1")

# 23
def p_addop2(p):
    '''addop : MINUS'''
    p[0] = addop2(MINUS(p[1]), "addop2")
    print ("addop2")

# 24
def p_term1(p):
    '''term : term mulop factor'''
    p[0] = term1(p[1],p[2],p[3], "term1")
    print ("term1")

# 24
def p_term2(p):
    '''term : factor'''
    p[0] = term2(p[1], "term2")
    print ("term2")

# 25
def p_mulop1(p):
    '''mulop : TIMES'''
    p[0] = mulop1(TIMES(p[1]), "mulop1")
    print ("mulop1")

# 25
def p_mulop2(p):
    '''mulop : DIVIDE'''
    p[0] = mulop2(DIVIDE(p[1]), "mulop2")
    print ("mulop2")

# 26
def p_factor1(p):
    '''factor : factor powop exp'''
    p[0] = factor1(p[1],p[2],p[3], "factor1")
    print ("factor1")

# 26
def p_factor2(p):
    '''factor : exp'''
    p[0] = factor2(p[1], "factor2")
    print ("factor2")

# 27
def p_powop1(p):
    '''powop : POWOP1'''
    p[0] = powop1(POWOP1(p[1]), "powop1")
    print ("powop1")

# 27
def p_powop2(p):
    '''powop : POWOP2'''
    p[0] = powop2(POWOP2(p[1]), "powop2")
    print ("powop2")

# 28
def p_exp1(p):
    '''exp : LPARENT expression RPARENT'''
    p[0] = exp1(LPARENT(p[1]),p[2],RPARENT(p[3]), "exp1")
    print ("exp1")

# 28
def p_exp2(p):
    '''exp : var'''
    p[0] = exp2(p[1], "exp2")
    print ("exp2")

# 28
def p_exp3(p):
    '''exp : call'''
    p[0] = exp3(p[1], "exp3")
    print ("exp3")

# 28
def p_exp4(p):
    '''exp : NUMBER'''
    p[0] = exp4(NUMBER(p[1]), "exp4")
    print ("exp4")

# 29
def p_call(p):
    '''call : ID LPARENT args RPARENT'''
    p[0] = call(ID(p[1]),LPARENT(p[2]),p[3],RPARENT(p[4]),"call")
    print ("call")

# 30
def p_args1(p):
    '''args : argList'''
    p[0] = args1(p[1],"args1")
    print ("args1")

# 30
def p_args2(p):
    '''args : empty'''
    p[0] = Null()
    print ("args2")

# 31
def p_argList1(p):
    '''argList : argList COMMA expression'''
    p[0] = argList1(p[1],COMMA(p[2]),p[3], "argList1")
    print ("argList1")

# 31
def p_argList2(p):
    '''argList : expression'''
    p[0] = argList2(p[1],"argList2")
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

result.imprimir(" ")
# print(result.traducir())

graphFile = open('graphviztree.dot','w')
graphFile.write(result.traducir())
#.traducir()

graphFile.close()
print("Se ha guardado el programa traducido en /graphviztree.dot")

print(result)

while True:
    tok = analyzer.token()
    if not tok: break
    print(tok)