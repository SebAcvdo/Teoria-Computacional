from random import randint

from numpy import append

def main():
    print("|----------- PUSHDOWN AUTOMATA ----------|")
    
    print("1. Automático\n2. Manual")
    opc = int(input())

    if(opc == 1):
        if 0<randint(0,10)<9:
            aux = randint(0,5)
            string = " "+("0"* aux)+("1"* aux)+" "
        else: 
            string = " "+("0"* randint(0,5))+("1"* randint(0,5)+" ")        
        
    elif(opc == 2):

        print("Ingrese la cadena a evaluar")
        string = " "+input()+" "

    else:
        print("Opción no válida")
        string = ""

    if(pda(string) == 1):
        print("=============== CADENA VALIDADA ===================")
    else:
        print("!!!!!!!!!!!!!!! CADENA INVALIDADA !!!!!!!!!!!!!!!!")

def pda(string):
    file = open("pda.txt","w")
    file.write("\nCadena ==> "+ string)
    print(string)
    stack = []
    estado = 0
    for char in string:
        top = len(stack) - 1
        file.write("\nChar = "+char)
        print("char =" ,char)
        file.write("\nEstado = "+str(estado))
        print("estado =",estado)
        file.write("\n"+str(stack))
        print(stack)
        file.write("\n/----------------------/")
        print("/----------------------/")
        if estado ==0 :
            stack.append("$")
            estado = 1
            continue
        if estado == 1:
            if char == "0":
                stack.append(char)
                estado = 1
            if char == "1" and stack[top] == "0":
                stack.pop(len(stack)-1)
                estado = 2
            continue

        if estado == 2:
            if char == "1" and stack[top] == "0":
                stack.pop(len(stack)-1)
                estado = 2
            if char == " " and stack[top] == "$":
                stack.pop(len(stack)-1)
                estado = 3
                stack.append("$")
                return 1
            continue



main()