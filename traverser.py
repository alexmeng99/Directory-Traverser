# Alexandria Meng

from pathlib import Path
import os
import shutil



# prints all things in directory and its subdirectory
def pressed_r(p):
    file_list = []
    r_list = []
    dir_list = []
    for element in p.iterdir():
        if element.is_file():
            file_list.append(element)
    for element in p.iterdir():
        if element.is_dir():
            r_list = pressed_r(element)
            for file in r_list:
                file_list.append(file)
    return file_list

# prints all things in root directory and prints subdirectories
def pressed_d(p):
    file_list = []
    for element in p.iterdir():
        if element.is_file():
            file_list.append(element)
    for element in p.iterdir():
        if element.is_dir():
            file_list.append(element)
    return file_list

# turns path into string
def path_into_string(file_path):
    string_list = str(file_path)
    string = ''
    for letter in string_list:
        string += letter
    return string

# retype all past files
def pressed_a(file_list):
    file_list_2 = []
    for element in file_list:
        print(element)
        file_list_2.append(element)
    return file_list_2

# search for file and include file type
def pressed_n(file_list, detail_order):
    file_list_2 = []
    for element in file_list:
        if element.name == detail_order:
            print(element)
            file_list_2.append(element)
    return file_list_2   

#search for particular extension
def pressed_e(file_list, detail_order):
    file_list_2 = []
    if detail_order.find('.') != -1:
        detail_order = detail_order[detail_order.find('.') + 1:]
    for element in file_list:
        string_element = path_into_string(element)
        extension = string_element[string_element.find('.') + 1:]
        if extension == detail_order:
            print(element)
            file_list_2.append(element)
    return file_list_2   

# search text file or specific word and return that file
def pressed_t(file_list, detail_order):
    file_list_2 = []
    for file in file_list:
        check_file = None
        try:
            check_file = open(file, 'r')
            for line in check_file:
                if line.find(detail_order) != -1:
                    print(file)
                    file_list_2.append(element)
            return file_list_2   
        except ValueError:
            pass
        finally:
            if check_file != None:
                check_file.close()

# search for file sizes that less than the number after it
def pressed_less_than(file_list, detail_order):
    file_list_2 = []
    for file in file_list:
        if os.path.getsize(file) < int(detail_order):
            print(file)
            file_list_2.append(file)
    return file_list_2

# search for file sizes that are greater than the number after it
def pressed_greater_than(file_list, detail_order):
    file_list_2 = []
    for file in file_list:
        if os.path.getsize(file) > int(detail_order):
            print(file)
            file_list_2.append(file)
    return file_list_2

# print first line of text file; “NOT TEXT” if it’s not a text file
def pressed_f(file_list_2):
    for file in file_list_2:
        check_file = None
        try:
            with open(file, 'r') as check_file:
                first_line = check_file.readline()
                first_line = first_line[:-1]
                print(first_line)
        except ValueError:
            print('NOT TEXT')
        finally:
            if check_file != None:
                check_file.close()

# duplicates file and puts the duplicate in its original directory 
def pressed_dup(file_list_2):
    for file in file_list_2:
        if file.is_file():
            file_string = path_into_string(file)
            new_file_string = file_string + '.dup'
            new_file = Path(new_file_string)
            shutil.copyfile(file, new_file)
        else:
            print('It is a directory!')

# changes date and time of file to current date and time
def pressed_touch(file_list_2):
    for file in file_list_2:
        if file.is_file():
            os.utime(file, )
        else:
            print('It is a directory!')

def step_1():
    while True:
        s = input()
        p = Path(s[2:])
        file_list = []
        if p.exists() and s.startswith('R '):
            file_list = pressed_r(p)
            for file in file_list:
                print(file)
            break

        elif p.exists() and s.startswith('D '):
            file_list = pressed_d(p)
            for file in file_list:
                print(file)
            break
        else:
            print('ERROR')
    return file_list



def step_2():
    file_list = step_1()
    while True:
        s = input()
        detail_order = s[2:]
        file_list_2 = []
        try:
            if s.startswith('A '):
                file_list_2 = pressed_a(file_list)
                return file_list_2

            elif s.startswith('N '):
                file_list_2 = pressed_n(file_list, detail_order)
                return file_list_2

            elif s.startswith('E '):
                file_list_2 = pressed_e(file_list, detail_order)
                return file_list_2
            
            elif s.startswith('T '):
                file_list_2 = pressed_t(file_list, detail_order)
                return file_list_2

            elif s.startswith('< '):
                file_list_2 = pressed_less_than(file_list, detail_order)
                return file_list_2

            elif s.startswith('> '):
                file_list_2 = pressed_greater_than(file_list, detail_order)
                return file_list_2
            else:
                print('ERROR')
        except ValueError:
            print('ERROR')



def step_3():
    file_list_2 = step_2()
    if file_list_2 != None:
        while True:
            s = input()
            if s == 'F':
                pressed_f(file_list_2)
                break
            elif s == 'D':
                pressed_dup(file_list_2)
                break
            elif s == 'T':
                pressed_touch(file_list_2)
                break
            else:
                print('ERROR')
            
    


step_3()

