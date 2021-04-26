"""
CP1404 Week 6 Lecture 1 do this now
List comprehension - checks whether a product is on sale
"""

products = [["Phone", 340, False], ["PC", 1420.95, True],["Plant", 24.5, True]]
on_sale_products = []

for product in products:
    if product[2]:
        on_sale_products.append(product)
print(on_sale_products)
