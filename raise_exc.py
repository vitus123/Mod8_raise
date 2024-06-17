
class ValidationError(Exception):
    pass


class InvalidDataException(Exception):
    pass


def person_age(age):
    if age < 0:
        raise InvalidDataException('Возраст не может быть отрицательным')
    elif age > 120:
        raise ValidationError('Возраст не может быть больше 120')
    return True


try:
    person_age(150)
except ValidationError as exc:
    print(exc)

try:
    person_age(-40)
except InvalidDataException as exc:
    print(exc)
