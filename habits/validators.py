from rest_framework import serializers


def connected_is_pleasant(value):
    # Проверяем что связанная привычка приятная
    if not value.is_pleasant:
        text = "Связанной привычкой может быть только приятная"
        raise serializers.ValidationError(text)


def is_under7(value):
    # Проверяем что значение от 1 до 7
    if not (0 < value < 8):
        text = "Нужно повторять действие не реже раза в неделю"
        raise serializers.ValidationError(text)


def is_under120(value):
    # Проверяем что значение от 1 до 120
    if not (0 < value < 121):
        text = "Длительность привычки должна быть " \
               "не больше 120 секунд"
        raise serializers.ValidationError(text)


def filled_only_one(value1, value2):
    # Проверяем что не может быть заполнены оба значения
    if not ((value1 == "" or value1 is None)
            or (value2 == "" or value2 is None)):
        text = "Может быть или вознаграждение или связанная " \
               "привычка, поправьте настройки"
        raise serializers.ValidationError(text)


def empty_both(value1, value2):
    # Проверяем что оба значения пусты
    if not ((value1 == "" or value1 is None)
            and (value2 == "" or value2 is None)):
        text = "У приятной привычки не может быть награждения " \
               "или связанной привычки, она сама по себе"
        raise serializers.ValidationError(text)
