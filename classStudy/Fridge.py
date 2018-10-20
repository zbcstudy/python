# 定义一个类
class Fridge:
    def __init__(self, items={}):
        if type(items) != type({}):
            raise TypeError("Fridge requires a dictionary but was given %s", str(type(items)))
        self.items = items
        return

    def add_one(self, food_name):
        if type(food_name) != type(""):
            raise TypeError("Fridge requires a string but was given %s", str(type(food_name)))
        self._add_mulity(food_name, 1)
        return True

    def add_many(self, food_dict):
        if type(food_dict) != type({}):
            raise TypeError("Fridge requires a dictionary but was given %s", str(type(food_dict)))
        for item in food_dict.keys():
            self._add_mulity(item, food_dict[item])
        return

    def _add_mulity(self, food_name, num):
        if not food_name in self.items:
            self.items[food_name] = 0
        self.items[food_name] = self.items[food_name] + num

    def has_various(self, foods):
        try:
            for food in foods.keys():
                if self.items[food] < foods[food]:
                    return False
            return True
        except KeyError:
            return False

    def has(self, food_name, quality=1):
        return self.has_various({food_name: quality})


f = Fridge()
f.items = {"cheese": 2, "tomato": 4, "milk": 3}
f.add_one("apple")
f.add_many({"egg": 5, "grape": 9})
print(f.items)
print(f.has("egg", 7))

