from models.user import User

def get_current_user():
    return User(id=1, email="test@example.com", hashed_password="fake")