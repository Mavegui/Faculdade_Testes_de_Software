def maximo(x, y):
    if x > y:
        return x
    else:
        return y
  
def main():    
    while True:
        try:
            print("---------------------------------------------")
            x = int(input("Insira o primeiro valor: "))
            y = int(input("Insira o segundo valor: "))
            print("---------------------------------------------")
            
            break
            
        except ValueError:
            
            print("*********************************************")
            print("** Erro: Insira valores numéricos válidos! **")
            print("*********************************************")
    
    resultado = maximo(x, y)
    print("O número {} é o maior".format(resultado))
    return x, y
    
if __name__ == "__main__":
    main()