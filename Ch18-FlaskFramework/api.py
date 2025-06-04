from flask import Flask, jsonify, request

app = Flask(__name__)

##Initial Data in my to do list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
    {"id": 3, "name": "Item 3", "description": "This is item 3"},
    {"id": 4, "name": "Item 4", "description": "This is item 4"}
]

#home page
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the To-Do List API!"

#get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200


#get a specific item by id
@app.route('/item/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item), 200
    else:
        return jsonify({"error": "Item not found"}), 404
    
#create a new item
@app.route('/item', methods=['POST'])
def create_item():
    if not request.json or'name' not in request.json:
        return jsonify({"error": "Bad request"}), 400
    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json.get('description', "")
    }
    items.append(new_item)
    return jsonify(new_item), 201

#update an existing item
@app.route('/item/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item), 200
    
#delete an item
@app.route('/item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": "Item deleted"}), 200


'''
run the Flask application
To run this application, save it as api.py and run the command:
python api.py
'''
if __name__ == '__main__':
    app.run(debug=True, port=8000)
