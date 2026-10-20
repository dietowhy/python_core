class Flower:
    def __init__(self, name: str, cost: float, lifespan: int):
        self.name = name
        self.cost = cost
        self.lifespan = lifespan 

    def __str__(self):
        return f"{self.name} (Цена: {self.cost} руб., Жизнь: {self.lifespan} дн.)"


class Rose(Flower):
    def __init__(self, cost: float, lifespan: int):
        super().__init__("Роза", cost, lifespan)


class Tulip(Flower):
    def __init__(self, cost: float, lifespan: int):
        super().__init__("Тюльпан", cost, lifespan)


class Orchid(Flower):
    def __init__(self, cost: float, lifespan: int):
        super().__init__("Орхидея", cost, lifespan)