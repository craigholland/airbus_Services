"""`main` is the top level module  of airbus Services."""

# Import the Pyramid Framework
from pyramid.config import Configurator
from pyramid.response import Response

from CartItems.routes import routes as cart_item_routes
from CartProfile.routes import routes as cart_profile_routes
from Inventory.routes import routes as inventory_routes
from Product.routes import routes as product_routes
from ProductOptions.routes import routes as product_option_routes
from User.routes import routes as user_routes

config = Configurator()


def root_page(request):
    """Main Page."""

    return Response('Service API')


_routes = [
    ('root', '/', root_page)
]

routes = (_routes + cart_item_routes + cart_profile_routes +
          inventory_routes + product_routes + product_option_routes +
          user_routes)

for route in routes:
    name, uri, handler = route
    config.add_route(name, uri)
    config.add_view(handler, route_name=name)

app = config.make_wsgi_app()
