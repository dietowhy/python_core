from .flowers import Flower
from .accessories import Accessory

class Bouquet:
    def __init__(self):
        self.flowers = []
        self.accessories = []

    def add_flower(self, flower: Flower):
        self.flowers.append(flower)

    def add_accessory(self, accessory: Accessory):
        self.accessories.append(accessory)

    def get_total_cost(self) -> float:
        flowers_cost = sum(flower.cost for flower in self.flowers)
        accessories_cost = sum(acc.cost for acc in self.accessories)
        return flowers_cost + accessories_cost

    def get_withering_time(self) -> float:
        if not self.flowers:
            return 0
        total_lifespan = sum(flower.lifespan for flower in self.flowers)
        return total_lifespan / len(self.flowers)

    def sort_flowers_by_cost(self, reverse: bool = False):
        self.flowers.sort(key=lambda flower: flower.cost, reverse=reverse)

    def has_flower(self, flower_name: str) -> bool:
        return any(flower.name.lower() == flower_name.lower() for flower in self.flowers)

    def show_bouquet(self):
        print(" Букет:")
        for flower in self.flowers:
            print(f" Цветок: {flower}")
        for acc in self.accessories:
            print(f" Аксессуар: {acc}")