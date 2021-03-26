def push_(pila, elemento):
    pila.append(elemento)
    
def pop_(pila):
    return pila.pop()

def main():
    parentesi = input("inserisci una stringa: ")
    pila = []
    giusto = False
    
    for elemento in parentesi:
        if(elemento == "(" or elemento == "[" or elemento == "{"):
            push_(pila, elemento)

    print(pila)
    
    for el in parentesi:
        if (len(pila)!= 0 and giusto):
            if(el == ")"):
                print("bri")
                if ("(" == pop_(pila)):
                    giusto = True
                    print("bri")
                else:
                    giusto = False
                    
            if(el == "]"):
                if ("[" == pop_(pila)):
                    giusto = True
                else:
                    giusto = False

            if(elemento == "}"):
                if ("{" == pop_(pila)):
                    giusto = True
                else:
                    giusto = False
        
        
    
    if (giusto):
        print("corretta!")
    else:
        print("sbagliata")


        

if __name__ == "__main__":
    main()