from Common.Utiles import config
from Domain.Init.flask_init import init_flask
from EntryPoint.Controllers.event_controller import app as event_controller
from EntryPoint.Controllers.user_controller import app as user_controller
from EntryPoint.Controllers.venue_controller import app as venue_controller


def create():
    app = config.app
    app.register_blueprint(user_controller)
    app.register_blueprint(venue_controller)
    app.register_blueprint(event_controller)

    return app


if __name__ == "__main__":
    init_flask()
    create().run()
