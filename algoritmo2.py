cadena=input("Introduzca un texto: ")
texto = cadena.replace(" ","")
palindromo = cadena.replace(" ","")[::-1]
if palindromo==texto:
    print(cadena+ " Es un palindromo")
else:
    print(cadena + "No es un palindromo")