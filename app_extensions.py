from flask_mongoengine import MongoEngine
from flasgger import Swagger

swagger_info = {
    "swagger": "2.0",
    "info": {
        "title": "User-Store",
        "description": "User-Store API",
        "contact": {
            "responsibleOrganization": "ME",
            "responsibleDeveloper": "Muhammad Nahid",
            "email": "mdnahid22@gmail.com",
            "url": "http://github.com/nahid111",
        },
        "termsOfService": "#",
        "version": "0.0.1"
    },
    # "host": "user-store.com",  # overrides localhost:500
    "basePath": "",  # base bash for blueprint registration
    "schemes": [
        "http",
        # "https"
    ]
}

db = MongoEngine()
swagger = Swagger(template=swagger_info)
