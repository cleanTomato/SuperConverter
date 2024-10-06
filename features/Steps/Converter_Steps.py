from behave import given, when, then

from Converter_Pr import convert_value

# Переменные для хранения состояния теста
input_system = None
input_unit = None
input_value = None
output_value = None
error_message = None


@given('я выбрал американскую систему')
def step_given_american_system(context):
    global input_system
    input_system = 1


@given('я выбрал старорусскую систему')
def step_given_old_russian_system(context):
    global input_system
    input_system = 2


@given('я выбрал международную систему')
def step_given_international_system(context):
    global input_system
    input_system = 3


@given('я выбрал дюйм')
def step_given_inch(context):
    global input_unit
    input_unit = 1


@given('я выбрал фут')
def step_given_foot(context):
    global input_unit
    input_unit = 2


@given('я выбрал ярд')
def step_given_yard(context):
    global input_unit
    input_unit = 3

@given('я выбрал километр')
def step_given_kilometr(context):
    global input_unit
    input_unit = 4


@given('я выбрал версту')
def step_given_versta(context):
    global input_unit
    input_unit = 4


@given('я выбрал метр')
def step_given_meter(context):
    global input_unit
    input_unit = 3


@given('я ввел значение {value:d}')
def step_given_value(context, value):
    global input_value
    input_value = value


@given('я ввел неверный выбор системы мер')
def step_given_invalid_system(context):
    global input_system
    input_system = 99  # Неверный номер системы


@given('я ввел неверный выбор единицы измерения')
def step_given_invalid_unit(context):
    global input_unit
    input_unit = 99  # Неверный номер единицы измерения


@when('я конвертирую значение')
def step_when_convert(context):
    global output_value, error_message

    try:
        output_value = convert_value(input_system, input_unit, input_value)
        error_message = None  # Сброс ошибки, если конвертация успешна
    except ValueError as e:
        error_message = str(e)


@when('я пытаюсь выбрать систему мер')
def step_when_select_system(context):
    global error_message

    if input_system not in [1, 2, 3]:
        error_message = "Неверный выбор системы мер."


@when('я пытаюсь выбрать единицу измерения')
def step_when_select_unit(context):
    global error_message

    if input_unit not in [1, 2, 3, 4]:
        error_message = "Неверный выбор единицы измерения."


@then('результат должен быть {expected_value:f} миллиметров')
def step_then_result_in_millimeters(context, expected_value):
    assert output_value == expected_value, f"Ожидалось {expected_value}, но получено {output_value}"

@then('результат должен быть {expected_value:f} метров')
def step_then_result_in_si(context, expected_value):
    assert output_value == expected_value, f"Ожидалось {expected_value}, но получено {output_value}"

@then('я должен увидеть сообщение "{message}"')
def step_then_see_message(context, message):
    assert error_message == message, f"Ожидалось сообщение '{message}', но получено '{error_message}'"



