from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_BASE_URL = '/swagger'
SWAGGER_API_URL = r'../static/swagger.json'

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_BASE_URL,
    SWAGGER_API_URL
)
