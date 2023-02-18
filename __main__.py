from flask import Flask
from sqlalchemy.orm import sessionmaker

from db_api.base import create_all
from db_api.funcs.engine import create_db_engine
from db_api.funcs.session_maker import create_db_factory
from middlewares.db_middleware import DBMiddleware
from views.main.main_main import main_page


def setup_middlewares(app: Flask, db_factory: sessionmaker):
    DBMiddleware(app, db_factory)


def create_app(db_factory: sessionmaker) -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'SUPERSECRET'

    app.register_blueprint(main_page)

    setup_middlewares(app, db_factory)

    return app


def main():
    db_engine = create_db_engine('postgresql+psycopg2://user_1:test123@localhost/users')
    db_factory = create_db_factory(db_engine)

    app = create_app(db_factory)

    create_all(db_engine)

    try:
        app.run(host='127.0.0.1', port=5000)
    except KeyboardInterrupt:
        db_factory.close_all()


if __name__ == '__main__':
    main()