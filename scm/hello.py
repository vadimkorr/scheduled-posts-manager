from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

date_time_started = datetime.now()


@app.route('/')
def status():
    status = {'date_time_started': date_time_started}
    return render_template('home.html', status=status)


@app.route('/posts/<id>')
def get_posts(id):
    return 'Post id: %s' % id

# @app.route('/posts/new', methods=['POST'])
# def add_posts():
#     post = request.model
#     return 'New post model'


if __name__ == '__main__':
    app.run(host='localhost', port='5005', debug=True)
