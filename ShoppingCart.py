class ShoppingCart:
    items = []
    uniqueitems = ()

    def add_item(self, item):
        self.items.append(item)

    def show_cart(self):
        Items = self.items
        print(" items : ", Items)

    def RemoveItem(self, item):
        self.items.remove(item)
        print("item remove successfully")

    def CountTotalItems(self):

        print("Count of Total Items is : ", self.items.__len__())

    def ItemCounts(self, item):
        print(f"count of {item} is : ", self.items.count(item))

    def ClearCart(self):
        print("your cart is empty : ", self.items.clear())

    def show_unique(self):
        self.uniqueitems = set(self.items)
        print("unique items : ", self.uniqueitems)


cart1 = ShoppingCart()

start = True
while start:
    print("    ")
    print("==== Shopping Cart Menu ====")
    print("1. Add item")
    print("2. Show cart")
    print("3. Show unique items")
    print("4. Remove item")
    print("5. Show item counts")
    print("6. Count total items")
    print("7. Clear cart")
    print("8. Exit")
    print("============================")
    print("    ")
    number = int(input("Enter choice = "))
    match number:

        case 1:
            item = input("enter items name that you want to add in list : ")
            cart1.add_item(item)

        case 2:
            cart1.show_cart()

        case 3:
            cart1.show_unique()

        case 4:
            i = input("enter item that you want to remove from the cart : ")
            cart1.RemoveItem(i)

        case 5:
            item = input("enter item that you want to count : ")
            cart1.ItemCounts(item)

        case 6:
            # item = input("enter item to count")
            cart1.CountTotalItems()

        case 7:
            cart1.ClearCart()

        case 8:
            start = False
