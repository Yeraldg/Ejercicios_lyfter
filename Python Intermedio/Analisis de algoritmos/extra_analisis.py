#jercicio 1

# manual_add
def manual_add(n):
    result = 0
    for i in range(1, n + 1):  # O(n)
        result += i  # O(1)
    return result  # O(1)
# complejidad temporal: O(n)


# add_formula
def add_formula(n):
    return n * (n + 1) // 2  # O(1)
# complejidad temporal: O(1)

#Versión 1 (manual_add) → O(n)
#Versión 2 (add_formula) → O(1)
#Si number = 1,000,000,000, usaría la versión 2, porque realiza la operación directamente sin tener que recorrer mil millones de números

# ejercicio 2

# linear_search

def linear_search(my_list, target):
    for item in my_list:  # O(n)
        if item == target:  # O(1)
            return True  # O(1)
    return False  # O(1)
# complejidad temporal: O(n)


# binary_search

def binary_search(my_list, target):
    low = 0  # O(1)
    high = len(my_list) - 1  # O(1)
    while low <= high:  # O(log n)
        mid = (low + high) // 2  # O(1)
        if my_list[mid] == target:  # O(1)
            return True  # O(1)
        elif my_list[mid] < target:  # O(1)
            low = mid + 1  # O(1)
        else:
            high = mid - 1  # O(1)
    return False  # O(1)

# complejidad temporal: O(log n)

#R 2: lineal search sirve cuando toda la lista esta ordenada , aunq como revisa todos se toma su tiempo
#     binary search es mas rapida pero la lista tiene que estar casi que ordena sino no funciona
#R 3: linear search funciona bien, binary tree no funcionaria, xq ordenaria la lista en 2 bloques


#ejercicio 3
# print_all_pairs

def print_all_pairs(my_dict):
    for key1 in my_dict:  # O(n)
        for key2 in my_dict:  # O(n)
            print(f"{key1}-{key2}")  # O(1)

# complejidad temporal: O(n²), xq tiene 2 for

#R 2: haria un millon de millones de operaciones/print osea un billon, pero en si la duracion tambien depende de la compu, y tampoco sabemos la dificultad de cada print