import data
import sender_stand_request

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body
#функция для позитивных проверок
def positive_assert(kit_body):
    user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = user_response.json()["authToken"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert user_response.status_code == 201
    assert kit_response.status_code == 201
    requested_name = kit_body["name"]
    response_name = kit_response.json()["name"]
    assert requested_name == response_name
#функция для негативных проверок
def negative_assert(kit_body):
    user_body = data.user_body
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400

#1 Допустимое количество символов (1):
def test_positive_create_kit_1():
    kit_body = get_kit_body("Аа")
    positive_assert(kit_body)

#2 Допустимое количество символов (511):
def test_positive_create_kit_2():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body)

#3 Количество символов меньше допустимого (0)
def test_negative_create_kit_name_empty():
    kit_body = get_kit_body("")
    negative_assert(kit_body)

#4 Количество символов больше допустимого (512):
def test_negative_create_kit_name_512():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(kit_body)

#5 Разрешены английские буквы
def test_positive_create_kit_enlish():
    kit_body = get_kit_body("QWErty")
    positive_assert(kit_body)

#6 Разрешены русские буквы
def test_positive_create_kit_russian():
    kit_body = get_kit_body("Мария")
    positive_assert(kit_body)

#7 Разрешены спецсимволы
def test_positive_create_kit_symbols():
    kit_body = get_kit_body('''''"№%@",''')
    positive_assert(kit_body)

#8 Разрешены пробелы
def test_positive_create_kit_space():
    kit_body = get_kit_body("Человек и КО")
    positive_assert(kit_body)

#9 Разрешены цифры
def test_positive_create_kit_numbers():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

#10 Параметр не передан в запросе
def get_kit_body(name=None):
    kit_body = {
    }
    if name is not None:
        kit_body["name"] = name
    return kit_body
def test_negative_create_kit_no_name():
    kit_body = get_kit_body()
    negative_assert(kit_body)

#11 Передан другой тип параметра (число)
def test_negative_create_kit_name_diftype():
    kit_body = get_kit_body(123)
    negative_assert(kit_body)
