txt = ""
cont = 0
nivel = 0

def incrementarContador ():
    global cont
    cont += 1
    return "%d" %cont

def getScope(id):
    if(len(Nodo.scopes)==0):
        return
    else:
        for x in range(0, len(Nodo.scopes)):
            print("Scope: "+str(Nodo.scopes[x]))
            if(Nodo.scopes[x].id==id):
                print(Nodo.scopes[x])
                return Nodo.scopes[x]

class Nodo():
    variablesGlobales = []
    funciones = []
    scopes = []




class Scope():
    def __init__(self, id):
        self.id = id
        self.nivel = nivel
        self.localVariables = []


class Null(Nodo):

    def __init__(self):
        self.type = 'void'
        self.name = "Nodo nulo"

    def imprimir(self, ident):
        print(ident + "Nodo nulo")

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id+"[label= "+"Nodo_nulo"+"]"+"\n\t"

        return id

# 1
class program(Nodo):

    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()


        txt += id + "[label = \"" + self.name + "\\nVariables globales" + str(Nodo.variablesGlobales) + "\\nFunciones" + str(Nodo.funciones) + "\"]" + "\n\t"
        txt += id+"->"+son1+"\n\t"


        return "digraph G {\n\t"+txt+"}"
    
# 2
class declarationList1(Nodo):
    


    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    def imprimir(self,ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        print(ident+"Nodo: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

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

    def __init__(self,son1,son2,son3, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.name = name
        self.tipoVariable = son1.tipo
        self.idVariable = son2.name
        self.variable = "id: " + self.idVariable + " - tipo: " + son1.tipo
        print(self.variable)
        if(len(Nodo.scopes)==0):
            print("Esta variable es global: " +self.idVariable + " y es de tipo: " +self.tipoVariable)
            variable = []
            variable.append("id: "+self.idVariable+" - tipo: "+self.tipoVariable)
            Nodo.variablesGlobales.append(variable)
        else:
            print("Esta variable es local: " +self.idVariable + " y es de tipo: " +self.tipoVariable)




    def imprimir(self,ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)

        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
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
        self.tipoVariable = son1.tipo
        self.idVariable = son2.name
        self.variable = "id: " + self.idVariable + "tipo: " + son1.tipo
        # print("Scopes: " + str(len(Nodo.scopes)))
        if (len(Nodo.scopes) == 0):
            print("Esta variable es global: " + self.idVariable + " y es de tipo: " + self.tipoVariable)
            variable = []
            variable.append("id: " + self.idVariable + " - tipo: " + self.tipoVariable)
            Nodo.variablesGlobales.append(variable)
        else:
            print("Esta variable es local: " + self.idVariable + " y es de tipo: " + self.tipoVariable)

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)
        self.son5.imprimir(" " + ident)
        self.son6.imprimir(" " + ident)
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
        self.tipo = son1.name

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
        self.tipo = son1.name

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
    


    def __init__(self,son1, son2, son3,son4,son5,son6, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.tipoFuncion = son1.tipo
        self.idFuncion = son2.name
        self.params = son4.params
        self.variablesLocales = son6.variablesLocales
        print("Esta funcion se llama: " + self.idFuncion + " y es de tipo: " + self.tipoFuncion + " y tiene variables: "+str(self.variablesLocales))
        funcion = []
        funcion.append("id: "+self.idFuncion+" tipo: "+self.tipoFuncion)
        Nodo.funciones.append(funcion)
    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)

        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)

        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else:
            self.son4.imprimir(" "+ident)

        if type(self.son5) == type(tuple()):
            self.son5[0].imprimir(" "+ident)
        else:
            self.son5.imprimir(" "+ident)

        if type(self.son6) == type(tuple()):
            self.son6[0].imprimir(" "+ident)
        else:
            self.son6.imprimir(" "+ident)
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


        txt += id + "[label = \"" + self.name + "\\nParametros: " + str(self.params) + "\\nVariables locales: " + str(self.variablesLocales) + " \"]" + "\n\t"
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
        self.params = son1.params


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
        self.params = son1.name

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
        self.params = []
        self.params.append(son1.params)
        self.params.append(son3.param)

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
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
    
# 8
class paramList2(Nodo):
    


    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1
        self.params = son1.param

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
        self.param = []
        self.param.append(son1.tipo)
        self.param.append(son2.name)

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
        self.param = []
        self.param.append(son1.tipo)
        self.param.append(son2.name)

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
        self.variablesLocales =  []
        if(son2.name != "Nodo nulo"):
            self.variablesLocales.append(son2.variables)
        Nodo.scopes.append("")

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else:
            self.son4.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()

        txt += id + "[label = \"" + self.name + "\\nVariables locales: " +str(self.variablesLocales) + "\"]" + "\n\t"
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
        self.variables = []
        if(son1.name=="Nodo nulo"):
            self.variables.append(son2.variable)
        else:
            self.variables.append(son1.variables)
            self.variables.append(son2.variable)

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
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
        else:
            self.son1.imprimir(" "+ident)
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
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
        son2 = self.son2.traducir()

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
        else:
            self.son1.imprimir(" "+ident)
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else:
            self.son4.imprimir(" "+ident)
        if type(self.son5) == type(tuple()):
            self.son5[0].imprimir(" "+ident)
        else:
            self.son5.imprimir(" "+ident)
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
        return id
    
# 15
class selectionStmt2(Nodo):
    


    def __init__(self, son1, son2, son3, son4, son5, son6, son7, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        self.son4.imprimir(" "+ident)
        self.son5.imprimir(" "+ident)
        self.son6.imprimir(" "+ident)
        self.son7.imprimir(" "+ident)
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
        return id
    

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
        else:
            self.son1.imprimir(" "+ident)
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else:
            self.son4.imprimir(" "+ident)
        if type(self.son5) == type(tuple()):
            self.son5[0].imprimir(" "+ident)
        else:
            self.son5.imprimir(" "+ident)
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
        return id

# 17
class returnStmt1(Nodo):
    


    def __init__(self,son1, son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
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
        else:
            self.son1.imprimir(" "+ident)
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
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
        else:
            self.son1.imprimir(" "+ident)
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
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
        return id
    

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
        return id
    

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
        else:
            self.son1.imprimir(" "+ident)
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else:
            self.son4.imprimir(" "+ident)
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
    

# 20
class simpleExpression1(Nodo):
    


    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
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
        return id
   

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
        return id
    
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
        return id
   
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
        return id
   

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
        return id
    

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
        return id
    

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
        return id
    

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
        else:
            self.son1.imprimir(" "+ident)
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
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
        return id
    

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
        return id
    

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
        return id

# 24
class term1(Nodo):
    


    def __init__(self, son1, son2 ,son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3


    def imprimir(self, ident):
        if type(self.son1) == type(tuple()): 
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
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
        return id
    

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
        return id
    

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
        return id
    

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
        else:
            self.son1.imprimir(" "+ident)
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
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
        return id


# 27
class factor3(Nodo):
    


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
        return id;


# 27
class factor4(Nodo):
    


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
        return id;
   

#27
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
            self.son2[0].imprimir(" "+ident)
            self.son3[0].imprimir(" "+ident)
            self.son4[0].imprimir(" "+ident)
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

# 28
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
        return id;

# 28
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
        return id;

# 29
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
        return id;

#  29
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
        return id;
# 32
class empty(Nodo):
    


    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        # self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class error(Nodo):
    


    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        # self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)
        

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

# Terminales y reservadas
class ID(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"ID: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=  \""+"ID: "+self.name +"\"]"+"\n\t"
        return id
class PLUS(Nodo):
    


    def __init__(self , name):
        self.name = name
        # self.value =

    def imprimir(self , ident):
        print(ident+"PLUS: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"PLUS: "+self.name+"\"]"+"\n\t"
        return id
class MINUS(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"MINUS: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"MINUS: "+self.name+"\"]"+"\n\t"
        return id
class TIMES(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"TIMES: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"TIMES: "+self.name+"\"]"+"\n\t"
        return id
class DIVIDE(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"DIVIDE: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"DIVIDE: "+self.name+"\"]"+"\n\t"
        return id
class LT(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"LT: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"LT: "+self.name+"\"]"+"\n\t"
        return id
class LEQ(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"LEQ: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"LEQ: "+self.name+"\"]"+"\n\t"
        return id
class GT(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"GT: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"GT: "+self.name+"\"]"+"\n\t"
        return id
class GEQ(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"GEQ: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"GEQ: "+self.name+"\"]"+"\n\t"
        return id
class EQ(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"EQ: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"EQ: "+self.name+"\"]"+"\n\t"
        return id
class NEQ(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"NEQ: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"NEQ: "+self.name+"\"]"+"\n\t"
        return id
class LPARENT(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"LPARENT: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"LPARENT: "+self.name+"\"]"+"\n\t"
        return id
class RPARENT(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"RPARENT: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"RPARENT: "+self.name+"\"]"+"\n\t"
        return id
class LBRACKET(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"LBRACKET: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"LBRACKET: "+self.name+"\"]"+"\n\t"
        return id
class RBRACKET(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"RBRACKET: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"RBRACKET: "+self.name+"\"]"+"\n\t"
        return id
class LBRACE(Nodo):
    


    def __init__(self , name):
        self.name = name
        self.id = id
    def imprimir(self , ident):
        print(ident+"LBRACE: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"LBRACE: "+self.name+"\"]"+"\n\t"
        return id
class RBRACE(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"RBRACE: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"RBRACE: "+self.name+"\"]"+"\n\t"
        return id
class POWOP1(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"POWOP1: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"POWOP1: "+self.name+"\"]"+"\n\t"
        return id
class POWOP2(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"POWOP2: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"POWOP2: "+self.name+"\"]"+"\n\t"
        return id
class SEMICOLON(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"SEMICOLON: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"SEMICOLON: "+self.name+"\"]"+"\n\t"
        return id
class COMMA(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"COMMA: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"COMMA: "+self.name+"\"]"+"\n\t"
        return id
class ASSIGN(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"ASSIGN: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"ASSIGN: "+self.name+"\"]"+"\n\t"
        return id
class NUMBER(Nodo):
    


    def __init__(self , name):
        self.name = str(name)
        self.value = name

    def imprimir(self , ident):
        print(ident+"NUMBER: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"NUMBER: "+self.name+"\"]"+"\n\t"
        return id



class SCOMMENT(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"SCOMMENT: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"SCOMMENT: "+self.name+"\"]"+"\n\t"
        return id
class BEGINCOMMENT(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"BEGINCOMMENT: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id
class ENDCOMMENT(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"ENDCOMMENT: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class ELSE(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"ELSE: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"ELSE: "+self.name+"\"]"+"\n\t"
        return id

class IF(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"IF: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"IF: "+self.name+"\"]"+"\n\t"
        return id

class INT(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"INT: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"INT: "+self.name+"\"]"+"\n\t"
        return id

class VOID(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"VOID: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"VOID: "+self.name+"\"]"+"\n\t"
        return id

class RETURN(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"RETURN: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"RETURN: "+self.name+"\"]"+"\n\t"
        return id



class WHILE(Nodo):
    


    def __init__(self , name):
        self.name = name

    def imprimir(self , ident):
        print(ident+"WHILE: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \""+"WHILE: "+self.name+"\"]"+"\n\t"
        return id