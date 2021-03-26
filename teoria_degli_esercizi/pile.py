def push_(pila, elemento):
    pila.append(elemento)
    
def pop_(pila):
    return pila.pop()

def main():
    stack = ["a", "b", "c", "d"]
    push_(stack, "z")
    print(stack)
    print(pop_(stack))
    print(stack)


if __name__ == "__main__":
    main()