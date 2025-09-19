class Product:
    last_id = -1

    def __init__(self, name: str, price: float, score: int) -> None:
        Product.last_id += 1
        self._id: int = Product.last_id
        self._name = name
        self._price = price
        self._score = score

        # all should be property
        self._factory = 1

        # factory only in class getter
        # only to read and not to change

        self._count = self._id


class Category:
    last_id = -1

    def __init__(self) -> None:
        Category.last_id += 1
        self._id: int = Category.last_id
        self._name = ""
        self._product_list: list[Product] = []
        self._category_dict: dict = {}

    def AddProductCategory(self, product_list: list[Product]):
        self._product_list += product_list

    def FilterByPrice(self, low_price: float, high_price: float):
        pass

    def ShowSupply(self):
        pass

    # sort


class People:
    def __init__(self) -> None:
        self.first_name: str
        self.last_name: str
        self.age: int
        self.phone_number: str
        # handle with regex


class Cart:
    def __init__(self, owner: People) -> None:
        self._cart_owner: People = owner
        self._product_list: list[Product]

    def AddProductToCart(self, product_list: list[Product]):
        self._product_list += product_list

    def CalculatePrice(self):
        message = f"\
{self._cart_owner.first_name}, \
{self._cart_owner.last_name}, \
{self._cart_owner.phone_number}\n\n"

        message += "Products: \n"
        for prod in self._product_list:
            message += prod + "\n"

        message += sum([prod._price * prod._id for prod in self._product_list])

        print(message)


# class Main:
