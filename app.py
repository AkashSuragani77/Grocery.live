from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Grocery products with image URLs
products = [
    # Fruits (by dozen)
    {'id': 1, 'name': 'Apple', 'price': 120, 'unit': 'dozen', 'image': 'https://images.unsplash.com/photo-1567306226416-28f0efdc88ce?auto=format&fit=crop&w=400&q=60'},
    {'id': 2, 'name': 'Banana', 'price': 60, 'unit': 'dozen', 'image': 'https://www.jiomart.com/images/product/original/590000454/banana-robusta-1-kg-product-images-o590000454-p590000454-0-202410011654.jpg?im=Resize=(420,420)'},
    {'id': 3, 'name': 'Orange', 'price': 100, 'unit': 'dozen', 'image': 'https://cdn-prod.medicalnewstoday.com/content/images/articles/272/272782/oranges-in-a-box.jpg'},
    {'id': 4, 'name': 'Pineapple', 'price': 90, 'unit': 'dozen', 'image': 'https://5.imimg.com/data5/MG/VC/OC/SELLER-89004543/fresh-pineapple-281kg-29-500x500-500x500.png'},
    {'id': 5, 'name': 'Mango', 'price': 150, 'unit': 'dozen', 'image': 'https://i0.wp.com/post.medicalnewstoday.com/wp-content/uploads/sites/3/2022/01/mangoes_what_to_know_1296x728_header-1024x575.jpg?w=1155&h=1528'},
    {'id': 6, 'name': 'Papaya', 'price': 80, 'unit': 'dozen', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTW-QmKlo1pDP1ahUd55Sc_96nRjkXREeh4yA&s'},
    {'id': 7, 'name': 'Grapes', 'price': 140, 'unit': 'dozen', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCaSUv7rhNDxj6yq2R3a4kes3rLpSeRsQu8Q&s'},
    {'id': 8, 'name': 'Guava', 'price': 70, 'unit': 'dozen', 'image': 'https://cdn.britannica.com/59/139059-050-30794D53/Guava-fruit.jpg'},
    {'id': 9, 'name': 'Pomegranate', 'price': 130, 'unit': 'dozen', 'image': 'https://rukminim3.flixcart.com/image/850/1000/xif0q/plant-seed/o/1/x/25-vlr-138-pomegranate-tree-seed-punica-granatum-25-seeds-vibex-original-imagggaf2dazyshm.jpeg?q=90&crop=false'},
    {'id': 10, 'name': 'Lemon', 'price': 50, 'unit': 'dozen', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJhgLmTWMetMSXmVt7bXQqoTmaVl5IxPwu9Q&s'},

    # Vegetables (by kg)
    {'id': 11, 'name': 'Tomato', 'price': 40, 'unit': 'kg', 'image': 'https://www.thespruceeats.com/thmb/PXkn3CCiNQSClbfRCsGfPAEpyRs=/4460x2974/filters:fill(auto,1)/growers-and-enthusiasts-enjoy-the-rhs-london-harvest-festival-show-456787858-58110a625f9b58564c6bb051.jpg'},
    {'id': 12, 'name': 'Carrot', 'price': 35, 'unit': 'kg', 'image': 'https://img3.exportersindia.com/product_images/bc-full/dir_73/2189649/carrot-1910303.jpg'},
    {'id': 13, 'name': 'Potato', 'price': 25, 'unit': 'kg', 'image': 'https://www.tasteofhome.com/wp-content/uploads/2022/07/GettyImages-1224918845-e1658929817975.jpg?w=2036'},
    {'id': 14, 'name': 'Onion', 'price': 30, 'unit': 'kg', 'image': 'https://4.bp.blogspot.com/-ZgO8JEjCGPg/UCiKLMyzA4I/AAAAAAAADCA/riL5eSPL8bs/s1600/file0001628903495.jpg'},
    {'id': 15, 'name': 'Capsicum', 'price': 60, 'unit': 'kg', 'image': 'https://cdn.shopify.com/s/files/1/0286/8586/0898/products/Capsicum_Green_1024x1024.jpg?v=1593836720'},
    {'id': 16, 'name': 'Cabbage', 'price': 28, 'unit': 'kg', 'image': 'https://assets.clevelandclinic.org/transform/871f96ae-a852-4801-8675-683191ce372d/Benefits-Of-Cabbage-589153824-770x533-1_jpg'},
    {'id': 17, 'name': 'Cauliflower', 'price': 30, 'unit': 'kg', 'image': 'https://media-cdn2.greatbritishchefs.com/media/xuaop4pn/cauliflower.whqc_768x512q90.jpg'},
    {'id': 18, 'name': 'Brinjal', 'price': 40, 'unit': 'kg', 'image': 'https://pushtiorganics.com/cdn/shop/files/Brinjal_d2d7db50-62dd-4b99-af45-9f0adf46703d_1200x.png?v=1709270808'},
    {'id': 19, 'name': 'Spinach', 'price': 20, 'unit': 'kg', 'image': 'https://www.greendna.in/cdn/shop/files/palak2_1200x1200.jpg?v=1715600291'},
    {'id': 20, 'name': 'Cucumber', 'price': 32, 'unit': 'kg', 'image': 'https://gardenerspath.com/wp-content/uploads/2021/05/Types-of-Cucumbers-FB.jpg'},

    # Grains (by kg)
    {'id': 21, 'name': 'Rice', 'price': 60, 'unit': 'kg', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRVE8BJzmsMe5y7ND_appSZ5WWvEl1UOPfnA&s'},
    {'id': 22, 'name': 'Wheat', 'price': 50, 'unit': 'kg', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDGVppZEiF6qL0cZuABDH4uBy6ROp3ON8tkQ&s'},
    {'id': 23, 'name': 'Barley', 'price': 45, 'unit': 'kg', 'image': 'https://goodness-farm.com/wp-content/uploads/2023/04/barley.jpg'},
    {'id': 24, 'name': 'Maize', 'price': 55, 'unit': 'kg', 'image': 'https://www.peptechbio.com/wp-content/uploads/2023/09/wouter-supardi-salari-HE_MjmWh9eQ-unsplash-scaled.jpg'},
    {'id': 25, 'name': 'Lentils', 'price': 80, 'unit': 'kg', 'image': 'https://www.themediterraneandish.com/wp-content/uploads/2024/10/Guide-To-Lentils-Graphic-Horizontal-1.jpg'},
    {'id': 26, 'name': 'Chickpeas', 'price': 70, 'unit': 'kg', 'image': 'https://media.post.rvohealth.io/wp-content/uploads/2021/10/chickpeas-732x549-thumbnail.jpg'},
    {'id': 27, 'name': 'Millet', 'price': 60, 'unit': 'kg', 'image': 'https://arrowheadmills.com/wp-content/uploads/2022/10/puffed-millet-9-1024x656.jpg'},
    {'id': 28, 'name': 'Quinoa', 'price': 120, 'unit': 'kg', 'image': 'https://5.imimg.com/data5/SELLER/Default/2024/6/424055315/MH/PV/ML/25044508/white-quinoa-seeds-500x500.jpeg'},
    {'id': 29, 'name': 'Green Gram', 'price': 75, 'unit': 'kg', 'image': 'https://www.agrifarming.in/wp-content/uploads/Ultimate-Guide-to-Green-Gram-Farming-1.jpg'},
    {'id': 30, 'name': 'Black Gram', 'price': 85, 'unit': 'kg', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzDNaeEcxDrvQxAgDa-Hzo9tFKsOMdqa7n_Q&s'},
]

# Cart stored globally (single-user)
cart = []

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = int(request.form['product_id'])
    quantity = int(request.form['quantity'])

    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        existing_item = next((item for item in cart if item['id'] == product_id), None)
        if existing_item:
            existing_item['quantity'] += quantity
        else:
            cart.append({
                'id': product['id'],
                'name': product['name'],
                'price': product['price'],
                'unit': product['unit'],
                'image': product['image'],
                'quantity': quantity
            })

    return redirect(url_for('cart_view'))

@app.route('/cart')
def cart_view():
    total = sum(item['price'] * item['quantity'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/checkout')
def checkout():
    total = sum(item['price'] * item['quantity'] for item in cart)
    return render_template('checkout.html', cart=cart, total=total)

@app.route('/place_order', methods=['POST'])
def place_order():
    global cart
    if not cart:
        return redirect(url_for('cart_view'))

    # Simulate order processing by clearing the cart
    cart.clear()

    return render_template('placeorder.html')


@app.route('/clear_cart')
def clear_cart():
    cart.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
