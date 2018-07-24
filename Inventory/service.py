
from pyramid.view import view_config
from pyramid.view import view_defaults

@view_defaults(accept = 'application/json', renderer='json')
class InventoryService(object):
    def __init__(self, request):
        self.request = request

    @view_config(request_method='GET')
    def get(self):
        # add the code that will do the look by id
        dummy_object = {
            'some_attr': 'some_value'
        }

        return dummy_object

    @view_config(request_method='PUT')
    def put(self):
        cart_item_dict = self.request.json_body

        # add the code to update by id
        # add the response


    @view_config(request_method='POST')
    def post(self):
        inventory = self.request.json_body

        # add code to store the object
        # ensure the object has an id

        return inventory  # this should be the saved object

    @view_config(request_method='DELETE')
    def delete(self):
        # git the id from the request
        # call the store to delete object
        pass
