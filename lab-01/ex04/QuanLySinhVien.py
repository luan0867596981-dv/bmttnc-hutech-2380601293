from SinhVien import SinhVien


class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    # Sinh ID tự tăng
    def generateID(self):
        maxID = 1

        if len(self.listSinhVien) > 0:
            maxID = self.listSinhVien[0]._id

            for sv in self.listSinhVien:
                if sv._id > maxID:
                    maxID = sv._id

            maxID += 1

        return maxID

    # Số lượng sinh viên
    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    # Thêm sinh viên
    def nhapSinhVien(self):
        svID = self.generateID()

        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập ngành học sinh viên: ")
        diemTB = float(input("Nhập điểm trung bình sinh viên: "))

        sv = SinhVien(svID, name, sex, major, diemTB)

        self.xepLoaiHocLuc(sv)

        self.listSinhVien.append(sv)

    # Cập nhật sinh viên
    def updateSinhVien(self, ID):
        sv = self.findByID(ID)

        if sv is not None:
            sv._name = input("Nhập tên sinh viên: ")
            sv._sex = input("Nhập giới tính sinh viên: ")
            sv._major = input("Nhập ngành học sinh viên: ")
            sv._diemTB = float(input("Nhập điểm trung bình sinh viên: "))

            self.xepLoaiHocLuc(sv)

            print("Cập nhật thành công!")
        else:
            print("Sinh viên không tồn tại!")

    # Xóa sinh viên
    def deleteByID(self, ID):
        sv = self.findByID(ID)

        if sv is not None:
            self.listSinhVien.remove(sv)
            return True

        return False

    # Tìm theo ID
    def findByID(self, ID):
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv

        return None

    # Tìm theo tên
    def findByName(self, keyword):
        result = []

        for sv in self.listSinhVien:
            if keyword.upper() in sv._name.upper():
                result.append(sv)

        return result

    # Sắp xếp theo ID
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id)

    # Sắp xếp theo tên
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name)

    # Sắp xếp theo điểm TB
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=True)

    # Xếp loại học lực
    def xepLoaiHocLuc(self, sv):
        if sv._diemTB >= 8:
            sv._hocluc = "Giỏi"
        elif sv._diemTB >= 6.5:
            sv._hocluc = "Khá"
        elif sv._diemTB >= 5:
            sv._hocluc = "Trung Bình"
        else:
            sv._hocluc = "Yếu"

    # Hiển thị danh sách sinh viên
    def showSinhVien(self, listSV):
        print(
            "{:<8} {:<20} {:<10} {:<15} {:<10} {:<10}".format(
                "ID",
                "Name",
                "Sex",
                "Major",
                "DiemTB",
                "HocLuc"
            )
        )

        for sv in listSV:
            print(
                "{:<8} {:<20} {:<10} {:<15} {:<10} {:<10}".format(
                    sv._id,
                    sv._name,
                    sv._sex,
                    sv._major,
                    sv._diemTB,
                    sv._hocluc
                )
            )

    # Lấy danh sách sinh viên
    def getListSinhVien(self):
        return self.listSinhVien