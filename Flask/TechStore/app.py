# app.py (updated to add cabinet route)
from flask import Flask, render_template, request, json
import os

app = Flask(__name__)

# Load product data from JSON file
with open('products.json', 'r', encoding='utf-8') as file:
    categories = json.load(file)

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

@app.route('/cabinet')
def cabinet():
    return render_template('cabinet.html', categories=categories)

if __name__ == '__main__':
    app.run(debug=True)