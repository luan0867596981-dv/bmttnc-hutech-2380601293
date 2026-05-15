from QuanLySinhVien import QuanLySinhVien   
qlsv = QuanLySinhVien()
while (1==1):
    print("\n CHUONG TRINH QUAN LY SINH VIEN")
    print("**************************Menu**************************")
    print("** 1.Them sinh vien.                                  **")
    print("** 2.Cap nhat thong tin sinh vien boi ID.             **")
    print("** 3.Xoa sinh vien boi ID.                            **")
    print("** 4.Tim kiem sinh vien theo ten.                     **")
    print("** 5.Sap xep sinh vien theo diem trung binh.          **")
    print("** 6.Sap xep sinh vien theo ten chuyen nghanh.        **")
    print("** 7.Hien thi danh sach sinh vien.                    **")
    print("** 0.Thoat.                                           **")
    print("******************************************************")
     
    key = int(input("Nhap lua chon cua ban: "))
    if (key ==1):
        print("\n 1.Them sinh vien.")
        qlsv.nhapSinhVien()
        print("Sinh vien da duoc them vao danh sach.")
    elif (key == 2):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n 2.Cap nhat thong tin sinh vien boi ID.")
            print("Nhap ID sinh vien can cap nhat: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("Danh sach sinh vien rong.")
    elif (key == 3):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n 3.Xoa sinh vien boi ID.")
            print("Nhap ID sinh vien can xoa: ")
            ID = int(input())
            if (qlsv.deleteByID(ID)):
                print("Sinh vien co ID = ", ID, " da duoc xoa khoi danh sach.")
            else:
                print("Sinh vien co ID = ", ID, " khong ton tai trong danh sach.")
        else:
            print("Danh sach sinh vien rong.")
            
    elif (key == 4):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n 4.Tim kiem sinh vien theo ten.")
            print("Nhap tu khoa tim kiem: ")
            name = input()
            seachResult = qlsv.findByName(name)
            qlsv.showSinhVien(seachResult)   
        else:
            print("Danh sach sinh vien rong.")  
    
    elif (key == 5):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n 5.Sap xep sinh vien theo diem trung binh.")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.listSinhVien)
        else:
            print("Danh sach sinh vien rong.")  
            
    elif (key == 6):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n 6.Sap xep sinh vien theo ten chuyen nghanh.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.listSinhVien)
        else:
            print("Danh sach sinh vien rong.")
    elif (key == 7):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n 7.Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.listSinhVien)
        else:
            print("Danh sach sinh vien rong.")
    elif (key == 0):
        print("Thoat chuong trinh.")
        break
    else:
        print("Lua chon khong hop le. Vui long chon lai.")
        print("\n Hay chon chuc nang trong truong hop menu")