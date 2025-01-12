def encontrar_mayor(lista):
    if not lista:  # Verificar que la lista no esté vacía
        raise ValueError("La lista no puede estar vacía")

    # Verificar que todos los elementos sean de tipo int
    for num in lista:
        if type(num) is not int:
            raise TypeError("Todos los elementos de la lista deben ser de tipo int")

    mayor = lista[0]  # Asumimos que el primer elemento es el mayor

    for num in lista[1:]:  # Recorremos el resto de los elementos
        if num > mayor:  # Comparamos si el elemento actual es mayor
            mayor = num

    return mayor

# Prueba
print(encontrar_mayor([3, 1, 4, 1, 5, 9, 2]))  # 9

