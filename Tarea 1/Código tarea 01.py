op = 0

def convertirbases(basem, basen, numero):
    alfabeto ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numfinalentero = ""
    numfinalfraccion = ""
    resultadoentero = 0
    resultadofraccion = 0
    numeroentero, punto, numerofraccion = numero.partition(".")
    revision = numeroentero + numerofraccion

    validacion = True


    for simbolo in revision:

        if simbolo not in alfabeto:
            print("Error: El número contiene símbolos no registrados.")
            validacion = False
            break

        valor = alfabeto.index(simbolo) 

        if valor >= basem:
            print("Error: El número contiene símbolos inválidos para la base original.")
            validacion = False
            break

        if validacion:
            elevado = len(numeroentero) 
            for simbolo in numeroentero:
                valor = alfabeto.index(simbolo)
                elevado = elevado - 1 
                potencia = valor*basem**(elevado)
                resultadoentero = resultadoentero + potencia

            elevado = 0

            for simbolo in numerofraccion:      
                valor = alfabeto.index(simbolo)
                elevado = elevado + 1
                potencia = valor*basem**(-elevado)
                resultadofraccion = resultadofraccion + potencia

            while resultadoentero > 0:          
                residuo = resultadoentero % basen
                resultadoentero = resultadoentero // basen
                simbolo = alfabeto[residuo]
                numfinalentero = simbolo + numfinalentero

            for i in range(5):        
                resultadofraccion = float(resultadofraccion) * basen
                entero, punto, fraccion = str(resultadofraccion).partition(".")
                simbolo = alfabeto[int(entero)]
                resultadofraccion = "0." + fraccion
                numfinalfraccion = numfinalfraccion + simbolo

            return numfinalentero, numfinalfraccion

def a2(binario, signo):
    binario = binario.zfill(5)
    
    if signo == False:        
        binarioinv = binario[::-1]
        binc = ""
        volteo = True
        
        for simbolo in binarioinv:
            if volteo == True:
                if simbolo == "1":
                    volteo = False
                binc = binc + simbolo
            else:
                if simbolo == "0":
                    binc = binc + "1"
                else:
                    binc = binc + "0"

        binario = binc[::-1]
        return binario
    else:
        binario = binario
        return binario

def suma_un_bit(bita, bitb, acarreo):
    suma_con_acarreo = int(bita) + int(bitb) + acarreo
    suma = suma_con_acarreo % 2
    if suma_con_acarreo >= 2:
        acarreo = 1
    else:
        acarreo = 0
    return str(suma), acarreo

while True:
    print("\nBienvenido al programa de conversión de bases y suma de binarios.\n")
    print("Seleccione una opción:")
    print("1 = Conversion de base a base")
    print("2 = Suma de binarios")
    print("3 = Salir")
    op = int(input("Su opción: "))
    if op == 1:
        basem = int(input("Ingrese la base del número original: "))
        basen = int(input("Ingrese la base del número nuevo: "))
        numero = input("Ingrese el número a convertir: ")

        numfinalentero, numfinalfraccion = convertirbases(basem, basen, numero)

        print(f"El número {numero} en base {basem} es igual a {numfinalentero}.{numfinalfraccion} en base {basen}.\n")

    elif op == 2:
        numero1 = int(input("Ingrese su primer numero: "))
        numero2 = int(input("Ingrese su segundo numero: "))

        validacion = True

        if(numero1 <= -32 or numero1 >= 31 ):
            print("Error: Los números ingresados están fuera del rango permitido.")
            validacion = False
        elif(numero2 <= -32 or numero2 >= 31 ):
            print("Error: Los números ingresados están fuera del rango permitido.")
            validacion = False

        if validacion:
            if numero1 < 0:
                signo1 = False
                numero1 = abs(numero1)
            else: 
                signo1 = True
            
            if numero2 < 0:
                signo2 = False
                numero2 = abs(numero2)
            else: 
                signo2 = True

            numfinalentero1, numfinalfraccion1 = convertirbases(10, 2, str(numero1))
            numfinalentero2, numfinalfraccion2 = convertirbases(10, 2, str(numero2))

            binario1 = numfinalentero1 
            binario2 = numfinalentero2

            binario1 = a2(binario1, signo1)
            binario2 = a2(binario2, signo2)
            
            binario1v = binario1[::-1]
            binario2v = binario2[::-1]
            binariofinal = ""
            acarreo = 0
            
            for simbolo1, simbolo2 in zip(binario1v, binario2v):
                resultado, acarreo = suma_un_bit(simbolo1, simbolo2, acarreo)
                binariofinal = binariofinal + resultado
                
            binariofinal = binariofinal[::-1]
            
            overflow = False
            if signo1 == True and signo2 == True:
                if acarreo == 1:
                    overflow = True
            elif signo1 == False and signo2 == False:
                if acarreo == 0 or binariofinal == "00000":
                    overflow = True
            
            if overflow:
                print("Error: Se ha producido un desbordamiento (overflow) en la suma de los números binarios.\n")
            else:
                if numero1 > numero2:
                    if signo1 == False:
                        binariofinal = a2(binariofinal, False)
                        binariofinal = "1" + binariofinal
                    else:
                        binariofinal = a2(binariofinal, True)
                        binariofinal = "0" + binariofinal
                elif numero1 < numero2:
                    if signo2 == False:
                        binariofinal = a2(binariofinal, False)
                        binariofinal = "1" + binariofinal
                    else:
                        binariofinal = a2(binariofinal, True)
                        binariofinal = "0" + binariofinal
                else: 
                    if signo1 == False:
                        binariofinal = a2(binariofinal, False)
                        binariofinal = "1" + binariofinal
                    else:
                        binariofinal = a2(binariofinal, True)
                        binariofinal = "0" + binariofinal
                    
                decimal_resultado, _ = convertirbases(2, 10, binariofinal[1:])  
                        
                if binariofinal[0] == "1":
                    decimal_resultado = "-" + decimal_resultado       
                            
                print(f"\nEl resultado de la suma es: {binariofinal} en binario y {decimal_resultado} en decimal\n")   

    elif op == 3:
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.\n")
        break