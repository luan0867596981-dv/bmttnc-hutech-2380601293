def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_str = input("Mời nhập chuỗi đảo ngược: ")
print("Chuỗi sau khi đảo ngược:", dao_nguoc_chuoi(input_str))
