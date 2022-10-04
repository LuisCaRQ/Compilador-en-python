import Tokenizador
import AnalizadorSintactico as x
import evaluador


def main():
    exit = False
    simbolTable = []
    ambiente = { "pi": 3.14 , "e" : 2.71 }

    while (not exit):
        print("------------------------------------------------------------------------------")
        exit , simbolTable = Tokenizador.start()
        x.setSimboleTable(simbolTable)
        x.setAmbiente(ambiente)
        
        evaluador.setAmbiente(ambiente)
        if (not exit):
            arbol = x.asignacion()
            
            print("\nSemantic tree: ")
            print(arbol)
            result = evaluador.evalue(arbol) 
            if result != None:
                print("\nResult: " + str(result))
        print("\nEnvironment: ")
        print(ambiente)
        print("\n")
       
if __name__ == "__main__":
    main()
