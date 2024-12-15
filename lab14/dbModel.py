from struct import Struct


def strValidator(string: str):
    try:
        if len(string) > 255:
            return False, b""
        return True, string.encode("utf-8")
    except:
        return False, b""


def intValidator(string: str):
    try:
        num = int(string)
        if num < 0:
            return False, 0
        return True, num
    except:
        return False, 0


def floatValidator(string: str):
    try:
        num = float(string)
        if num < 0:
            return False, 0
        return True, num
    except:
        return False, 0


def boolValidator(string: str):
    valid = {"true": True, "1": True, "yes": True}
    return True, valid.get(string, False)


MODEL = {
    "name": {
        "name": "Название",
        "enc_type": "128s",
        "default": "Пустое название".encode('utf-8'),
        "validator": strValidator,
        "offset": 0,
    },
    "price": {
        "name": "Цена",
        "enc_type": "I",
        "default": 0,
        "validator": intValidator,
        "offset": 1,
    },
    "volume": {
        "name": "Объем",
        "enc_type": "f",
        "default": 0.0,
        "validator": floatValidator,
        "offset": 2,
    },
    "is_diet": {
        "name": "С сахаром",
        "enc_type": "?",
        "default": False,
        "validator": boolValidator,
        "offset": 3,
    },
}


def decodeEntry(entry_bytes: bytes):
    data = STRUCT.unpack(entry_bytes)
    return [
        (val.decode("utf-8").replace("\x00", "") if isinstance(val, bytes) else val)
        for val in data
    ]


fmt = ">" + "".join([el["enc_type"] for el in MODEL.values()])
STRUCT = Struct(fmt)
