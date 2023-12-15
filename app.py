
from Commons.Utiles import config


def create():
    app = config.app


    return app


if __name__ == "__main__":
    create().run()
