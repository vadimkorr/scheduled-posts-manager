from flask import Flask, render_template, request, abort, jsonify
from datetime import datetime
from uuid import uuid4
app = Flask(__name__)

date_time_started = datetime.now()


@app.route('/')
def status():
    status = {'date_time_started': date_time_started}
    return render_template('home.html', status=status)


@app.route('/api/v1.0/posts/<id>')
def get_posts(id):
    return 'Post id: %s' % id


@app.route('/api/v1.0/posts/')
def get_post():
    return 'Post id: %s' % id


@app.route('/api/v1.0/posts/new', methods=['POST'])
def add_posts():
    if not request.json:
        abort(400)
    post = {
        'id': str(uuid4()),
        'message': request.json['message']
    }
    return jsonify(post), 201


if __name__ == '__main__':
    app.run(host='localhost', port='5005', debug=True)
