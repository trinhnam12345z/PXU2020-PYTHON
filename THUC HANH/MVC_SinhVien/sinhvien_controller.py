import db_exceptions
import sinhvien_db
import sinhvien_view
import sinhvien_model

class SinhVienController(object):
    #Phương thức khởi tạo
    def __init__(self, model, view):
        self.model = model
        self.view = view

    #Phương thức hiển thị tất cả dữ liệu của bảng person
    def show_all_sinhvien(self):
        items = self.model.get_all_sinhvien()
        self.view.display_all_sinhvien(items)

    #Phương thức insert
    def insert_sinhvien(self, TenSV, NamSinh):
        resultID = self.model.insert_sinhvien(TenSV, NamSinh)
        self.view.ket_qua_insert(resultID)
    #Phương thức update
    def update_sinhvien(self, TenSV, idSinhVien):
        self.model.update_sinhvien(TenSV,idSinhVien)
        self.view.ket_qua_update()

    #Phương thức delete
    def delete_sinhvien(self,idSinhVien):
        self.model.delete_sinhvien(idSinhVien)
        self.view.ket_qua_delete()