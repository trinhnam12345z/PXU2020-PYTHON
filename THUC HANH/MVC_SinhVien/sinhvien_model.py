import sinhvien_db
import db_exceptions

class SinhVienModel(object):
    #Phương thức khởi tạo
    def __init__(self, database_server, username, password, database):
        self.connection, self.metadata, self.engine = sinhvien_db.connect_db(database_server,
                                                                                 username,
                                                                                 password,
                                                                                 database)

    #Phương thức lấy dữ liệu
    def get_all_sinhvien(self):
        results = sinhvien_db.get_all_db_sv(self.connection,
                                                           self.metadata,
                                                           self.engine)
        return results

    #Phương thức insert
    def insert_sinhvien(self, TenSV, NamSinh):
        resultID = sinhvien_db.insert_sv(self.connection,
                                       self.metadata,
                                       self.engine,
                                       TenSV, NamSinh)
        return resultID

    #Phương thức update
    def update_sinhvien(self, TenSV,idSinhVien):
        resultID = sinhvien_db.update_sv(self.connection,
                                         self.metadata,
                                         self.engine,
                                         TenSV, idSinhVien)
        return resultID
    #Phương thức delete
    def delete_sinhvien(self, idSinhVien):
        resultID = sinhvien_db.delete_sv(self.connection,
                                         self.metadata,
                                         self.engine,idSinhVien)
        return resultID