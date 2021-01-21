import sqlalchemy as db
import db_exceptions

#Xây dựng hàm thiết lập kết nối đến csdl
#Trả về đối tượng là connection, metadata và engine
def connect_db(database_server, username, password, database):
    connection_str = "mysql://{}:{}@{}/{}".format(username, password, database_server, database)
    engine = db.create_engine(connection_str)
    connection = engine.connect()
    metadata = db.MetaData()
    return connection, metadata, engine

#Xây dựng hàm lấy tất cả dữ liệu của bảng Person
def get_all_db_sv(connection, metadata, engine):
    # Lấy đối tượng person từ bảng person trong csdl
    sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)

    # Lấy tất cả dữ liệu của bảng person - tương đương câu lênh SELECT * FROM person
    query = db.select([sinhvien])

    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()

    return ResultSet

#Hàm insert
def insert_sv(connection,metadata, engine,TenSV,NamSinh):
    sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)
    query = db.insert(sinhvien).values(TenSV=TenSV, NamSinh=NamSinh)
    ResultProxy = connection.execute(query)
    return ResultProxy.inserted_primary_key

#Hàm update

def update_sv(connection,metadata, engine,TenSV,idSinhVien):
    sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)
    query_insert = db.update(sinhvien).values(TenSV=TenSV).where(sinhvien.columns.idSinhVien == idSinhVien)
    ResultProxy = connection.execute(query_insert)
    return ResultProxy

#Hàm delete

def delete_sv(connection,metadata, engine,idSinhVien):
    sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)
    query_delete = db.delete(sinhvien).where(sinhvien.columns.idSinhVien == idSinhVien)
    ResultProxy = connection.execute(query_delete)
    return ResultProxy