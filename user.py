class User:
    """Keep username and token"""
    def __init__(self, name: str, token: str) -> None:
        self.name = name
        self.token = token
