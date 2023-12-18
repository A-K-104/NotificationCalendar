from flask import Flask

from Common.Utiles.config import scheduler_bl
from Domain.Init.flask_init import init_flask
from EntryPoint.Controllers.event_controller import app as event_controller
from EntryPoint.Controllers.swagger_controller import swagger_ui_blueprint
from EntryPoint.Controllers.user_controller import app as user_controller
from EntryPoint.Controllers.venue_controller import app as venue_controller


def create():
    app = Flask(__name__)

    app.register_blueprint(user_controller)
    app.register_blueprint(venue_controller)
    app.register_blueprint(event_controller)
    app.register_blueprint(swagger_ui_blueprint)

    scheduler_bl.register_jobs_from_scheduler_db()

    return app


if __name__ == "__main__":
    init_flask()
    create().run()
