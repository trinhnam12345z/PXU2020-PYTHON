class car:
    def __init__(self,name, engine, color):
        self.name = name
        self.engine = engine
        self.color = color

    def set_name(self, name):
        self.name = name
    def set_engine(self, engine):
        self.engine = engine
    def set_color(self, color):
        self.color = color

    def __str__(self):
        return "{} sử dụng động cơ {} có màu {}".format(self.name,self.engine,self.color)

    @classmethod

    def get_all_car(self):
        database = [("lambogini","H1","xanh"),("BMW","H2","đỏ"),("Audi","H3","tím")]
        result = []

        for idx, (name,engine,color) in enumerate(database):
            tam = car(name,engine,color)
            result.append(tam)
        return result
