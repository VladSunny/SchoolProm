# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Hardcoded data
categories = {
    'smartphones': {
        'name': 'Smartphones',
        'icon': '/static/images/smartphone-icon.png',
        'products': [
            {
                'id': 1,
                'name': 'iPhone 14',
                'price': 800,
                'stock': 10,
                'images': ['/static/images/iphone14-1.jpg', '/static/images/iphone14-2.jpg', '/static/images/iphone14-3.jpg'],
                'description': 'Latest iPhone with great camera.',
                'reviews': ['Great phone!', 'Battery lasts long.', 'Expensive but worth it.'],
                'hit': True,
                'photos_count': 3,
                'reviews_count': 3
            },
            {
                'id': 2,
                'name': 'Samsung S23',
                'price': 700,
                'stock': 15,
                'images': ['/static/images/s23-1.jpg', '/static/images/s23-2.jpg', '/static/images/s23-3.jpg', '/static/images/s23-4.jpg'],
                'description': 'Android flagship with amazing display.',
                'reviews': ['Smooth performance.', 'Good value.'],
                'hit': False,
                'photos_count': 4,
                'reviews_count': 2
            },
            {
                'id': 3,
                'name': 'Google Pixel 8',
                'price': 600,
                'stock': 5,
                'images': ['/static/images/pixel8-1.jpg', '/static/images/pixel8-2.jpg', '/static/images/pixel8-3.jpg'],
                'description': 'Pure Android experience.',
                'reviews': ['Best camera.', 'Updates forever.', 'Compact size.'],
                'hit': False,
                'photos_count': 3,
                'reviews_count': 3
            },
            {
                'id': 4,
                'name': 'OnePlus 11',
                'price': 550,
                'stock': 20,
                'images': ['/static/images/oneplus11-1.jpg', '/static/images/oneplus11-2.jpg', '/static/images/oneplus11-3.jpg', '/static/images/oneplus11-4.jpg', '/static/images/oneplus11-5.jpg'],
                'description': 'Fast charging and performance.',
                'reviews': ['Value for money.'],
                'hit': True,
                'photos_count': 5,
                'reviews_count': 1
            }
        ]
    },
    'laptops': {
        'name': 'Laptops',
        'icon': '/static/images/laptop-icon.png',
        'products': [
            {
                'id': 1,
                'name': 'MacBook Air',
                'price': 1000,
                'stock': 8,
                'images': ['/static/images/macair-1.jpg', '/static/images/macair-2.jpg', '/static/images/macair-3.jpg', '/static/images/macair-4.jpg'],
                'description': 'Light and powerful.',
                'reviews': ['Silent operation.', 'Long battery.', 'Premium build.', 'Great for work.'],
                'hit': True,
                'photos_count': 4,
                'reviews_count': 4
            },
            {
                'id': 2,
                'name': 'Dell XPS',
                'price': 1200,
                'stock': 12,
                'images': ['/static/images/xps-1.jpg', '/static/images/xps-2.jpg', '/static/images/xps-3.jpg'],
                'description': 'Infinity edge display.',
                'reviews': ['Beautiful screen.', 'Powerful specs.', 'A bit pricey.'],
                'hit': False,
                'photos_count': 3,
                'reviews_count': 3
            },
            {
                'id': 3,
                'name': 'HP Spectre',
                'price': 1100,
                'stock': 10,
                'images': ['/static/images/spectre-1.jpg', '/static/images/spectre-2.jpg', '/static/images/spectre-3.jpg', '/static/images/spectre-4.jpg'],
                'description': 'Convertible laptop.',
                'reviews': ['Versatile.', 'Good keyboard.'],
                'hit': False,
                'photos_count': 4,
                'reviews_count': 2
            },
            {
                'id': 4,
                'name': 'Lenovo ThinkPad',
                'price': 900,
                'stock': 15,
                'images': ['/static/images/thinkpad-1.jpg', '/static/images/thinkpad-2.jpg', '/static/images/thinkpad-3.jpg', '/static/images/thinkpad-4.jpg', '/static/images/thinkpad-5.jpg'],
                'description': 'Durable business laptop.',
                'reviews': ['Reliable.', 'Great trackpoint.', 'Expandable.'],
                'hit': True,
                'photos_count': 5,
                'reviews_count': 3
            }
        ]
    }
}

# For comparison, using smartphones as example
comparison_category = 'smartphones'

@app.route('/')
def index():
    return render_template('index.html', categories=categories)

@app.route('/category/<cat_id>')
def category(cat_id):
    if cat_id not in categories:
        return "Category not found", 404
    cat = categories[cat_id]
    view = request.args.get('view', 'grid')
    page = int(request.args.get('page', 1))
    per_page = 3
    start = (page - 1) * per_page
    end = start + per_page
    products = cat['products'][start:end]
    total_pages = (len(cat['products']) + per_page - 1) // per_page
    return render_template('category.html', cat=cat, products=products, view=view, page=page, total_pages=total_pages, cat_id=cat_id, categories=categories)

@app.route('/product/<cat_id>/<int:prod_id>')
def product(cat_id, prod_id):
    if cat_id not in categories:
        return "Category not found", 404
    prod = next((p for p in categories[cat_id]['products'] if p['id'] == prod_id), None)
    if not prod:
        return "Product not found", 404
    return render_template('product.html', prod=prod, cat_name=categories[cat_id]['name'], categories=categories)

@app.route('/comparison')
def comparison():
    cat = categories[comparison_category]
    products = cat['products']
    min_price = min(p['price'] for p in products)
    return render_template('comparison.html', products=products, min_price=min_price, cat_name=cat['name'], categories=categories)

if __name__ == '__main__':
    app.run(debug=True)