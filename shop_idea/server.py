from flask import Flask, request, jsonify

app = Flask(__name__)

shop = {
    'apple': 10,
    'banana': 20,
    'orange': 15
}

@app.route('/shop', methods=['GET'])
def show_shop():
    return jsonify({'message': 'GET request successful', 'data': shop})

@app.route('/shop/add', methods=['POST'])
def add_item():
    data = request.get_json()
    item = data.get('item')
    quantity = data.get('quantity')
    if item and quantity is not None:
        shop[item] = quantity
        return jsonify({'message': 'Item added successfully', 'data': shop}), 201
    else:
        return jsonify({'message': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=67)