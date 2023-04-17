class Ads:
    def __init__(self, _id: str, _name: str = '', _price: float = 0):
        self.id = _id
        self.name = _name
        self.price = _price

    def __str__(self):
        return f'{self.__class__.__name__}(id:{self.id}, price:{self.price})'

    def get_price(self):
        return self.price

# class ClassicAds(Ads):
#     def __init__(self, _id: str, _name: str = '', _price: float = 0):
#         super().__init__(_id, _name, _price)
#         self.feature = 'Offers the most basic level of advertisement'
#
#
# class StandoutAds(Ads):
#     def __init__(self, _id: str, _name: str = '', _price: float = 0):
#         super().__init__(_id, _name, _price)
#         self.feature = 'Allows advertisers to use a company logo and use a longer presentation text'
#
#
# class PremiumAds(Ads):
#     def __init__(self, _id: str, _name: str = '', _price: float = 0):
#         super().__init__(_id, _name, _price)
#         self.feature = 'Same benefits as Standout Ad, but also puts the advertisement at the top of the results,
#         allowing higher visibility'


class Offer:
    def __init__(self, _type: str, item_count: int = 0, _price: float = 0):
        self.type = _type  # 'deal', 'discount'
        self.threshold_item_count = item_count
        self.price = _price

    def __str__(self):
        return f'Offer(type:{self.type}, threshold_item_count:{self.threshold_item_count}, price:{self.price})'


class PricingRules:
    def __init__(self):
        self.inventory = {}
        self.offers = {}

    def create_new_ads(self, ads_id: str, name: str, price: float):
        self.inventory[ads_id] = Ads(ads_id, name, price)

    def create_new_offer(self, customer: str, ads_id: str, offer: dict):
        if customer not in self.offers:
            self.offers[customer] = {}

        if offer['type'] == 'deal':
            offer['price'] = (offer['charge_item'] / offer['target_item']) * self.inventory[ads_id].get_price()

        self.offers[customer][ads_id] = Offer(offer['type'], offer['target_item'], offer['price'])


class Checkout:
    def __init__(self, pricing_rules: PricingRules):
        self.pricing_rules = pricing_rules
        self._total = 0
        self.item_count = {}
        self.privileged_customer = None

    def reset(self):
        self._total = 0
        self.item_count = {}
        self.privileged_customer = None

    def total(self):
        if self.privileged_customer is None or self.privileged_customer not in self.pricing_rules.offers:
            for item_id in self.item_count:
                self._total += self.item_count[item_id] * self.pricing_rules.inventory[item_id].get_price()
            return self._total

        for item_id in self.item_count:
            if item_id in self.pricing_rules.offers[self.privileged_customer]:
                offer = self.pricing_rules.offers[self.privileged_customer][item_id]
                if offer.type == 'deal':
                    multiple_target_items = self.item_count[item_id] // offer.threshold_item_count
                    self._total += multiple_target_items * offer.threshold_item_count * offer.price
                    self._total += (self.item_count[item_id] % offer.threshold_item_count) * \
                                   self.pricing_rules.inventory[item_id].get_price()
                elif offer.type == 'discount' and self.item_count[item_id] >= offer.threshold_item_count:
                    self._total += self.item_count[item_id] * offer.price
                else:
                    self._total += self.item_count[item_id] * self.pricing_rules.inventory[item_id].get_price()
            else:
                self._total += self.item_count[item_id] * self.pricing_rules.inventory[item_id].get_price()

        return self._total

    def set_customer(self, _customer):
        self.privileged_customer = _customer

    def add(self, item_id):
        if item_id not in self.item_count:
            self.item_count[item_id] = 0
        self.item_count[item_id] += 1


if __name__ == "__main__":
    pr = PricingRules()
    pr.create_new_ads('classic', 'Classic Ad', 269.99)
    pr.create_new_ads('standout', 'Standout Ad', 322.99)
    pr.create_new_ads('premium', 'Premium Ad', 394.99)

    pr.create_new_offer('UNILEVER', 'classic', {'type': 'deal', 'target_item': 3, 'charge_item': 2})
    pr.create_new_offer('APPLE', 'standout', {'type': 'discount', 'target_item': 1, 'price': 299.99})
    pr.create_new_offer('NIKE', 'premium', {'type': 'discount', 'target_item': 4, 'price': 379.99})
    pr.create_new_offer('FORD', 'classic', {'type': 'deal', 'target_item': 5, 'charge_item': 4})
    pr.create_new_offer('FORD', 'APPLE', {'type': 'discount', 'target_item': 1, 'price': 309.99})
    pr.create_new_offer('FORD', 'premium', {'type': 'discount', 'target_item': 3, 'price': 389.99})

    co = Checkout(pr)
    co.add('classic')
    co.add('standout')
    co.add('premium')
    print('Total (default): ', co.total(), '$987.97')

    co.reset()
    co.set_customer('UNILEVER')
    co.add('classic')
    co.add('classic')
    co.add('classic')
    co.add('premium')
    print('Total (UNILEVER): ', co.total(), '$934.97')

    co.reset()
    co.set_customer('APPLE')
    co.add('standout')
    co.add('standout')
    co.add('standout')
    co.add('premium')
    print('Total (APPLE): ', co.total(), '$1294.96')

    co.reset()
    co.set_customer('NIKE')
    co.add('premium')
    co.add('premium')
    co.add('premium')
    co.add('premium')
    print('Total (NIKE): ', co.total(), '$1519.96')

    co.reset()
    co.set_customer('FORD')
    co.add('classic')
    co.add('premium')
    co.add('classic')
    co.add('standout')
    co.add('classic')
    co.add('premium')
    co.add('classic')
    co.add('premium')
    co.add('classic')
    co.add('premium')
    co.add('classic')
    print('Total (FORD): ', co.total(), '$3232.9')

    co.reset()
    co.set_customer('UNILEVER')
    co.add('classic')
    co.add('classic')
    co.add('classic')
    co.add('premium')
    co.add('classic')
    co.add('classic')
    co.add('classic')
    co.add('classic')
    co.add('classic')
    co.add('classic')
    co.add('standout')
    co.add('classic')
    print('Total (UNILEVER): ', co.total(), '$2607.91')
