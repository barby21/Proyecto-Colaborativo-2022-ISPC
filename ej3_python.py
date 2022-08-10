#creo la lista perro que se corresponde con los datos de un perro de nuestra base de datos (Id_Perro,nombre,fecha de nacimiento, sexo y dni del dueño)

perro = [13, "Puppy", "12/12/2012", "Macho", 123]

print (perro)

print ("se realiza modificacion de fecha de nacimiento del animal y el dni del dueño")

for x in range (len(perro)):
    if perro[x] == "12/12/2012" :
        perro[x] = "13/12/2012"

for x in range (len(perro)):
    if perro[x] == 123 :
        perro[x] = 28957346  


print (perro)
