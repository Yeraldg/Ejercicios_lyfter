
#ejercicio 1

def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) -1):
        avoid_to_repeat = False
        #for index in range(0, len(list_to_sort) -1): *ejercico 1
        for index in range(len(list_to_sort) -1, 0, -1):
            current_element = list_to_sort[index]
            #next_element = list_to_sort[index +1]   *ejercicio 1
            prev_element = list_to_sort[index - 1]
            print(f"iteration: {outer_index}")
            # print(f"Element:{current_element}, next element: {next_element}")
            print(f"Element:{current_element}, previous element: {prev_element}")
            #if current_element > next_element:
            if current_element < prev_element:
                print(f"{current_element} is lower than {prev_element}")
                list_to_sort[index] = prev_element
                list_to_sort[index - 1] = current_element 
                #print(f"{current_element} is bigger than {next_element}")
                #list_to_sort[index] = next_element  *ejercicio 1
                #list_to_sort[index + 1] = current_element    *ejercicio 1
                
                avoid_to_repeat = True
        if not avoid_to_repeat:
            return
    
    
    
list_to_sort = [80, 50, 15, -15, -50, -80]
bubble_sort(list_to_sort)
print(list_to_sort)

#ejercicio 2