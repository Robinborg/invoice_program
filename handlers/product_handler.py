from models.product import Product

class ProductHandler:
    def __init__(self):
        #Start session here?
        engine = #Get from function?
        self.session = engine

    def get_all_products(self):
        self.session.query(products).all()

    def add_one_product(self):
        self.session.query(products).add_entity()

    def remove(self):
        self.session.query(products).delete()

    def search(self, looking_for):
        self.session.query(products).get(looking_for)

