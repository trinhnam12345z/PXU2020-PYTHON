import db_exceptions
import sinhvien_db
import sinhvien_model, sinhvien_view, sinhvien_controller

def start():
    #Khởi tạo đối tượng model
    model = sinhvien_model.SinhVienModel("localhost", "root", "123456789", "ql_sv_pxu")
    #Khởi tạo đối tượng view
    view = sinhvien_view.SinhVienView()
    #Khởi tạo controller
    controller = sinhvien_controller.SinhVienController(model, view)

    # controller.insert_sinhvien("Trinh Nam",20)

    controller.update_sinhvien("nam update",24)

    # controller.delete_sinhvien(21)

    #Hiển thị tất cả dữ liệu của bảng person
    controller.show_all_sinhvien()

if __name__ == "__main__":
    start()