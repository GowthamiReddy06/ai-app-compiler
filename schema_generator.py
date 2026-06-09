def generate_schema(design):

    return {
        "ui_schema": {
            "pages": design["pages"]
        },

        "api_schema": {
            "endpoints": [
                {
                    "path": "/login",
                    "method": "POST"
                },
                {
                    "path": "/contacts",
                    "method": "GET"
                }
            ]
        },

        "db_schema": {
            "tables": [
                {
                    "name": "users",
                    "columns": [
                        "id",
                        "email",
                        "password"
                    ]
                }
            ]
        },

        "auth_rules": {
            "roles": design["roles"]
        }
    }