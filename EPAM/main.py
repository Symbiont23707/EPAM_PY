print("Task 1.1:") #для удобства в проверке

str1 = "Hello"
def calculate_without_len(str1):
    length_str = 0
    for i in str1:
        length_str += 1
    return length_str
print(calculate_without_len(str1)) #для удобства в проверке

print("Task 1.2:") #для удобства в проверке

str2 = "Oh, it is python"
def number_of_characters(str2):
    characters_and_count = {}
    for i in str2.lower():
        characters_and_count[i] = str2.count(i)
    return characters_and_count
print(number_of_characters(str2)) #для удобства в проверке

print("Task 1.3(1):") #для удобства в проверке

list1 = ['red', 'white', 'black', 'red', 'green', 'black']
def unique_words(list1):
    edited_list1 = []
    for i in sorted(set(list1)):
        edited_list1.append(i)
    return edited_list1
print(unique_words(list1))

print("Task 1.3(2):") #для удобства в проверке
def list_divisors():
    number = int(input("What's number u want: "))
    i = 1
    set1 = set()
    while i <= number:
        if number % i == 0:
            set1.add(i)
        i += 1
    return set1
print(list_divisors())

print("Task 1.4:") #для удобства в проверке
dict1 = {4: "apple", 1: "orange", 2: "pineapple", 5: "pear"}
def sort_dictionary_by_key(dict1):
    saved_items = dict1.items()
    dict1 = sorted(saved_items)
    return dict(dict1)
print(sort_dictionary_by_key(dict1))

print("Task 1.5:") #для удобства в проверке
list2 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
def unique_values(list2):
    list2_edited = set()
    for i in list2:
        for value in i.values():
            list2_edited.add(value)
    print(list2_edited)
unique_values(list2)

print("Task 1.6:") #для удобства в проверке
tuple1 = (1, 2, 3, 4)
def convert_tuple_in_integer(tuple1):
    convert_number = ""
    for i in tuple1:
        if i > 0:
            convert_number += str(i)
    return int(convert_number)
print(convert_tuple_in_integer(tuple1))

print("Task 1.6:") #для удобства в проверке
def multiplication_table(a = 2,b = 4,c = 3,d = 7):
    for x in range(c, d + 1):
        if x == c:
            print("    "+str(x), end="   ")
        else:
            print(str(x), end="   ")
    print(sep="\n")
    for i in range(a, b+1):
        list3 = []
        print(i, end="   ")
        for x in range(c, d+1):
            list3.append(i*x)
        for row in list3:
            if row > 9:
                print(row, end="  ")
            else:
                print(row, end="   ")
        print(sep="\n")
multiplication_table()
