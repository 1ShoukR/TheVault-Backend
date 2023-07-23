class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class UserAlreadyExistsError(CustomError):
    def __init__(self, field, value):
        message = f"User with {field} '{value}' already exists."
        super().__init__(message)

class UserCreationError(CustomError):
    def __init__(self, reason):
        message = f"Error creating user: {reason}"
        super().__init__(message)