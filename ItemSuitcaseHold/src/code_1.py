# Write your solution here:
class Item:

    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

class Suitcase:

    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__case = []
        self.__total_weight = 0

    def add_item(self, item: Item):
        if self.__total_weight < self.__max_weight and self.__total_weight + item.weight() < self.__max_weight:
            self.__case.append(item)
            self.__total_weight += item.weight()

    def __str__(self):
        if len(self.__case) == 1:
            return f"{len(self.__case)} item ({self.__total_weight} kg)"
        return f"{len(self.__case)} items ({self.__total_weight} kg)"

    def print_items(self):
        for i in self.__case:
            print(i)

    def weight(self):
        return self.__total_weight

    def heaviest_item(self):

        if len(self.__case) == 0:
            return None

        heavy_weight = 0
        heaviest_item = self.__case[0]

        for item in self.__case:
            if item.weight() > heavy_weight:
                heavy_weight = item.weight()
                heaviest_item = item

        return heaviest_item

class CargoHold:

    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__cargo = []
        self.__total_weight = 0

    def add_suitcase(self, suitcase: Suitcase):
        if self.__total_weight < self.__max_weight and self.__total_weight + suitcase.weight() < self.__max_weight:
            self.__cargo.append(suitcase)
            self.__total_weight += suitcase.weight()

    def __str__(self):
        if len(self.__cargo) == 1:
            return f"{len(self.__cargo)} suitcase, space for {self.__max_weight - self.__total_weight} kg"
        return f"{len(self.__cargo)} suitcases, space for {self.__max_weight - self.__total_weight} kg"

    def print_items(self):
        for suitcase in self.__cargo:
            suitcase.print_items()

