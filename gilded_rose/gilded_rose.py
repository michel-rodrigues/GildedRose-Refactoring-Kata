from items import is_special_item, update_regular_item, update_special_item


class GildedRose():

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if is_special_item(item):
                update_special_item(item)
            else:
                update_regular_item(item)
