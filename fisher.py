from flask import Flask, make_response

app = Flask(__name__)


app.config.from_object('config')


@app.route('/hello')
def hello():
    headers = {
        'content-type': 'text/plain'
    }
    response = make_response('<html></html>', 404)
    response.headers = headers
    return response


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])

