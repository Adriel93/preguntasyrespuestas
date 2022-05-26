#Mi testing
print("Preguntas \n")
calvinista = 1
arminiano = 1

print("La salvacion se pierde? \n")
print("1. La salvacion no se pierde")
print("2. La salvacion si se pierde \n")

salvacion = int(input("Tu respuesta: "))
if salvacion == 1:
    calvinista += 1
elif salvacion == 2:
    arminiano +=1

if arminiano > calvinista:
    print("Segun tu resultado eres: arminiano")
else:
        print("Segun tu resultado eres: calvinista")



#print(arminiano, calvinista)
print("Fin")

