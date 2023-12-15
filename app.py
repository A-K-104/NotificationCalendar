
from Commons.Utiles import config
from Doman.Init.flask_init import init_flask
from EntryPoints.Controllers.user_controller import app as user_controller


def create():
    app = config.app
    app.register_blueprint(user_controller)

    return app


if __name__ == "__main__":
    init_flask()
    create().run()
