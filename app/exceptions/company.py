class BaseAppError(Exception):
    """Виняток базової програми"""

class EmailAlreadyExistsError(BaseAppError):
    """Помилка: email вже існує"""

class CompanyNotFoundError(BaseAppError):
    """Компанія не знайдена"""