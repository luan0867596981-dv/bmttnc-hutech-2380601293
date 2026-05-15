def tao_tupre_tu_list(lst):
    return tuple(lst)
input_str = input("Nhập một dãy số nguyên, phân tách bằng dấu phẩy: ")
numbers = list(map(int, input_str.split(",")))
my_tuple = tao_tupre_tu_list(numbers)
print("List: ", numbers)
print("Tuple từ list: ", my_tuple)