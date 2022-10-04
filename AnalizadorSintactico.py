simbolTable = []
ambiente = {}

def getToken():
    global simbolTable
    if simbolTable != []:
        token = simbolTable[0]
        simbolTable = simbolTable[1:]
        return token
    return -1

def retToken(token):
    global simbolTable
    simbolTable = [token] + simbolTable
    return simbolTable

def setAmbiente(AuxAmbiente):
    global ambiente
    ambiente = AuxAmbiente

def setSimboleTable(AuxSimboleTable):
    global simbolTable
    simbolTable = AuxSimboleTable

# asig ::= var = exp | exp
def asignacion():
    global simbolTable
    var = getToken()
    op = getToken()
    if op == '=':
        return ['=', var, exp()]
    else:
        retToken(op)
        retToken(var)
        return exp()


# exp ::= exp + term | exp - term | term
def exp():
    global simbolTable
    val = term()
    tok = getToken()
    while tok == '+' or tok == '-':
        if tok == '+':
            val = ['+', val, term()]
        elif tok == '-':
            val = ['-', val, term()]
        tok = getToken()
    retToken(tok)
    return val

# term ::= term * fact | term / fact | fact
def term():
    global simbolTable
    val = fact()
    tok = getToken()
    while tok == '*' or tok == '/':
        if tok == '*':
            val = ['*', val, fact()]
        elif tok == '/':
            val = ['/', val, fact()]
        tok = getToken()
    
    retToken(tok)
    return val

# fact ::= (exp) | numero 
def fact():
    global simbolTable
    val = valor()
    tok = getToken()
    while tok == '^':
        val = ['^', val, fact()]
        tok = getToken()
    
    retToken(tok)
    return val

# fact ::= (exp) | numero 
def valor():
    global simbolTable
    tok = getToken()
    
    if tok == '(':
        val = exp()
        tok = getToken()
        if tok != ')':
            return -1
        else:
            return val

    if tok == "cos" or tok == "sin" or tok == "exp" or tok ==  "ln" or tok == "tan":
        fun = tok
        tok = getToken()
        if tok == '(':
            val = exp()
            val = [fun, val] 
            tok = getToken()
            if tok != ')':
                return -1
            else:
                return val

    if isinstance( tok, int):
        return float(tok)
    else:
        return tok

