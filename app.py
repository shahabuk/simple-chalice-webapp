from chalice import Chalice, Response, BadRequestError
from chalicelib.location_service import information_about
from chalicelib.index_html import index_html

app = Chalice(app_name='simple_web_app')


@app.route('/')
def index():
    return Response(body=index_html,
                    status_code=200,
                    headers={'Content-Type': 'text/html'})


@app.route('/location')
def location():
    place = app.current_request.query_params.get('place')
    result = information_about(place)
    if result:
        return result
    else:
        raise BadRequestError(f"Unknown place: {place}")
