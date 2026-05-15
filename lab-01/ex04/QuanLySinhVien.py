from SinhVien import SinhVien

class QuaLySinhVien:
    listSinhVien = []
    
    def generateID(self):
        maxID = 1
        if (self.soLuongSinhVien() > 0):
            maxID = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (sv._id > maxID):
                    maxID = sv._id
            maxID += 1
        return maxID
    
    def soLuongSinhVien(self):
        svID = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập ngành học sinh viên: ")
        diemTB = float(input("Nhập điểm trung bình sinh viên: "))
        sv = SinhVien(svID, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
        
    def updateSinhVien(self, ID):
        sv: SinhVien = self.findByID(ID)
        if (sv != None):
                name = input("Nhập tên sinh viên: ")
                sex = input("Nhập giới tính sinh viên: ")
                major = input("Nhập ngành học sinh viên: ")
                diemTB = float(input("Nhập điểm trung bình sinh viên: "))
                sv._name = name
                sv._sex = sex
                sv._major = major
                sv._diemTB = diemTB
                self.xepLoaiHocLuc(sv)
        else :
            print("Sinh viên có ID = {} không tồn tại".format(ID))
    
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
    
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
        
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=True)
    
    def findByID(self, ID):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
    
    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    
    def deleteByID(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLuc(self, sv: SinhVien):
        if (sv._diemTB >= 8):
            sv._hocluc = "Giỏi"
        elif (sv._diemTB >= 6.5):
            sv._hocluc = "Khá"
        elif (sv._diemTB >= 5):
            sv._hocluc = "Trung bình"
        else:
            sv._hocluc = "Yếu"
    
    def showSinhVien(self, listSV):
        print("{:<=8} {:<=18} {:<=8} {:<=8} {:<=8} {:<=8}".format("ID", "Name", "Sex", "Major", "DiemTB", "HocLuc"))
        if (listSV)._len_() > 0:
            for sv in listSV:
                print("{:<=8} {:<=18} {:<=8} {:<=8} {:<=8} {:<=8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocluc))
        print("\n")
    
    
    def getListSinhVien(self):
        return self.listSinhVien