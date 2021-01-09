from model import car

def startView():
    key = input('Bạn có muốn xem tất cả dữ liệu không? [y/n] ')
    return key
def endView():
    print('See You')

def showAllView(danhsach):
    for car in danhsach:
        print(car.name, '--', car.engine,'--',car.color)
    print('Tổng cộng có ', len(danhsach), ' car')