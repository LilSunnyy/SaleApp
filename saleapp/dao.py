def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    }, {
        'id': 2,
        'name': 'Tablet'
    }]

def load_products(kw):
    products = [{
        'id': 1,
        'name': 'iPhone 15 Pro Max',
        'price': 24000000,
        'image': "https://i.imgur.com/Tzr2xoF.jpeg"
    }, {
            'id': 1,
            'name': 'iPhone 15 Pro Max',
            'price': 24000000,
            'image': "https://i.imgur.com/Tzr2xoF.jpeg"
    }, {
        'id': 1,
        'name': 'iPhone 15 Pro Max',
        'price': 24000000,
        'image': "https://i.imgur.com/Tzr2xoF.jpeg"
    }, {
        'id': 1,
        'name': 'iPhone 15 Pro Max',
        'price': 24000000,
        'image': "https://i.imgur.com/Tzr2xoF.jpeg"
    }]
    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products