from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemSchema

blp = Blueprint('items', 'items', url_prefix='/items', description='Operations on items')

items = []

@blp.route('/')
class ItemList(MethodView):
    @blp.response(200)
    def get(self):
        return items
    
    @blp.arguments(ItemSchema)
    @blp.response(201, description="Item added")
    def post(self, new_data):
        items.append(new_data)
        return new_data
    
    @blp.route('/<int:item_id>')
    class Item(MethodView):
        @blp.response(200)
        def get(self, item_id):
            item = next((item for item in items if item['id'] == item_id), None)
            if item is None:
                abort(404, message='Item not found')
            return item

        @blp.arguments(ItemSchema)
        @blp.reponse(200, description='Item updated')
        def put(self, new_data, item_id):
            item = next((item for item in items if item['id'] == item_id), None)
            if item is None:
                abort(404, message='Item not found')
            item.update(new_data)
            return item
    
    @blp.response(204, description='Item deleted')
    def delete(self, item_id):
        global items
        if not any(item for item in items if item['id'] == item_id):
            abort(404, message='Item not found')
        items = [item for item in  items if item['id'] != item_id]
        return ''
