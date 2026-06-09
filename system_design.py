def design_system(intent):

    return {
        "entities": [
            "User",
            "Contact"
        ],
        "pages": [
            "Login",
            "Dashboard",
            "Contacts"
        ],
        "roles": intent["roles"]
    }