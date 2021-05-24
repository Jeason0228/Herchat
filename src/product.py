from typing import List


class Product:
    sku: str
    title: str
    product_code: str
    assets: List[Asset]
    more_colors: bool
    size: str
    avg_color: str
    department_code: str
    family_code: str
    division_code: str
    price: int
    url: str
    slug: str
    has_stock: bool
    has_stock_retail: bool
    has_stock_or_has_stock_retail: bool
    stock: Stock
    personalize: bool

    def __init__(self, sku: str, title: str, product_code: str, assets: List[dict], more_colors: bool, size: str, avg_color: str, department_code: str, family_code: str, division_code: str, price: int, url: str, slug: str, has_stock: bool, has_stock_retail: bool, has_stock_or_has_stock_retail: bool, stock: dict, personalize: bool) -> None:
        self.sku = sku
        self.title = title
        self.product_code = product_code
        self.assets = assets
        self.more_colors = more_colors
        self.size = size
        self.avg_color = avg_color
        self.department_code = department_code
        self.family_code = family_code
        self.division_code = division_code
        self.price = price
        self.url = url
        self.slug = slug
        self.has_stock = has_stock
        self.has_stock_retail = has_stock_retail
        self.has_stock_or_has_stock_retail = has_stock_or_has_stock_retail
        self.stock = stock
        self.personalize = personalize
