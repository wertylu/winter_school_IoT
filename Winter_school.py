from operator import itemgetter


class Fish:

    def __init__(self) -> None:
        self.name = input("name?")
        self.price_in_uah_per_kilo = input("price_in_uah_per_kilo?")
        self.body_only = input("body_only?")
        self.origin = input("origin?")
        self.weight = input("weight?")


class FishShop:
    list_of_fish = []

    def add_fish(self):
        fish_name = str(input("name?"))
        fish_price_in_uah_per_kilo = float(input("price per kilo?"))
        fish_weight = float(input("weight?"))
        list_of_parameters = [fish_name, fish_price_in_uah_per_kilo, fish_weight]
        self.list_of_fish.append(list_of_parameters)

    def get_fish_names_sorted_by_price(self):
        print("Sorted List based on price: % s" % (sorted(self.list_of_fish, key=itemgetter(1), reverse=True)))

    def sell_fish(self):
        fish_name = input("which fish u want to sell?")
        weight = float(input("How much u want to sell?"))
        counter = len(self.list_of_fish)
        for i in range(len(self.list_of_fish)):
            if self.list_of_fish[i][0] == fish_name:
                counter -= 1
                self.list_of_fish[i][2] -= weight
                if self.list_of_fish[i][2] < 0:
                    self.list_of_fish[i][2] += weight
                    print("you want too much")
                money = int(self.list_of_fish[i][1]) * weight
                print("money is :" + str(money))
                print(self.list_of_fish)
                return money
        if counter == len(self.list_of_fish):
            print("fish not found")

    def cast_out_old_fish(self):
        fish_name = input("which fish u want to cast out")
        weight = int(input("How much u want to cast out"))
        counter = len(self.list_of_fish)
        for i in range(len(self.list_of_fish)):
            if self.list_of_fish[i][0] == fish_name:
                counter -= 1
                if self.list_of_fish[i][2] - weight >= 0:
                    self.list_of_fish[i][2] -= weight
                    print(self.list_of_fish)
                else:
                    print("you want too much")
        if counter == len(self.list_of_fish):
            print("fish not found")


class Seller:
    def sell_fish(self, fish_type: str, fish_weight: float):
        pass

    def torguvatys(self, fish_price_in_uah):
        pass


class Buyer:
    def buy_fish(self, fish_type: str, fish_weight: float):
        pass

    def torguvatys(self, fish_price_in_uah):
        pass

    def get_fish_info(self, fish_type):
        pass


shop = FishShop()
shop.add_fish()
shop.add_fish()
shop.add_fish()
shop.get_fish_names_sorted_by_price()
money_account = shop.sell_fish()
shop.cast_out_old_fish()
