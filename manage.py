import os

from flask_script import Manager
from main.create_app import create_app
from blueprint import blueprint

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()
manager = Manager(app)


@manager.command
def run():
    app.run(host='localhost', port='5005', debug=True)


if __name__ == '__main__':
    manager.run()
