def strToBool(string: str) -> bool:
    if string == "True":
        return True
    elif string == "False":
        return False
    raise Exception("Ошибка при конвертации из str в bool!")


DB_MODEL = {
    "name": {
        "offset": 0,
        "type": str,
        "name": "Имя",
        "default": ""
    },
    "age": {
        "offset": 1,
        "type": int,
        "name": "Возраст",
        "default": 0
    },
    "profession": {
        "offset": 2,
        "type": str,
        "name": "Профессия",
        "default": ""
    },
    "weight": {
        "offset": 3,
        "type": float,
        "name": "Вес",
        "default": 0.0
    },
    "is_student": {
        "offset": 4,
        "type": strToBool,
        "name": "Студент",
        "default": False
    }
}