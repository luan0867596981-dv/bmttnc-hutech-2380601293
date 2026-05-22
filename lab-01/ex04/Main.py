from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:

    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("************************** MENU **************************")
    print("**               1. Them sinh vien                      **")
    print("**               2. Cap nhat sinh vien theo ID          **")
    print("**               3. Xoa sinh vien theo ID               **")
    print("**               4. Tim kiem sinh vien theo ten         **")
    print("**               5. Sap xep sinh vien theo diem TB      **")
    print("**               6. Sap xep sinh vien theo ten          **")
    print("**               7. Hien thi danh sach sinh vien        **")
    print("**               0. Thoat                               **")
    print("**********************************************************")

    key = int(input("Nhap lua chon: "))

    # Thêm sinh viên
    if key == 1:
        print("\nTHEM SINH VIEN")
        qlsv.nhapSinhVien()

    # Cập nhật
    elif key == 2:
        if qlsv.soLuongSinhVien() > 0:

            ID = int(input("Nhap ID sinh vien can sua: "))
            qlsv.updateSinhVien(ID)

        else:
            print("Danh sach rong!")

    # Xóa
    elif key == 3:
        if qlsv.soLuongSinhVien() > 0:

            ID = int(input("Nhap ID sinh vien can xoa: "))

            if qlsv.deleteByID(ID):
                print("Xoa thanh cong!")
            else:
                print("Khong tim thay sinh vien!")

        else:
            print("Danh sach rong!")

    # Tìm kiếm
    elif key == 4:
        if qlsv.soLuongSinhVien() > 0:

            keyword = input("Nhap ten can tim: ")

            result = qlsv.findByName(keyword)

            qlsv.showSinhVien(result)

        else:
            print("Danh sach rong!")

    # Sắp xếp điểm TB
    elif key == 5:
        if qlsv.soLuongSinhVien() > 0:

            qlsv.sortByDiemTB()

            qlsv.showSinhVien(qlsv.getListSinhVien())

        else:
            print("Danh sach rong!")

    # Sắp xếp tên
    elif key == 6:
        if qlsv.soLuongSinhVien() > 0:

            qlsv.sortByName()

            qlsv.showSinhVien(qlsv.getListSinhVien())

        else:
            print("Danh sach rong!")

    # Hiển thị danh sách
    elif key == 7:
        if qlsv.soLuongSinhVien() > 0:

            qlsv.showSinhVien(qlsv.getListSinhVien())

        else:
            print("Danh sach rong!")

    # Thoát
    elif key == 0:
        print("Thoat chuong trinh!")
        break

    else:
        print("Lua chon khong hop le!")