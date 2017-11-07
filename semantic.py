txt = ""
cont = 0
def incrementarContador ():
    global cont
    cont += 1
    return "%d" %cont

class Nodo():
    pass

class Null(Nodo):
    def __init__(self):
        self.type = 'void'

    def imprimir(self, ident):
        print(ident + "nodo nulo")

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id+"[label= "+"nodo_nulo"+"]"+"\n\t"

        return id

# 1
class program(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id+"[label = "+self.name+"]"+"\n\t"
        txt += id+"->"+son1+"\n\t"


        return "digraph G {\n\t"+txt+"}"
    
# 2
class declarationList1(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        print(ident+"Nodo: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"

        return id
    
# 2
class declarationList2(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        print(ident+"Nodo: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        return id
    
# 3
class declaration1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        return id
    

# 3
class declaration2(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

        return id
    
# 4

class varDeclaration1(Nodo):
    def __init__(self,son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        return id
    
# 4
class varDeclaration2(Nodo):
    def __init__(self,son1,son2,son3,son4,son5,son6,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
            self.son4.imprimir(" "+ident)
            self.son5.imprimir(" "+ident)
            self.son6.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        son5 = self.son5.traducir()
        son6 = self.son6.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"
        txt += id + "->" + son5 + "\n\t"
        txt += id + "->" + son6 + "\n\t"
        return id
    
# 5
class typeSpecifier1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

        return id
    
# 5
class typeSpecifier2(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

        return id
    
# 6
class funDeclaration(Nodo):
    def __init__(self,son1, son2, son3, son4, son5, son6, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6


    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
            self.son4.imprimir(" "+ident)
            self.son5.imprimir(" "+ident)
            self.son6.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        son5 = self.son5.traducir()
        son6 = self.son6.traducir()


        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"
        txt += id + "->" + son5 + "\n\t"
        txt += id + "->" + son6 + "\n\t"
        return id
    

# 7
class params1(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        return id
    

# 7
class params2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        return id
    

# 8
class paramList1(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son1.traducir()
        son3 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        return id
    
# 8
class paramList2(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        return id
    

# 9
class param1(Nodo):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        return id
    

# 9
class param2(Nodo):
    def __init__(self,son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"


        return id
    

# 10
class compoundStmt(Nodo):
    def __init__(self,son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
            self.son4.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"
        return id
    

# 11
class localDeclarations1(Nodo):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        return id
    

# 11
class localDeclarations2(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)

        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        return id
    

# 12
class statementList1(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"

        return id
    

# 12
class statementList2(Nodo):
    def __init__(self, son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

        return id
    

# 13
class statement1(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1  = son1

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

        return id
    

# 13
class statement2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

        return id
    
# 13
class statement3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

        return id
    
# 13
class statement4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

        return id
    
# 13
class statement5(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

        return id
    

# 14
class expressionStmt1(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"

        return id
    

# 14
class expressionStmt2(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        return id
    

# 15
class selectionStmt1(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
            self.son4.imprimir(" "+ident)
            self.son5.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        son5 = self.son5.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"
        txt += id + "->" + son5 + "\n\t"
    
# 15
class selectionStmt2(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
            self.son4.imprimir(" "+ident)
            self.son5.imprimir(" "+ident)
            self.son6.imprimir(" "+ident)
            self.son7.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        son5 = self.son5.traducir()
        son6 = self.son6.traducir()
        son7 = self.son7.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"
        txt += id + "->" + son5 + "\n\t"
        txt += id + "->" + son6 + "\n\t"
        txt += id + "->" + son7 + "\n\t"
    

# 16
class iterationStmt(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
            self.son4.imprimir(" "+ident)
            self.son5.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        son5 = self.son5.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"
        txt += id + "->" + son5 + "\n\t"

# 17
class returnStmt1(Nodo):
    def __init__(self,son1, son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        return id
    

# 17
class returnStmt2(Nodo):
    def __init__(self, son1, son2,son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        return id
    

# 18
class expression1(Nodo):
    def __init__(self, son1, son2,son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
    

# 18
class expression2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
    

# 19
class var1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
    

# 19
class var2(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
            self.son4.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"
    

# 20
class simpleExpression1(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son1
        self.son3 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son1.traducir()
        son3 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
   

# 20
class simpleExpression2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
   

# 21
class relop1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
    
# 21
class relop2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
   
# 21
class relop3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
   

# 21
class relop4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
    

# 21
class relop5(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
    

# 21
class relop6(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
    

# 22
class additiveExpression1(Nodo):
    def __init__(self, son1,son2,son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
    

# 22
class additiveExpression2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
    

# 23
class addop1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
    

# 23
class addop2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
    

# 24
class term1(Nodo):
    def __init__(self, son1,son2,son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
    

# 24
class term2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
    

# 25
class mulop1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
    

# 25
class mulop2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
    

# 26
class factor1(Nodo):
    def __init__(self, son1,son2,son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
    

# 26
class factor2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"


# 27
class powop1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"


# 27
class powop2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
   

# 28
class exp1(Nodo):
    def __init__(self, son1,son2,son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
   

# 28
class exp2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

# 28
class exp3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

# 28
class exp4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

# 29
class call(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
            self.son4.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"
        return id

# 30
class args1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

# 30
class args2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

# 31
class argList1(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
            self.son2.imprimir(" "+ident)
            self.son3.imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"

# 31
class argList2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()

        txt += id + "[label = " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
# 32
class empty(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class error(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

# Terminales
class ID(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class PLUS(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class MINUS(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class TIMES(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class DIVIDE(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class LT(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class LEQ(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class GT(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class GEQ(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class EQ(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class NEQ(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class LPARENT(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class RPARENT(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class LBRACKET(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class RBRACKET(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class LBRACE(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class RBRACE(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class POWOP1(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class POWOP2(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class SEMICOLON(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class COMMA(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class ASSIGN(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class NUMBER(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

# def __init__(self , name):
#     self.name = name
#
# def imprimir(self , ident):
#     print(ident+""+self.name)
#
# def traducir(self):
#     global txt
#     id = incrementarContador()
#     txt += id + "[label= \""+self.name+"\"]"+"\n\t"
#     return id
#
# def __init__(self , name):
#     self.name = name
#
# def imprimir(self , ident):
#     print(ident+""+self.name)
#
# def traducir(self):
#     global txt
#     id = incrementarContador()
#     txt += id + "[label= \""+self.name+"\"]"+"\n\t"
#     return id
class SCOMMENT(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class BEGINCOMMENT(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class ENDCOMMENT(Nodo):
    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+""+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id


