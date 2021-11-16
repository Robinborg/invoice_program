from models.product import Product

class ProductHandler:
    def __init__(self):
        #Start session here?
        engine = #Get from function?
        self.session = engine

    def get_all_customers(self):
        self.session.query(customers).all()

    def add_one_product(self):
        self.session.query(customers).add_entity()

    def remove(self):
        self.session.query(customers).delete()

    def search(self, looking_for):
        self.session.query(customers).get(looking_for)

