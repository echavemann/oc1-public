import time
class Item():

    def __init__(self, cost, components):
        self.cost = cost
        self.components = components

    def get_cost(self):
        return self.cost
    def get_components(self):
        return self.components

class C5API():
    
    def __init__(self, items):
        self.items = set(items)
        self.x = 0.1
        self.y = 0.1

    def get_item_components(self, item):
        if item in self.items:
            time.sleep(self.x)
            self.x+=-0.1
            return item.get_components().copy()
        return []
    
    def get_delivery_cost(self, item):
        if item in self.items:
            time.sleep(self.y)
            self.y+=-0.1
            return item.get_cost()
        return float("inf")