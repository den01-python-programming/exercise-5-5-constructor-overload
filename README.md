# Exercise 5.5 Constructor overload

The exercise template has a class `Product`, which represents a product in a shop. Every product has a name, location and weight.

Add the following constructor to the `Product` class:

 - `def __init__(String name)` creates a product with the given name. Its location is set to "shelf" and its weight is set to 1.

 Use a `@classmethod` statement to overload the constructors with the below:
 -  `Product.with_location(name, location)` creates a product with the given name and the given location. Its weight is set to 1.
 - `Product.with_weight(name, weight)` creates a product with the given name and the given weight. Its location is set to "shelf".

You can test your program with the following code:


```python
tape_measure = Product("Tape measure")
plaster = Product.with_location("Plaster", "home improvement section")
tyre = Product.with_weight("Tyre", 5)

print(tape_measure)
print(plaster)
print(tyre)
```

```plaintext
Tape measure (1 kg) can be found from the shelf
Plaster (1 kg) can be found from the home improvement section
Tyre (5 kg) can be found from the shelf
```
