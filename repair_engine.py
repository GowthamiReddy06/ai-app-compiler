def repair_schema(schema, errors):

    if "ui_schema" not in schema:
        schema["ui_schema"] = {}

    if "api_schema" not in schema:
        schema["api_schema"] = {}

    if "db_schema" not in schema:
        schema["db_schema"] = {}

    if "auth_rules" not in schema:
        schema["auth_rules"] = {}

    return schema