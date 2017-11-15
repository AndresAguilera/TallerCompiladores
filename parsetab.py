
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightIDIFWHILErightASSIGNleftLTLEQGTGEQleftPLUSMINUSleftTIMESDIVIDEleftLPARENTRPARENTPLUS MINUS TIMES DIVIDE LT LEQ GT GEQ EQ NEQ LPARENT RPARENT LBRACKET RBRACKET LBRACE RBRACE SCOMMENT BEGINCOMMENT ENDCOMMENT MCOMMENT POWOP1 POWOP2 SEMICOLON COMMA ID ASSIGN NUMBER ELSE IF INT VOID RETURN WHILEprogram : declarationListdeclarationList : declarationList declarationdeclarationList : declarationdeclaration : varDeclarationdeclaration : funDeclarationvarDeclaration : typeSpecifier ID SEMICOLONvarDeclaration : typeSpecifier ID LBRACKET NUMBER RBRACKET SEMICOLONtypeSpecifier : INTtypeSpecifier : VOIDfunDeclaration : typeSpecifier ID LPARENT params RPARENT compoundStmtparams : paramListparams : VOIDparamList : paramList COMMA paramparamList : paramparam : typeSpecifier IDparam : typeSpecifier ID LBRACKET RBRACKET compoundStmt : LBRACE localDeclarations statementList RBRACElocalDeclarations : localDeclarations varDeclarationlocalDeclarations : emptystatementList : statementList statementstatementList : emptystatement : expressionStmtstatement : compoundStmtstatement : selectionStmtstatement : iterationStmtstatement : returnStmtexpressionStmt : expression SEMICOLON expressionStmt :  SEMICOLON selectionStmt : IF LPARENT expression RPARENT statementselectionStmt : IF LPARENT expression RPARENT statement ELSE statementiterationStmt : WHILE LPARENT expression RPARENT statementreturnStmt : RETURN SEMICOLONreturnStmt : RETURN expression SEMICOLONexpression : var EQ expressionexpression : simpleExpressionvar : IDvar : ID LBRACKET expression RBRACKETsimpleExpression : additiveExpression relop additiveExpressionsimpleExpression : additiveExpressionrelop : LEQrelop : LTrelop : GTrelop : GEQrelop : EQ relop : NEQadditiveExpression : additiveExpression addop termadditiveExpression : termaddop : PLUSaddop : MINUSterm : term mulop factorterm : factormulop : TIMESmulop : DIVIDEfactor : factor powop expfactor : exppowop : POWOP1powop : POWOP2exp : LPARENT expression RPARENTexp : varexp : callexp : NUMBERcall : ID LPARENT args RPARENTargs : argListargs : emptyargList : argList COMMA expressionargList : expressionempty : '
    
_lr_action_items = {'INT':([0,2,3,4,5,9,11,13,23,24,26,27,30,31,33,36,],[7,7,-3,-4,-5,-2,-6,7,7,-7,-10,-67,7,-19,-18,-17,]),'VOID':([0,2,3,4,5,9,11,13,23,24,26,27,30,31,33,36,],[8,8,-3,-4,-5,-2,-6,18,8,-7,-10,-67,8,-19,-18,-17,]),'$end':([1,2,3,4,5,9,11,24,26,36,],[0,-1,-3,-4,-5,-2,-6,-7,-10,-17,]),'ID':([6,7,8,11,15,18,24,27,30,31,32,33,34,35,36,37,38,39,40,41,42,44,46,48,59,60,62,63,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,87,99,100,103,104,105,107,108,],[10,-8,-9,-6,21,-9,-7,-67,-67,-19,51,-18,-21,58,-17,-20,-22,-23,-24,-25,-26,-28,51,51,-27,51,51,-32,51,51,51,51,51,-40,-41,-42,-43,-44,-45,-48,-49,51,-52,-53,51,-56,-57,-33,51,51,51,-29,-31,51,-30,]),'SEMICOLON':([10,11,20,24,27,30,31,32,33,34,36,37,38,39,40,41,42,43,44,48,49,50,51,52,53,54,55,56,57,58,59,63,64,85,87,88,94,95,96,97,98,99,100,101,102,104,105,107,108,],[11,-6,24,-7,-67,-67,-19,44,-18,-21,-17,-20,-22,-23,-24,-25,-26,59,-28,63,-59,-35,-36,-39,-47,-51,-55,-60,-61,11,-27,-32,87,-58,-33,-34,-38,-59,-46,-50,-54,44,44,-37,-62,-29,-31,44,-30,]),'LBRACKET':([10,21,51,58,],[12,25,66,12,]),'LPARENT':([10,11,24,27,30,31,32,33,34,36,37,38,39,40,41,42,44,45,46,47,48,51,59,60,62,63,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,87,99,100,103,104,105,107,108,],[13,-6,-7,-67,-67,-19,46,-18,-21,-17,-20,-22,-23,-24,-25,-26,-28,60,46,62,46,67,-27,46,46,-32,46,46,46,46,46,-40,-41,-42,-43,-44,-45,-48,-49,46,-52,-53,46,-56,-57,-33,46,46,46,-29,-31,46,-30,]),'RBRACE':([11,24,27,30,31,32,33,34,36,37,38,39,40,41,42,44,59,63,87,104,105,108,],[-6,-7,-67,-67,-19,36,-18,-21,-17,-20,-22,-23,-24,-25,-26,-28,-27,-32,-33,-29,-31,-30,]),'LBRACE':([11,22,24,27,30,31,32,33,34,36,37,38,39,40,41,42,44,59,63,87,99,100,104,105,107,108,],[-6,27,-7,-67,-67,-19,27,-18,-21,-17,-20,-22,-23,-24,-25,-26,-28,-27,-32,-33,27,27,-29,-31,27,-30,]),'IF':([11,24,27,30,31,32,33,34,36,37,38,39,40,41,42,44,59,63,87,99,100,104,105,107,108,],[-6,-7,-67,-67,-19,45,-18,-21,-17,-20,-22,-23,-24,-25,-26,-28,-27,-32,-33,45,45,-29,-31,45,-30,]),'WHILE':([11,24,27,30,31,32,33,34,36,37,38,39,40,41,42,44,59,63,87,99,100,104,105,107,108,],[-6,-7,-67,-67,-19,47,-18,-21,-17,-20,-22,-23,-24,-25,-26,-28,-27,-32,-33,47,47,-29,-31,47,-30,]),'RETURN':([11,24,27,30,31,32,33,34,36,37,38,39,40,41,42,44,59,63,87,99,100,104,105,107,108,],[-6,-7,-67,-67,-19,48,-18,-21,-17,-20,-22,-23,-24,-25,-26,-28,-27,-32,-33,48,48,-29,-31,48,-30,]),'NUMBER':([11,12,24,27,30,31,32,33,34,36,37,38,39,40,41,42,44,46,48,59,60,62,63,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,87,99,100,103,104,105,107,108,],[-6,14,-7,-67,-67,-19,57,-18,-21,-17,-20,-22,-23,-24,-25,-26,-28,57,57,-27,57,57,-32,57,57,57,57,57,-40,-41,-42,-43,-44,-45,-48,-49,57,-52,-53,57,-56,-57,-33,57,57,57,-29,-31,57,-30,]),'RBRACKET':([14,25,49,50,51,52,53,54,55,56,57,85,88,89,94,95,96,97,98,101,102,],[20,29,-59,-35,-36,-39,-47,-51,-55,-60,-61,-58,-34,101,-38,-59,-46,-50,-54,-37,-62,]),'RPARENT':([16,17,18,19,21,28,29,49,50,51,52,53,54,55,56,57,61,67,84,85,86,88,90,91,92,93,94,95,96,97,98,101,102,106,],[22,-11,-12,-14,-15,-13,-16,-59,-35,-36,-39,-47,-51,-55,-60,-61,85,-67,99,-58,100,-34,102,-63,-64,-66,-38,-59,-46,-50,-54,-37,-62,-65,]),'COMMA':([17,19,21,28,29,49,50,51,52,53,54,55,56,57,85,88,91,93,94,95,96,97,98,101,102,106,],[23,-14,-15,-13,-16,-59,-35,-36,-39,-47,-51,-55,-60,-61,-58,-34,103,-66,-38,-59,-46,-50,-54,-37,-62,-65,]),'ELSE':([36,38,39,40,41,42,44,59,63,87,104,105,108,],[-17,-22,-23,-24,-25,-26,-28,-27,-32,-33,-29,-31,-30,]),'EQ':([49,51,52,53,54,55,56,57,85,95,96,97,98,101,102,],[65,-36,74,-47,-51,-55,-60,-61,-58,-59,-46,-50,-54,-37,-62,]),'POWOP1':([49,51,54,55,56,57,85,95,97,98,101,102,],[-59,-36,82,-55,-60,-61,-58,-59,82,-54,-37,-62,]),'POWOP2':([49,51,54,55,56,57,85,95,97,98,101,102,],[-59,-36,83,-55,-60,-61,-58,-59,83,-54,-37,-62,]),'TIMES':([49,51,53,54,55,56,57,85,95,96,97,98,101,102,],[-59,-36,79,-51,-55,-60,-61,-58,-59,79,-50,-54,-37,-62,]),'DIVIDE':([49,51,53,54,55,56,57,85,95,96,97,98,101,102,],[-59,-36,80,-51,-55,-60,-61,-58,-59,80,-50,-54,-37,-62,]),'LEQ':([49,51,52,53,54,55,56,57,85,95,96,97,98,101,102,],[-59,-36,70,-47,-51,-55,-60,-61,-58,-59,-46,-50,-54,-37,-62,]),'LT':([49,51,52,53,54,55,56,57,85,95,96,97,98,101,102,],[-59,-36,71,-47,-51,-55,-60,-61,-58,-59,-46,-50,-54,-37,-62,]),'GT':([49,51,52,53,54,55,56,57,85,95,96,97,98,101,102,],[-59,-36,72,-47,-51,-55,-60,-61,-58,-59,-46,-50,-54,-37,-62,]),'GEQ':([49,51,52,53,54,55,56,57,85,95,96,97,98,101,102,],[-59,-36,73,-47,-51,-55,-60,-61,-58,-59,-46,-50,-54,-37,-62,]),'NEQ':([49,51,52,53,54,55,56,57,85,95,96,97,98,101,102,],[-59,-36,75,-47,-51,-55,-60,-61,-58,-59,-46,-50,-54,-37,-62,]),'PLUS':([49,51,52,53,54,55,56,57,85,94,95,96,97,98,101,102,],[-59,-36,76,-47,-51,-55,-60,-61,-58,76,-59,-46,-50,-54,-37,-62,]),'MINUS':([49,51,52,53,54,55,56,57,85,94,95,96,97,98,101,102,],[-59,-36,77,-47,-51,-55,-60,-61,-58,77,-59,-46,-50,-54,-37,-62,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declarationList':([0,],[2,]),'declaration':([0,2,],[3,9,]),'varDeclaration':([0,2,30,],[4,4,33,]),'funDeclaration':([0,2,],[5,5,]),'typeSpecifier':([0,2,13,23,30,],[6,6,15,15,35,]),'params':([13,],[16,]),'paramList':([13,],[17,]),'param':([13,23,],[19,28,]),'compoundStmt':([22,32,99,100,107,],[26,39,39,39,39,]),'localDeclarations':([27,],[30,]),'empty':([27,30,67,],[31,34,92,]),'statementList':([30,],[32,]),'statement':([32,99,100,107,],[37,104,105,108,]),'expressionStmt':([32,99,100,107,],[38,38,38,38,]),'selectionStmt':([32,99,100,107,],[40,40,40,40,]),'iterationStmt':([32,99,100,107,],[41,41,41,41,]),'returnStmt':([32,99,100,107,],[42,42,42,42,]),'expression':([32,46,48,60,62,65,66,67,99,100,103,107,],[43,61,64,84,86,88,89,93,43,43,106,43,]),'var':([32,46,48,60,62,65,66,67,68,69,78,81,99,100,103,107,],[49,49,49,49,49,49,49,49,95,95,95,95,49,49,49,49,]),'simpleExpression':([32,46,48,60,62,65,66,67,99,100,103,107,],[50,50,50,50,50,50,50,50,50,50,50,50,]),'additiveExpression':([32,46,48,60,62,65,66,67,68,99,100,103,107,],[52,52,52,52,52,52,52,52,94,52,52,52,52,]),'term':([32,46,48,60,62,65,66,67,68,69,99,100,103,107,],[53,53,53,53,53,53,53,53,53,96,53,53,53,53,]),'factor':([32,46,48,60,62,65,66,67,68,69,78,99,100,103,107,],[54,54,54,54,54,54,54,54,54,54,97,54,54,54,54,]),'exp':([32,46,48,60,62,65,66,67,68,69,78,81,99,100,103,107,],[55,55,55,55,55,55,55,55,55,55,55,98,55,55,55,55,]),'call':([32,46,48,60,62,65,66,67,68,69,78,81,99,100,103,107,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'relop':([52,],[68,]),'addop':([52,94,],[69,69,]),'mulop':([53,96,],[78,78,]),'powop':([54,97,],[81,81,]),'args':([67,],[90,]),'argList':([67,],[91,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declarationList','program',1,'p_program','parser.py',23),
  ('declarationList -> declarationList declaration','declarationList',2,'p_declarationList1','parser.py',28),
  ('declarationList -> declaration','declarationList',1,'p_declarationList2','parser.py',34),
  ('declaration -> varDeclaration','declaration',1,'p_declaration1','parser.py',39),
  ('declaration -> funDeclaration','declaration',1,'p_declaration2','parser.py',45),
  ('varDeclaration -> typeSpecifier ID SEMICOLON','varDeclaration',3,'p_varDeclaration1','parser.py',51),
  ('varDeclaration -> typeSpecifier ID LBRACKET NUMBER RBRACKET SEMICOLON','varDeclaration',6,'p_varDeclaration2','parser.py',56),
  ('typeSpecifier -> INT','typeSpecifier',1,'p_typeSpecifier1','parser.py',61),
  ('typeSpecifier -> VOID','typeSpecifier',1,'p_typeSpecifier2','parser.py',66),
  ('funDeclaration -> typeSpecifier ID LPARENT params RPARENT compoundStmt','funDeclaration',6,'p_funDeclaration','parser.py',71),
  ('params -> paramList','params',1,'p_params1','parser.py',77),
  ('params -> VOID','params',1,'p_params2','parser.py',83),
  ('paramList -> paramList COMMA param','paramList',3,'p_paramList1','parser.py',89),
  ('paramList -> param','paramList',1,'p_paramList2','parser.py',94),
  ('param -> typeSpecifier ID','param',2,'p_param1','parser.py',100),
  ('param -> typeSpecifier ID LBRACKET RBRACKET','param',4,'p_param2','parser.py',106),
  ('compoundStmt -> LBRACE localDeclarations statementList RBRACE','compoundStmt',4,'p_compoundStmt','parser.py',112),
  ('localDeclarations -> localDeclarations varDeclaration','localDeclarations',2,'p_localDeclarations1','parser.py',118),
  ('localDeclarations -> empty','localDeclarations',1,'p_localDeclarations2','parser.py',124),
  ('statementList -> statementList statement','statementList',2,'p_statementList1','parser.py',130),
  ('statementList -> empty','statementList',1,'p_statementList2','parser.py',136),
  ('statement -> expressionStmt','statement',1,'p_statement1','parser.py',142),
  ('statement -> compoundStmt','statement',1,'p_statement2','parser.py',148),
  ('statement -> selectionStmt','statement',1,'p_statement3','parser.py',153),
  ('statement -> iterationStmt','statement',1,'p_statement4','parser.py',158),
  ('statement -> returnStmt','statement',1,'p_statement5','parser.py',163),
  ('expressionStmt -> expression SEMICOLON','expressionStmt',2,'p_expressionStmt1','parser.py',169),
  ('expressionStmt -> SEMICOLON','expressionStmt',1,'p_expressionStmt2','parser.py',175),
  ('selectionStmt -> IF LPARENT expression RPARENT statement','selectionStmt',5,'p_selectionStmt1','parser.py',181),
  ('selectionStmt -> IF LPARENT expression RPARENT statement ELSE statement','selectionStmt',7,'p_selectionStmt2','parser.py',186),
  ('iterationStmt -> WHILE LPARENT expression RPARENT statement','iterationStmt',5,'p_iterationStmt','parser.py',192),
  ('returnStmt -> RETURN SEMICOLON','returnStmt',2,'p_returnStmt1','parser.py',198),
  ('returnStmt -> RETURN expression SEMICOLON','returnStmt',3,'p_returnStmt2','parser.py',204),
  ('expression -> var EQ expression','expression',3,'p_expression1','parser.py',210),
  ('expression -> simpleExpression','expression',1,'p_expression2','parser.py',216),
  ('var -> ID','var',1,'p_var1','parser.py',222),
  ('var -> ID LBRACKET expression RBRACKET','var',4,'p_var2','parser.py',228),
  ('simpleExpression -> additiveExpression relop additiveExpression','simpleExpression',3,'p_simpleExpression1','parser.py',234),
  ('simpleExpression -> additiveExpression','simpleExpression',1,'p_simpleExpression2','parser.py',240),
  ('relop -> LEQ','relop',1,'p_relop1','parser.py',246),
  ('relop -> LT','relop',1,'p_relop2','parser.py',252),
  ('relop -> GT','relop',1,'p_relop3','parser.py',258),
  ('relop -> GEQ','relop',1,'p_relop4','parser.py',264),
  ('relop -> EQ','relop',1,'p_relop5','parser.py',270),
  ('relop -> NEQ','relop',1,'p_relop6','parser.py',276),
  ('additiveExpression -> additiveExpression addop term','additiveExpression',3,'p_additiveExpression1','parser.py',282),
  ('additiveExpression -> term','additiveExpression',1,'p_additiveExpression2','parser.py',288),
  ('addop -> PLUS','addop',1,'p_addop1','parser.py',294),
  ('addop -> MINUS','addop',1,'p_addop2','parser.py',300),
  ('term -> term mulop factor','term',3,'p_term1','parser.py',306),
  ('term -> factor','term',1,'p_term2','parser.py',312),
  ('mulop -> TIMES','mulop',1,'p_mulop1','parser.py',318),
  ('mulop -> DIVIDE','mulop',1,'p_mulop2','parser.py',324),
  ('factor -> factor powop exp','factor',3,'p_factor1','parser.py',330),
  ('factor -> exp','factor',1,'p_factor2','parser.py',336),
  ('powop -> POWOP1','powop',1,'p_powop1','parser.py',342),
  ('powop -> POWOP2','powop',1,'p_powop2','parser.py',348),
  ('exp -> LPARENT expression RPARENT','exp',3,'p_exp1','parser.py',354),
  ('exp -> var','exp',1,'p_exp2','parser.py',360),
  ('exp -> call','exp',1,'p_exp3','parser.py',366),
  ('exp -> NUMBER','exp',1,'p_exp4','parser.py',372),
  ('call -> ID LPARENT args RPARENT','call',4,'p_call','parser.py',378),
  ('args -> argList','args',1,'p_args1','parser.py',384),
  ('args -> empty','args',1,'p_args2','parser.py',390),
  ('argList -> argList COMMA expression','argList',3,'p_argList1','parser.py',396),
  ('argList -> expression','argList',1,'p_argList2','parser.py',402),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',408),
]