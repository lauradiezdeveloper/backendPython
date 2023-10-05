def list_items_available(products):
    print("List of products available: ")
    for product in products:
        print(f"Product: {product['name']} - Price: {product['price']}") 

def add_to_cart(product, cart):
    cart.append(product)
    print(f"Product {product['name']} added to cart")

def list_my_orders(orders):
    orderid = lambda order: order + 1
    def create_order(order):
        order = []
        return order
    create_order(orders)
    print("My orders:")
    for order in orders:
        print(orderid, "Order: {order['name']} - Price: {order['price']}")

def get_my_account_info(user):
    userid = lambda user: user + 1
    print("My account info:")
    print(f"Id: {userid}")
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"Password: {user['password']}")