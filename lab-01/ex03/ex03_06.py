def xoa_phan_tu(dicionary, key):
    if key in dicionary:
        del dicionary[key]
        return True
    else:
        return False
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
key_to_delete = 'b'
result = xoa_phan_tu(my_dict, key_to_delete)
if result:
    print("Phần tử đã đc xoá từ Dictionary:", my_dict)
else:
    print("Không tìm thấy key trong Dictionary.")