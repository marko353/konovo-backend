def process_products(products):
    processed = []

    for product in products:
        # Uvećaj cenu za monitore
        price = product.get("price", 0)
        if product.get("category") == "Monitori":
            price = round(price * 1.1, 2)

        # Obradi opis
        description = product.get("description", "")
        if description:
            description = description.replace("brzina", "performanse").replace("Brzina", "Performanse")

        # Kreiraj novi proizvod sa pravilnim ključevima
        processed.append({
            "id": product.get("sif_product"),            # ← ključno
            "naziv": product.get("naziv") or product.get("name"),
            "price": price,
            "categoryName": product.get("category") or product.get("categoryName") or "Ostalo",
            "description": description,
            "imgsrc": product.get("imgsrc"),
        })

    return processed


def filter_and_search(products, category=None, search=None):
    filtered = products

    if category:
        filtered = [p for p in filtered if p.get("categoryName") == category]

    if search:
        filtered = [p for p in filtered if search.lower() in p.get("naziv", "").lower()]

    return filtered
