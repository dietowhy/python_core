from src import Rose, Tulip, Orchid, Accessory, Bouquet

def main():
    rose = Rose(cost=150.0, lifespan=7)
    tulip = Tulip(cost=80.0, lifespan=4)
    orchid = Orchid(cost=300.0, lifespan=14)
    another_rose = Rose(cost=120.0, lifespan=5)

    ribbon = Accessory("Лента", 50.0)
    wrap = Accessory("Упаковка", 100.0)

    bouquet = Bouquet()
    bouquet.add_flower(rose)
    bouquet.add_flower(tulip)
    bouquet.add_flower(orchid)
    bouquet.add_flower(another_rose)
    bouquet.add_accessory(ribbon)
    bouquet.add_accessory(wrap)

    bouquet.show_bouquet()

    print(f"\n Общая стоимость букета: {bouquet.get_total_cost()} руб.")

    print(f" Среднее время жизни букета: {bouquet.get_withering_time():.1f} дней")

    search_name = "Тюльпан"
    has_it = bouquet.has_flower(search_name)
    if has_it:
        print(f" {search_name} есть в букете")
    else:
        print(" Такого цветка нет")

    bouquet.sort_flowers_by_cost()
    print("\n Отсортированный букет")
    bouquet.show_bouquet()

if __name__ == "__main__":
    main()