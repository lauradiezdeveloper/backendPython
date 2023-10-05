class Product:
    name: str
    price: float
    category: str

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def __added_to_cart__(self):
        print("Product {self.name} added to cart")

    def __deleted_from_cart__(self):
        print("Product {self.name} deleted from cart")

    def __outofstock__(self):
        print("Product {self.name} is out of stock")
        print("Please select another product")



class CustomProduct(Product):
    custom: str

    def __init__(self, name, price, category, custom):
        super().__init__(name, price, category)
        self.name = name
        self.price = price 
        self.category = category
        self.custom = custom

    def __added_custom_price__(self):
        if self.custom == "yes":
            self.price +100
            print("Product {self.name} added to cart")
            print("Customized product price: {self.price}")
        else:
            print("Please customize your product")



product1 = Product("iPhone", 1000, "Phone")
product2 = Product("Xiaoºmi", 500, "Phone")

customproduct1 = CustomProduct("iPhone", 1000, "Phone", "yes")