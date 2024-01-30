#AFN a AFD (WebEbay)

from atexit import register
from tkinter import*

leer = open("./input.txt", "r")
registro = open("./registro.txt", "w")
posicion = open("./posicion.txt", "w")
prevstate = 0
auxweb1 = 0
auxweb2 = 0
web = [ ] #
website = [ ] #
webpage = [ ] #
website = [ ] #
webmaster = [ ] #
site = [ ] #
page = [ ] #
ebay = [ ] #


contador = 0
estado = 0

texto = leer.read()

for letra in texto.lower():

    if letra == "\n": letra = "\"n"
    contador += 1

    if (estado == 0):
        
        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 2
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        else:
            estado = 0

        registro.write("(q0,\""+letra+"\",q"+str(estado)+")\n")
        continue

    if (estado == 1):

        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 5
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        else:
            estado = 0

        registro.write("(q1,\""+letra+"\",q"+str(estado)+")\n")
        continue

    if (estado == 2):

        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 2
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        elif(letra == "b"):
            estado = 6
        else:
            estado = 0

        registro.write("(q2,\""+letra+"\",q"+str(estado)+")\n")
        continue

    if (estado == 3):
        auxweb1 = 0
        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 2
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        elif(letra == "a"):
            estado = 7
            if prevstate == 9:
                #print("prev = ",prevstate)
                auxweb1 = 1
            auxweb1 += 1
            prevstate = 0
        else:
            estado = 0
        registro.write("(q3,\""+letra+"\",q"+str(estado)+")\n")
        continue


    if (estado == 4):
        auxweb2 = 0
        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 2
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        elif(letra == "i"):
            estado = 8
            if prevstate == 9:
                auxweb2 = 1
            auxweb2 += 1
            prevstate = 0
        else:
            estado = 0

        registro.write("(q4,\""+letra+"\",q"+str(estado)+")\n")
        continue


    if (estado == 5):
        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 2
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        elif(letra == "b"):
            estado = 9
        else:
            estado = 0

        registro.write("(q5,\""+letra+"\",q"+str(estado)+")\n")
        continue


    if (estado == 6):
        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 2
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        elif(letra == "a"):
            estado = 10
        elif(letra == "i"):
            estado = 8
        else:
            estado = 0

        registro.write("(q6,\""+letra+"\",q"+str(estado)+")\n")
        continue

    if (estado == 7):
        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 2
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        elif(letra == "g"):
            estado = 11
            auxweb1 += 1
        else:
            estado = 0

        registro.write("(q7,\""+letra+"\",q"+str(estado)+")\n")
        continue

    if (estado == 8):
        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 2
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        elif(letra == "t"):
            estado = 12
            auxweb2 += 1
        else:
            estado = 0

        registro.write("(q8,\""+letra+"\",q"+str(estado)+")\n")
        continue

    if (estado == 9): #web        
        web.append(contador-3)

        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 2
        elif (letra == "p"):
            prevstate = estado
            estado = 3
        elif (letra == "s"):
            prevstate = estado
            estado = 4
        elif(letra == "m"):
            estado = 13
        else:
            estado = 0

        registro.write("(q9,\""+letra+"\",q"+str(estado)+")\n")
        continue

    if (estado == 10):
        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 2
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        elif(letra == "y"):
            estado = 14
        else:
            estado = 0

        registro.write("(q10,\""+letra+"\",q"+str(estado)+")\n")
        continue

    if (estado == 11):
        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 15
            auxweb1 += 1
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        else:
            estado = 0

        registro.write("(q11,\""+letra+"\",q"+str(estado)+")\n")
        continue

    if (estado == 12):

        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 16
            auxweb2 += 1
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        else:
            estado = 0

        registro.write("(q12,\""+letra+"\",q"+str(estado)+")\n")
        continue

    if (estado == 13):
        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 2
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        elif(letra == "a"):
            estado = 17
        else:
            estado = 0

        registro.write("(q13,\""+letra+"\",q"+str(estado)+")\n")
        continue

    if (estado == 14): #ebay

        ebay.append(contador-4)

        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 2
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        else:
            estado = 0

        registro.write("(q14,\""+letra+"\",q"+str(estado)+")\n")
        continue

    if (estado == 15): #page/webpage

        if auxweb1 == 4:
            webpage.append(contador-7)
        page.append(contador-4)

        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 2
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        elif(letra == "b"):
            estado = 6
        else:
            estado = 0
        
        registro.write("(q15,\""+letra+"\",q"+str(estado)+")\n")
        auxweb1 = 0
        continue

    if (estado == 16): #site/website
        if auxweb2 == 4:
            website.append(contador-7)
        site.append(contador-4)

        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 2
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        elif(letra == "b"):
            estado = 6
        else:
            estado = 0

        registro.write("(q16,\""+letra+"\",q"+str(estado)+")\n")
        auxweb2 = 0
        continue

    if (estado == 17):
        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 2
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 18
        else:
            estado = 0

        registro.write("(q17,\""+letra+"\",q"+str(estado)+")\n")
        continue

    if (estado == 18):
        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 2
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        elif(letra == "t"):
            estado = 19
        elif(letra == "i"):
            estado = 8
        else:
            estado = 0

        registro.write("(q18,\""+letra+"\",q"+str(estado)+")\n")
        continue

    if (estado == 19):
        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 20
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        else:
            estado = 0

        registro.write("(q19,\""+letra+"\",q"+str(estado)+")\n")
        continue

    if (estado == 20):
        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 2
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        elif(letra == "b"):
            estado = 6
        elif(letra == "r"):
            estado = 21
        else:
            estado = 0

        registro.write("(q20,\""+letra+"\",q"+str(estado)+")\n")
        continue

    if (estado == 21): #webmaster
        if (letra == "w"):
            estado = 1
        elif (letra == "e"):
            estado = 2
        elif (letra == "p"):
            estado = 3
        elif (letra == "s"):
            estado = 4
        else:
            estado = 0
        webmaster.append(contador-9)
        registro.write("(q21,\""+letra+"\",q"+str(estado)+")\n")
        continue

posicion.write("                REGISTRO DE APARICIONES\n")
posicion.write("Web = "+ str(len(web))+"\tPosiciones = "+str(web)+"\n")
posicion.write("ebay = "+ str(len(ebay))+"\tPosiciones = "+str(ebay)+"\n")
posicion.write("page = "+ str(len(page))+"\tPosiciones = "+str(page)+"\n")
posicion.write("site = "+ str(len(site))+"\tPosiciones = "+str(site)+"\n")
posicion.write("webpage = "+ str(len(webpage))+"\tPosiciones = "+str(webpage)+"\n")
posicion.write("Website = "+ str(len(website))+"\tPosiciones = "+str(website)+"\n")
posicion.write("Webmaster = "+ str(len(webmaster))+"\tPosiciones = "+str(webmaster)+"\n")

print("TERMINADO -> Checa los archivos generados")

leer.close()
posicion.close()
registro.close()