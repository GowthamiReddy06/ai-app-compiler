def extract_intent(prompt):

    prompt = prompt.lower()

    features = []

    keywords = [
        "login",
        "dashboard",
        "contacts",
        "payments",
        "analytics"
    ]

    for k in keywords:
        if k in prompt:
            features.append(k)

    return {
        "app_name": "Generated App",
        "features": features,
        "roles": ["admin", "user"]
    }