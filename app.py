
from Commons.Utiles import config
from Doman.Init.flask_init import init_flask
from EntryPoints.Controllers.user_controller import app as user_controller
from EntryPoints.Controllers.venue_controller import app as venue_controller
from EntryPoints.Controllers.event_controller import app as event_controller


def create():
    app = config.app
    app.register_blueprint(user_controller)
    app.register_blueprint(venue_controller)
    app.register_blueprint(event_controller)

    return app


if __name__ == "__main__":
    init_flask()
    create().run()
