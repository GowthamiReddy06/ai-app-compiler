def validate_schema(schema):

    errors = []

    required = [
        "ui_schema",
        "api_schema",
        "db_schema",
        "auth_rules"
    ]

    for item in required:

        if item not in schema:
            errors.append(
                f"Missing {item}"
            )

    return errors