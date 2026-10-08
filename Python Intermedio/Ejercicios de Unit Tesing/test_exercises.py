import pytest

#ejercicio 1
def bubble_sort(final_list):
    for outer_index in range(0, len(final_list) -1):
        avoid_to_repeat = False
        for index in range(0, len(final_list) -1):
                current_element = final_list[index]
                next_element = final_list[index +1]
                if current_element > next_element:
                    final_list[index] = next_element
                    final_list[index +1] = current_element 
                    avoid_to_repeat = True
        if not avoid_to_repeat:
            return final_list
    return final_list

def test_bubble_sort_small_list():
    final_list = [5, 3, 2, 1, 4] # arrange
    result = bubble_sort(final_list) # act
    assert result == [1, 2, 3, 4, 5] #assert
    
def test_bubble_sort_long_list():
    final_list = [
    57, 12, 89, 3, 76, 45, 21, 98, 34, 67,
    5, 81, 29, 43, 100, 16, 72, 8, 91, 38,
    64, 25, 49, 7, 83, 31, 59, 14, 96, 40,
    18, 74, 2, 87, 53, 22, 68, 35, 94, 11,
    61, 27, 79, 4, 50, 92, 33, 70, 19, 85,
    42, 6, 63, 28, 99, 15, 54, 73, 36, 88,
    10, 47, 80, 24, 66, 13, 95, 39, 71, 30,
    58, 1, 82, 46, 17, 69, 32, 90, 23, 52,
    75, 9, 44, 97, 26, 62, 37, 86, 20, 55,
    48, 78, 41, 60, 84, 93, 56, 65, 51, 77,
    101] #arrange
    result = bubble_sort(final_list) # act
    assert result == [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
    91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
    101] #assert

def test_bubble_sort_empty_list():
    final_list = [] #arrange
    result = bubble_sort(final_list) #act
    assert result == [] #assert

def test_bubble_sort_not_a_list():
    final_list = "string" #arrange
    with pytest.raises(TypeError):
        bubble_sort(final_list) #act
    # este caso va sin assert
    
# ejercicio 2

print("---- ejercicio 3 ----")

numbers = [4, 6, 2, 29]


def sum_numbers(numbers):
    total_result = 0
    
    for num in numbers:
        total_result += num 
    return total_result

    
print(sum_numbers(numbers))

print("---- ejercicio 4 ----")

text = "hola"

def go_backwards(text):
    new_text = ""
    
    for letter in range(len(text) -1 ,-1 , -1):
        new_text += text[letter]
        
    return new_text
    
print(go_backwards(text))

print("---- ejercicio 5 ----")

paragraph = "I love Nación Sushi"

def analyze_case(paragraph):
    upper_count = 0
    
    lower_count = 0
    
    for case in paragraph:
        if case.isupper():
            upper_count += 1
        elif case.islower():
            lower_count += 1

    print(f"there's {upper_count} upper cases and {lower_count} lower cases")
    
analyze_case(paragraph)

print("---- ejercicio 6 ----")

#hypen_words = input("pot favor ingrese palabras separadas por guiones (-): ")

def order_words(hypen_words):
    unsorted_list = hypen_words.split("-")
    unsorted_list.sort()
    ordered_list = "-".join(unsorted_list)
    
    print(ordered_list)

#order_words(hypen_words)

print("---- ejercicio 7 ----")

all_numbers = [1, 4, 6, 7, 13, 9, 67]

def is_prime(number):
    if number <= 1:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True

def get_primes(all_numbers):
    prime_numbers = []
    
    for number in all_numbers:
        if is_prime(number):
            prime_numbers.append(number)
            
    return prime_numbers
    
print(get_primes(all_numbers))

def test_sum_numbers_case1():
    numbers = [4, 6, 2, 29]
    result = sum_numbers(numbers)
    assert result == 41

def test_sum_numbers_case2():
    numbers = [14, 62, 16]
    result = sum_numbers(numbers)
    assert result == 92

def test_sum_numbers_case3():
    numbers = [17, 13, 6, 4]
    result = sum_numbers(numbers)
    assert result == 40

def test_go_backwards_case1():
    text = "hola"
    result = go_backwards(text)
    assert result == "aloh"

def test_go_backwards_case2():
    text = "yerald"
    result = go_backwards(text)
    assert result == "dlarey"

def test_go_backwards_case3():
    text = "keyboard"
    result = go_backwards(text)
    assert result == "draobyek"

def test_analyze_case_case1(capsys):
    paragraph = "I love New York"
    analyze_case(paragraph)
    captured = capsys.readouterr()
    assert captured.out == "there's 3 upper cases and 9 lower cases\n"

def test_analyze_case_case2(capsys):
    paragraph = "I am from CR"
    analyze_case(paragraph)
    captured = capsys.readouterr()
    assert captured.out == "there's 3 upper cases and 6 lower cases\n"

def test_analyze_case_case3(capsys):
    paragraph = "FOUR upper cases"
    analyze_case(paragraph)
    captured = capsys.readouterr()
    assert captured.out == "there's 4 upper cases and 10 lower cases\n"

def test_order_words_case1(capsys):
    hyphen_words = "python-variable-funcion-computadora-monitor"
    order_words(hyphen_words)
    captured = capsys.readouterr()
    assert captured.out == "computadora-funcion-monitor-python-variable\n"

def test_order_words_case2(capsys):
    hyphen_words = "carro-bicicleta-tren-bus-avion"
    order_words(hyphen_words)
    captured = capsys.readouterr()
    assert captured.out == "avion-bicicleta-bus-carro-tren\n"

def test_order_words_case3(capsys):
    hyphen_words = "papel-hoja-lapiz-boligrafo-uniforme"
    order_words(hyphen_words)
    captured = capsys.readouterr()
    assert captured.out == "boligrafo-hoja-lapiz-papel-uniforme\n"

def test_get_primes_case1():
    all_numbers = [1, 4, 6, 7, 13, 9, 67]
    primes = get_primes(all_numbers)
    assert primes == [7, 13, 67]

def test_get_primes_case2():
    all_numbers = [1, 3, 6, 7]
    primes = get_primes(all_numbers)
    assert primes == [3, 7]

def test_get_primes_case3():
    all_numbers = [1, 3, 6, 13]
    primes = get_primes(all_numbers)
    assert primes == [3, 13]