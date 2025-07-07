def process_products(products):
    for product in products:
        if product.get("category") == "Monitori":
            product["price"] = round(product["price"] * 1.1, 2)

        description = product.get("description")
        if description:
            description = description.replace("brzina", "performanse").replace("Brzina", "Performanse")
            product["description"] = description

    return products

def filter_and_search(products, category=None, search=None):
    filtered = products
    if category:
        filtered = [p for p in filtered if p.get("category") == category]
    if search:
        filtered = [p for p in filtered if search.lower() in p.get("name", "").lower()]
    return filtered
