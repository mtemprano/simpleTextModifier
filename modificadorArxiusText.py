from os import listdir
from os.path import isfile, join


def readFiles(targetPath):
    onlyFilesList = []
    print("Iniciar lectura d'arxius...")

    filesInDirectory = listdir(targetPath)
    for f in filesInDirectory:
        if isfile(join(targetPath, f)):
            onlyFilesList.append(join(targetPath, f))

    content = []
    for path in onlyFilesList:
        with open(path) as f:
            content.extend(f.readlines())

    print("Lectura d'arxius completada amb èxit")
    print("Arxius llegits: ", onlyFilesList)
    return content


def modifyLines(lines, charsToSearch, overWriteWith):
    parsedLines = []
    for line in lines:
        parsedLines.append(line.replace(charsToSearch, overWriteWith))

    return parsedLines


# Iniciar programa

# Especifica el path de la carpeta on hi ha els csv
targetPath = ""

# Llegeix tots els arxius i retorna una llista de totes les linies
totalLines = readFiles(targetPath)

# Mostra a l'usuari les linies sense modificar
print("LINIES A MODIFICAR -----------------------------------------------")
print(*totalLines)
print("-----------------------------------------------")

multipleChanges = True
modifiedLines = totalLines

while(multipleChanges):
    # Demana a l'usuari els caràcters a buscar i substituir
    charsToSearch = input("Quins caràcters vols buscar?: ")
    overWriteWith = input("Per a quins caràcters vols substituir-los?: ")

    # Modifica els caràcters
    modifiedLines = modifyLines(modifiedLines, charsToSearch, overWriteWith)

    # Mostra a l'usuari les linies modificades
    print("LINIES MODIFICADES -----------------------------------------------")
    print(*modifiedLines)
    print("-----------------------------------------------")

    userMultipleChanges = input("Vols fer algun canvi més? y/n: ")
    userMultipleChanges = userMultipleChanges.lower()
    if userMultipleChanges != 'y':
        multipleChanges = False

# Demanar confirmació a l'usuari
userInput = input(
    "Es crearà un arxiu nou amb les dades modificades, et sembla be? y/n: ")
userInput = userInput.lower()

# Crear un nou arxiu amb les linies modificades
if (userInput == 'y'):
    with open(join(targetPath, "parsedFile.csv"), "x") as f:
        f.writelines(modifiedLines)
        print("Arxiu creat correctament")
else:
    print("Arxiu NO creat")
