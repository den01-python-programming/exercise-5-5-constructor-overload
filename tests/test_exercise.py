import pytest
from src.product import Product

def test_exercise():
    coffee_cup = Product("Coffee cup")
    car = Product.with_location("Car", "showroom")
    table = Product.with_weight("Table", 50)

    assert str(coffee_cup) == "Coffee cup (1 kg) can be found from the shelf"
    assert str(car) == "Car (1 kg) can be found from the showroom"
    assert str(table) == "Table (50 kg) can be found from the shelf"
