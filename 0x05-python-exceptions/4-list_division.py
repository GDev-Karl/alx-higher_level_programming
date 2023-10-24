#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    division_list = []

    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            division_list.append(result)

    return division_list
