
from Commons.Utiles import config
from Doman.Init.flask_init import init_flask


def create():
    app = config.app


    return app


if __name__ == "__main__":
    init_flask()
    create().run()
