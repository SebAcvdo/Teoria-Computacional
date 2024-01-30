from random import randint


def main(): 
	print(" ==== MÁQUINA DE TURING ===")
	print("Seleccione un modo")
	print("1.- Automático\n2.- Manual")
	if int(input()) == 1:
		n = randint(0,20)
		m = randint(0,20)
		cadena = "*" + n*"|" + "*" + m*"|" +"*"
	else:
		print("Ingrese la cadena")
		cadena = input()
		while(1):
			if len(cadena) > 50:
				print("Cadena inválida")
			else:
				break
	print("Cadena Original: ",cadena)
	automata(list(cadena))

	
def automata(cadena):
	tape = open("tape.txt", "w")
	Right = 1
	Left = -1
	IDiS = open("IDS.txt","w")

	estado =1
	i = 0
	while(1):
		j = i
		preves = estado
		if i<len(cadena): prevchar = cadena[i]
		else: prevchar = "-"
		tape.write((i)*" "+"v\n")
		tape.write(''.join(cadena)+"\t\tq="+str(estado)+"\n\n\n")
		if estado == 1:
			if cadena[i] == "*":
				cadena[i] = "X"
				i += Right
				estado = 2
			else: 
				print("Cadena Inválida")
				exit(0)
				
		elif estado == 2:
			if cadena[i] == "*":
				cadena[i] = "*"
				i += Right
				estado = 3
			elif cadena[i] == "|":
				cadena[i] = "|"
				i += Right
				estado = 2
			else: 
				print("Cadena Inválida")
				exit(0)
		
		elif estado == 3:
			if cadena[i] == "*":
				cadena[i] = "X"
				i += Left
				estado = 4
			elif cadena[i] == "|":
				cadena[i] = "|"
				i += Right
				estado = 3
			else: 
				print("Cadena Inválida")
				exit(0)
		
		elif estado == 4:
			if cadena[i] == "*":
				cadena[i] = "*"
				i += Left
				estado = 4
			elif cadena[i] == "|":
				cadena[i] = "a"
				i += Right
				estado = 5
			elif cadena[i] == "X":
				cadena[i] = "X"
				i += Right
				estado = 7
			else: 
				print("Cadena Inválida")
				exit(0)

		elif estado == 5:
			if i==len(cadena):
				cadena.append("|")
				i += Left
				estado = 6
			elif cadena[i] == "*":
				cadena[i] = "*"
				i += Right
				estado = 5
			elif cadena[i] == "|":
				cadena[i] = "|"
				i += Right
				estado = 5
			elif cadena[i] == "X":
				cadena[i] = "X"
				i += Right
				estado = 5
			else: 
				print("Cadena Inválida")
				exit(0)

		elif estado == 6:
			if cadena[i] == "*":
				cadena[i] = "*"
				i += Left
				estado = 6
			elif cadena[i] == "|":
				cadena[i] = "|"
				i += Left
				estado = 6
			elif cadena[i] == "a":
				cadena[i] = "|"
				i += Left
				estado = 4
			elif cadena[i] == "X":
				cadena[i] = "X"
				i += Left
				estado = 6
			else: 
				print("Cadena Inválida")
				exit(0)

		elif estado == 7:
			if cadena[i] == "*":
				cadena[i] = "*"
				i += Right
				estado = 8
			elif cadena[i] == "|":
				cadena[i] = "|"
				i += Right
				estado = 7
			else: 
				print("Cadena Inválida")
				exit(0)

		elif estado == 8:
			if i == len(cadena):
				cadena.append("*")
				i += Left
				estado = 9
			elif cadena[i] == "|":
				cadena[i] = "|"
				i += Right
				estado = 8
			elif cadena[i] == "X":
				cadena[i] = "*"
				i += Right
				estado = 8
			else: 
				print("Cadena Inválida")
				exit(0)

		elif estado == 9:
			if cadena[i] == "*":
				cadena[i] = "*"
				i += Left
				estado = 9
			elif cadena[i] == "|":
				cadena[i] = "|"
				i += Left
				estado = 9
			elif cadena[i] == "X":
				cadena[i] = "*"
				i = i
				estado = 10
			else: 
				print("Cadena Inválida")
				exit(0)
		elif estado == 10:
			print("Ejecución de la cadena terminada.\nCadena Final:", end="")
			print(''.join(cadena))
			exit(0)

		if j < i: #R
			IDiS.write("q"+str(preves)+", "+prevchar+", "+cadena[j]+", R, q"+str(estado)+"\n")
		elif j>i: #L
			IDiS.write("q"+str(preves)+", "+prevchar+", "+cadena[j]+", L, q"+str(estado)+"\n")
	tape.close()
	IDiS.close()
main()