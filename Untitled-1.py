
# Función para convertir binario a hexadecimal
def binario_a_hexadecimal(binario):
    # Convertir binario a decimal
    decimal = int(binario, 2)
    # Convertir decimal a hexadecimal
    hexadecimal = hex(decimal)[2:].upper()  # Elimina el prefijo '0x' y convierte a mayúsculas
    return hexadecimal

# Función para sumar dos números binarios y convertir a hexadecimal
def suma_binaria_detallada(num1, num2):
    longitud_max = max(len(num1), len(num2))
    num1 = num1.zfill(longitud_max)
    num2 = num2.zfill(longitud_max)

    acarreo = 0
    resultado = []
    pasos = []
    pasos.append(f"{'Paso':<5} {'Bit1':<5} {'Bit2':<5} {'Acarreo':<8} {'Suma':<5} {'Resultado':<10} {'Nuevo Acarreo'}")

    for i, (bit1, bit2) in enumerate(zip(reversed(num1), reversed(num2))):
        suma_bits = int(bit1) + int(bit2) + acarreo
        resultado_bit = suma_bits % 2
        nuevo_acarreo = suma_bits // 2
        
        pasos.append(f"{i + 1:<5} {bit1:<5} {bit2:<5} {acarreo:<8} {suma_bits:<5} {resultado_bit:<10} {nuevo_acarreo}")

        resultado.append(str(resultado_bit))
        acarreo = nuevo_acarreo

    if acarreo:
        resultado.append(str(acarreo))
        pasos.append(f"{' ':<5} {' ':<5} {' ':<5} {' ':<8} {' ':<5} {' ':<10} {acarreo} (Acarreo final)")

    resultado.reverse()
    resultado_final = ''.join(resultado)

    # Convertir el resultado binario a hexadecimal
    resultado_hexadecimal = binario_a_hexadecimal(resultado_final)

    pasos.append(f"\nResultado en binario: {resultado_final}")
    pasos.append(f"Resultado en hexadecimal: {resultado_hexadecimal}")
    pasos.append("\nVerificación del resultado en decimal:")
    pasos.append(verificar_binario_a_decimal(resultado_final))

    return resultado_final, resultado_hexadecimal, pasos


def division_binaria_detallada(dividendo, divisor):
    # Convertir los números binarios a enteros
    dividendo_decimal = int(dividendo, 2)
    divisor_decimal = int(divisor, 2)

    pasos = []
    pasos.append("=== División Binaria Detallada ===")
    pasos.append(f"Dividendo: {dividendo} (decimal: {dividendo_decimal})")
    pasos.append(f"Divisor: {divisor} (decimal: {divisor_decimal})")
    
    # Verificar si el divisor es 0
    if divisor_decimal == 0:
        return None, None, ["Error: División por cero no permitida."]
    
    # Verificar si el divisor es mayor que el dividendo
    if divisor_decimal > dividendo_decimal:
        pasos.append("\n** Resultado inmediato **")
        pasos.append("El divisor es mayor que el dividendo.")
        pasos.append("Cociente: 0")
        pasos.append(f"Residuo: {dividendo} (binario) / {dividendo_decimal} (decimal)")
        return "0", dividendo, pasos
    
    # Inicializar el cociente y el residuo
    cociente_decimal = 0
    residuo = dividendo_decimal

    pasos.append("\n=== Proceso de División Binaria ===")
    pasos.append("--------------------------------------------------")
    
    # Calcular la longitud del dividendo
    longitud_dividendo = len(dividendo)

    for i in range(longitud_dividendo):
        # Desplazar el divisor
        divisor_desplazado = divisor_decimal << (longitud_dividendo - i - 1)
        pasos.append(f"Paso {i + 1}:")
        pasos.append(f"   Desplazamos el divisor {bin(divisor_decimal)[2:]} a la izquierda {longitud_dividendo - i - 1} posiciones.")
        pasos.append(f"   Divisor desplazado: {bin(divisor_desplazado)[2:]} (decimal: {divisor_desplazado})")

        if residuo >= divisor_desplazado:
            residuo -= divisor_desplazado
            cociente_decimal = (cociente_decimal << 1) | 1
            pasos.append("   - El divisor desplazado cabe en el residuo.")
            pasos.append(f"   - Restamos el divisor desplazado del residuo.")
            pasos.append(f"   - Residuo actualizado: {bin(residuo)[2:]} (decimal: {residuo})")
            pasos.append(f"   - Cociente actualizado: {bin(cociente_decimal)[2:]} (decimal: {cociente_decimal})")
        else:
            cociente_decimal = cociente_decimal << 1
            pasos.append("   - El divisor desplazado no cabe en el residuo.")
            pasos.append(f"   - Cociente actualizado: {bin(cociente_decimal)[2:]} (decimal: {cociente_decimal})")

        pasos.append("--------------------------------------------------")

    # Convertir cociente y residuo a binario
    cociente_binario = bin(cociente_decimal)[2:]
    residuo_binario = bin(residuo)[2:]

    # Calcular el residuo como porcentaje en decimal
    residuo_porcentaje = residuo % divisor_decimal

    # Añadir los resultados a los pasos
    pasos.append("\n=== Resultados Finales ===")
    pasos.append(f"Cociente: {cociente_binario} (binario) / {cociente_decimal} (decimal)")
    pasos.append(f"Residuo: {residuo_binario} (binario) = {residuo} (decimal)")
    pasos.append(f"Residuo entre {dividendo_decimal} % {divisor_decimal}: {residuo_porcentaje:.2f}")

    # Verificación de la división
    verificacion = dividendo_decimal == (cociente_decimal * divisor_decimal + residuo)
    pasos.append("\n=== Verificación de la División ===")
    pasos.append(f"Verificando: {dividendo_decimal} == ({cociente_decimal} * {divisor_decimal}) + {residuo}")
    pasos.append("Resultado de la verificación: " + ("Correcto" if verificacion else "Incorrecto"))

    return cociente_binario, residuo_binario, pasos


def multiplicacion_binaria_detallada(num1, num2):
    # Convertir los números binarios a enteros
    multiplicando = int(num1, 2)
    multiplicador = int(num2, 2)

    pasos = []
    pasos.append(f"Multiplicando: {num1} (decimal: {multiplicando})")
    pasos.append(f"Multiplicador: {num2} (decimal: {multiplicador})")
    
    resultado_decimal = 0
    desplazamiento = 0
    
    for bit in reversed(num2):
        if bit == '1':
            valor_a_sumar = multiplicando << desplazamiento
            resultado_decimal += valor_a_sumar
            pasos.append(f"Paso {desplazamiento + 1}: Multiplicando desplazado {multiplicando} << {desplazamiento} = {bin(valor_a_sumar)[2:]}")
        else:
            pasos.append(f"Paso {desplazamiento + 1}: Bit del multiplicador es 0, no se suma nada.")
        desplazamiento += 1

    # Convertir el resultado de la multiplicación a binario
    resultado_binario = bin(resultado_decimal)[2:]

    # Convertir el resultado binario a hexadecimal
    resultado_hexadecimal = binario_a_hexadecimal(resultado_binario)

    pasos.append(f"\nResultado binario: {resultado_binario}")
    pasos.append(f"Resultado en hexadecimal: {resultado_hexadecimal}")
    pasos.append(f"Resultado en decimal: {resultado_decimal}")
    
    return resultado_binario, resultado_hexadecimal, pasos


# Función para convertir binario a decimal y mostrar el cálculo
def verificar_binario_a_decimal(binario):
    decimal = 0
    detalles = []

    for i, bit in enumerate(reversed(binario)):
        valor = int(bit) * (2 ** i)
        detalles.append(f"Bit: {bit} * 2^{i} = {valor}")
        decimal += valor

    detalles.append(f"Resultado decimal: {decimal}")
    return '\n'.join(detalles)

def resta_binaria_detallada(num1, num2):
    longitud_max = max(len(num1), len(num2))
    num1 = num1.zfill(longitud_max)
    num2 = num2.zfill(longitud_max)
    
    pasos = []
    pasos.append(f"{'Paso':<5} {'Minuendo':<10} {'Sustraendo':<10} {'Préstamo':<10} {'Resultado Parcial'}")

    resultado = []
    prestamo = 0

    for i in range(longitud_max - 1, -1, -1):
        bit1 = int(num1[i])
        bit2 = int(num2[i])

        if prestamo:
            if bit1 == 0:
                bit1 = 1
                prestamo = 1
            else:
                bit1 -= 1
                prestamo = 0

        if bit1 < bit2:
            bit1 += 2
            prestamo = 1

        resultado_bit = bit1 - bit2
        resultado.append(str(resultado_bit))

        pasos.append(f"{longitud_max - i:<5} {bit1:<10} {bit2:<10} {prestamo:<10} {''.join(reversed(resultado))}")

    if prestamo:
        pasos.append("Nota: Préstamo final no utilizado, indica un número negativo en complemento a 2.")

    resultado.reverse()
    resultado_final = ''.join(resultado)

    # Convertir el resultado binario a hexadecimal
    resultado_hexadecimal = binario_a_hexadecimal(resultado_final)

    pasos.append(f"\nResultado en binario: {resultado_final}")
    pasos.append(f"Resultado en hexadecimal: {resultado_hexadecimal}")
    pasos.append("\nVerificación del resultado en decimal:")
    pasos.append(verificar_binario_a_decimal(resultado_final))

    return resultado_final, resultado_hexadecimal, pasos




def suma_varios_numeros(numeros):
    if not numeros:
        return '', []

    suma_actual = numeros[0]
    pasos_totales = [f"Iniciando con: {suma_actual}"]
    
    for num in numeros[1:]:
        suma_actual, resultado_hexadecimal, pasos = suma_binaria_detallada(suma_actual, num)
        pasos_totales.append(f"\nSuma actual: {suma_actual}")
        pasos_totales.extend(pasos)
    
    return suma_actual, pasos_totales



def resta_varios_numeros(numeros):
    if not numeros or len(numeros) < 2:
        return '', []

    resta_actual = numeros[0]
    pasos_totales = [f"Iniciando con: {resta_actual}"]
    
    for num in numeros[1:]:
        resta_actual,resultado_hexadecimal, pasos = resta_binaria_detallada(resta_actual, num)
        pasos_totales.append(f"\nResta actual: {resta_actual}")
        pasos_totales.extend(pasos)
    
    return resta_actual, pasos_totales


def multiplicacion_varios_numeros(numeros):
    if not numeros or len(numeros) < 2:
        return '', []

    multiplicacion_actual = numeros[0]
    pasos_totales = [f"Iniciando con: {multiplicacion_actual}"]
    
    for num in numeros[1:]:
        multiplicacion_actual,resultado_hexadecimal, pasos = multiplicacion_binaria_detallada(multiplicacion_actual, num)
        pasos_totales.append(f"\nMultiplicación actual: {multiplicacion_actual}")
        pasos_totales.extend(pasos)
    
    return multiplicacion_actual, pasos_totales



def elegir_numeros(numeros):
    if not numeros:
        print("No hay números disponibles para seleccionar.")
        return []

    print("\nSelecciona los números:")
    for i, num in enumerate(numeros):
        print(f"{i + 1}. {num} (decimal: {int(num, 2)})")
    
    indices = input("Ingrese los números correspondientes separados por espacio (o 'todos' para seleccionar todos): ")
    if indices.lower() == 'todos':
        return numeros
    else:
        try:
            indices = list(map(int, indices.split()))
            numeros_seleccionados = [numeros[i - 1] for i in indices]
            return numeros_seleccionados
        except (ValueError, IndexError):
            print("Entrada no válida. Inténtelo de nuevo.")
            return elegir_numeros(numeros)


def suma_binaria(numeros_8, numeros_16, numeros_24, numeros_personalizados):
    print("\nProcedimiento de operaciones cruzadas:")

    while True:
        print("\nSelecciona una opción:")
        print("1. Sumar Bits")
        print("2. Restar Bits")
        print("3. Multiplicar Bits")
        print("4. Dividir Bits")
        print("5. Salir")
        opcion = input("Ingrese su elección (1-5): ")

        if opcion == '5':
            break

        # Obtener números para realizar la operación
        todos_numeros = numeros_8 + numeros_16 + numeros_24 + numeros_personalizados
        if not todos_numeros:
            print("No hay números disponibles.")
            continue
        numeros_seleccionados = elegir_numeros(todos_numeros)

        if opcion == '1':
            resultado, pasos = suma_varios_numeros(numeros_seleccionados)
        elif opcion == '2':
            resultado, pasos = resta_varios_numeros(numeros_seleccionados)
        elif opcion == '3':
            resultado, pasos = multiplicacion_varios_numeros(numeros_seleccionados)
        elif opcion == '4' and len(numeros_seleccionados) == 2:
            resultado, residuo, pasos = division_binaria_detallada(numeros_seleccionados[0], numeros_seleccionados[1])
            print(f"Residuo: {residuo}")
        else:
            print("Opción no válida o no se puede realizar la operación con múltiples números para la división.")
            continue

        resultado_decimal = int(resultado, 2)
        print(f"\nResultado binario: {resultado} (decimal: {resultado_decimal})")
        print("Detalles de la operación:")
        for paso in pasos:
            print(paso)
        
        # Preguntar si desea realizar otra operación
        repetir = input("\n¿Desea realizar otra operación? (s/n): ").lower()
        if repetir != 's':
            break

# Función para obtener un número binario
def obtener_numero_binario(bits, cantidad):
    numeros_binarios = []
    for i in range(cantidad):
        while True:
            cadena_binaria = input(f"Ingrese el número binario {i + 1} ({bits} bits): ")
            if len(cadena_binaria) != bits or not all(bit in '01' for bit in cadena_binaria):
                print(f"Número binario no válido. Debe tener exactamente {bits} bits y solo contener 0 o 1.")
            else:
                numeros_binarios.append(cadena_binaria)
                break
    return numeros_binarios

def main():
      while True:
        cantidades = {}
        cantidades[8] = int(input("Ingrese la cantidad de números para 8 bits: "))
        cantidades[16] = int(input("Ingrese la cantidad de números para 16 bits: "))
        cantidades[24] = int(input("Ingrese la cantidad de números para 24 bits: "))

        # Pedir cantidad y tamaño personalizado de bits
        largo_personalizado = int(input("Ingrese el número de bits personalizados (n): "))
        cantidad_personalizada = int(input(f"Ingrese la cantidad de números binarios de {largo_personalizado} bits: "))

        # Obtener números binarios para cada tamaño
        numeros_8 = obtener_numero_binario(8, cantidades[8])
        numeros_16 = obtener_numero_binario(16, cantidades[16])
        numeros_24 = obtener_numero_binario(24, cantidades[24])
        numeros_personalizados = obtener_numero_binario(largo_personalizado, cantidad_personalizada)

        # Llamar a la función para realizar operaciones
        suma_binaria(numeros_8, numeros_16, numeros_24, numeros_personalizados)

        # Preguntar si desea repetir la calculadora
        repetir = input("\n¿Desea volver a iniciar la calculadora? (s/n): ").lower()
        if repetir != 's':
            print("¡Gracias por usar la calculadora!")
            break


# Ejecutar el programa
if __name__ == "__main__":
    main()
