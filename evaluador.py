import math
ambiente = {} 

def setAmbiente(AuxAmbiente):
    global ambiente
    ambiente = AuxAmbiente

def evalue(exp):
    global ambiente
    try:
        if not isinstance(exp, list):
            return valor(exp, ambiente)
        elif len(exp) == 1:
            return exp[0]
        elif exp[0] == '+':
            return evalue(exp[1]) + evalue(exp[2])
        elif exp[0] == '-':
            return evalue(exp[1]) - evalue(exp[2])
        elif exp[0] == '*':
            return evalue(exp[1]) * evalue(exp[2])
        elif exp[0] == '/':
            return evalue(exp[1]) / evalue(exp[2])
        elif exp[0] == '^':
            return evalue(exp[1]) ** evalue(exp[2])
        elif exp[0] == '=':
            if (evalue(exp[2])  != None and exp[1] != "pi" and exp[1] != "e"):
                ambiente[exp[1]] = evalue(exp[2])
                return ambiente[exp[1]]
            else:
                return ("\nError 01: Failed assignment")
        elif exp[0] == 'cos':
            return math.cos( evalue(exp[1]) )
        elif exp[0] == 'tan':
            return math.tan( evalue(exp[1]) )
        elif exp[0] == 'sin':
            return math.sin( evalue(exp[1]) )
        elif exp[0] == 'ln':
            return math.log( evalue(exp[1]) )
        elif exp[0] == 'exp':
            return math.exp( evalue(exp[1]) )
    except:
        print ("\nError 02: Calculation error")

def valor(exp, vars):
  if exp in vars:
    return float(vars[exp]) 
  else:
    try:
        return float(exp)
    except:
        print ("\nError 03: Undeclared variable")
