
def func():

    with open('text_random.txt', 'r') as file:
        data = file.read()
        little_data = data.lower()
        import re
        del_number = re.sub("[0-100]", "", little_data)
        num = del_number.split('.')

        dictionary = {}
        for i in num:
            word = i.split()
            for el in word:
                if el in dictionary:
                    dictionary[el] += 1
                else:
                    dictionary[el] = 1

    s = sum(dictionary.values())
    print(s)

    return dictionary


n = func()
print(n)










