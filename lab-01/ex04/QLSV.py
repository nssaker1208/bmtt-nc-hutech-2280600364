from SinhVien import SinhVien

class QLSV:
    listSinhVien = []
    
    def TaoID(self):
        maxId = 1
        if(self.soLuongSV() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
    
    def soLuongSV(self):
        return self.listSinhVien.__len__()
    
    def nhapSV(self):
        svId = self.TaoID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh cua sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
        
    def updateSV(self, ID):
        sv:SinhVien = self.findByID(ID)
        if (sv != None):
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh cua sinh vien: ")
            major = input("Nhap chuyen nganh cua sinh vien: ")
            diemTB = float(input("Nhap diem cua sinh vien: "))
            self._name = name
            self._sex = sex
            self._major = major
            self._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else: print("Sinh vien co ID = {} khong ton tai.".format(ID))
    
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)
    
    def findByID(self, ID):
        searchResult = None
        if (self.soLuongSV() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
    
    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSV() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    
    def deleteById(self, ID):
        isDelete = False
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDelete = True
        return isDelete
    
    def xepLoaiHocLuc(self, sv:SinhVien):
        if (sv._diemTB >= 8): sv._hocluc = "Gioi"
        elif (sv._diemTB >= 6.5): sv._hocluc = "Kha"
        elif (sv._diemTB >= 5): sv._hocluc = "Trung binh"
        else: sv._hocluc = "Yeu"
        
    def showSV(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}"
              .format("ID", "Name", "Sex", "Major", "DiemTB", "Hoc Luc"))
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}"
                      .format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocluc))
        print("\n")
    
    def getListSV(self):
        return self.listSinhVien
    