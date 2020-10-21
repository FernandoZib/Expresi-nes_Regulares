# coding: utf-8
# Your code here!
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
print ("¡Bienvenido !, Elija una opcion de la lista para ver en función el uso de las EXPRECIONES REGULARES:\n\n1.- Todas las palabras que tengan una longitud de 7 o más letras."
"\n2.- Expresiones que NO finalicen con una vocal.\n3.- Las palabras que inicien con “M” donde la segunda letra no sea vocal.\n4.- Expresiones encerradas entre comillas.\n"
"5.- Ip’s.\n6.- Horas.\n7.- Teléfonos.\n8.- Correos electrónicos.\n9.- Url's\n10.- Código postal.")


Opcion = int(input("Tu respuesta: \n"))
if Opcion == 1:
    regex = r"[a-zA-Z]{7,}"
elif Opcion == 2:
    regex = r"\w+[b-df-hj-np-tv-z]\b"
elif Opcion == 3:
    regex = r"\b[mM][^aA-uU]"    
elif Opcion == 4:
    regex = r"(\"[\w\s]+\")"
elif Opcion == 5:
    regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
elif Opcion == 6:
    regex = r"^([01]?[0-9]|2[0-3]):[0-5][0-9]$"
elif Opcion == 7:
    regex = r"(\+34|0034|34)?[ -]*(8|9)[ -]*([0-9][ -]*){9}"
elif Opcion == 8:
    regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
elif Opcion == 9:
    regex = r"^https?:\/\/[\w\-]+(\.[\w\-]+)+[/#?]?.*$"
elif Opcion == 10:
    regex = r"\d{5,5}"
else: print("Intente nuevamente")
        

                    #TEXTO DE PRUEBA#

test_str = ("En el área de la programación las expresiones regulares son un método por medio del cual se pueden realizar búsquedas dentro de cadenas de caracteres. Sin importar la amplitud de la búsqueda requerida de un patrón definido de caracteres, las expresiones regulares proporcionan una solución práctica al problema. Adicionalmente, un uso derivado de la búsqueda de patrones es la validación de un formato específico en una cadena de caracteres dada, como por ejemplo fechas o identificadores.\n\n"
	"Para poder utilizar las \"expresiones regulares\" al programar es necesario tener acceso a un motor de búsqueda con la capacidad de utilizarlas. Es posible clasificar los motores disponibles en dos tipos según su uso: motores para el programador y motores para el usuario final.\n\n"
	"Correo:\n"
	"bryanfernando@gmail.com\n\n"
	"Código Postal:\n"
	"77300\n\n"
	"Número de teléfono:\n"
	"9841195737\n\n"
	"Nacionalidad:\n"
	"Mx (Mexicana)\n\n"
	"IP:\n"
	"255.255.255.255\n\n"
	"URL:\n"
	"http://www.algunlugar.com\n\n"
	"Hora:\n"
	"3:30\n")
	

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.