inputText = ""
simbolTable = []

def skipSpace():
    global inputText
    while(inputText != "" and inputText[0] == " "):
        inputText = inputText[1:]
        
def getSimbolTable():
    global inputText
    currentToken = ""
    
    if( inputText == ""):
        return ""

    skipSpace()

    if ( inputText[0] == "=" or inputText[0] == " " or inputText[0] == "+"  or inputText[0] == "-" or inputText[0] == "*"  or inputText[0] == "/" 
                            or inputText[0] == "(" or inputText[0] == ")" or inputText[0] == "^"):
        currentToken = inputText[0]
        inputText = inputText[1:]
        return currentToken

    while( not(inputText == "" or inputText[0] == "=" or inputText[0] == " " or inputText[0] == "+"  
            or inputText[0] == "-" or inputText[0] == "*"  or inputText[0] == "/" 
            or inputText[0] == "(" or inputText[0] == ")" or inputText[0] == "^")): 
        
        currentToken = currentToken + inputText[0]
        inputText = inputText[1:]
    
    return currentToken



def start():
    global inputText, simbolTable
    simbolTable = []
    exit = False
    inputText = input("\nWrite a numerical expression (Type exit to quit): ")
    inputText = inputText.strip()
    while(inputText != ""):
        token = getSimbolTable()
        if(token !="exit"):
            simbolTable.append(token)
        else:
            exit = True
            break
    return exit , simbolTable

