def dao_nguoc_list(lst):
    return lst[::-1]
input_str = input("Nhập một dãy số nguyên, phân tách bằng dấu phẩy: ")
numbers = list(map(int, input_str.split(",")))
list_dao_nguoc = dao_nguoc_list(numbers)
print("Dãy số sau khi đảo ngược:", list_dao_nguoc)
