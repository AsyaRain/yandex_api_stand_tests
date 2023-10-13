import data
import sender_stand_request

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

#1
def test_positive_create_kit_1():
    kit_body = get_kit_body("Аа")
    user_body = data.user_body
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert user_response.status_code == 201
    assert auth_token != ""
    assert kit_response.status_code == 201
    requested_name = kit_body["name"]
    response_name = kit_response.json()["name"]
    assert requested_name == response_name
#2
def test_positive_create_kit_2():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = user_response.json()["authToken"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert user_response.status_code == 201
    assert auth_token != ""
    assert kit_response.status_code == 201
    requested_name = kit_body["name"]
    response_name = kit_response.json()["name"]
    assert requested_name == response_name
#3
def test_negative_create_kit_name_empty():
    kit_body = get_kit_body("")
    user_body = data.user_body
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
#4
def test_negative_create_kit_name_512():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    user_body = data.user_body
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
#5
def test_positive_create_kit_english():
    kit_body = get_kit_body("QWErty")
    user_body = data.user_body
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert user_response.status_code == 201
    assert auth_token != ""
    assert kit_response.status_code == 201
    requested_name = kit_body["name"]
    response_name = kit_response.json()["name"]
    assert requested_name == response_name
#6
def test_positive_create_kit_russian():
    kit_body = get_kit_body("Мария")
    user_body = data.user_body
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert user_response.status_code == 201
    assert auth_token != ""
    assert kit_response.status_code == 201
    requested_name = kit_body["name"]
    response_name = kit_response.json()["name"]
    assert requested_name == response_name
#7
def test_positive_create_kit_symbols():
    kit_body = get_kit_body('''''"№%@",''')
    user_body = data.user_body
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert user_response.status_code == 201
    assert auth_token != ""
    assert kit_response.status_code == 201
    requested_name = kit_body["name"]
    response_name = kit_response.json()["name"]
    assert requested_name == response_name
#8
def test_positive_create_kit_space():
    kit_body = get_kit_body("Человек и КО")
    user_body = data.user_body
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert user_response.status_code == 201
    assert auth_token != ""
    assert kit_response.status_code == 201
    requested_name = kit_body["name"]
    response_name = kit_response.json()["name"]
    assert requested_name == response_name
#9
def test_positive_create_kit_numbers():
    kit_body = get_kit_body("123")
    user_body = data.user_body
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert user_response.status_code == 201
    assert auth_token != ""
    assert kit_response.status_code == 201
    requested_name = kit_body["name"]
    response_name = kit_response.json()["name"]
    assert requested_name == response_name
#10
def test_negative_create_kit_no_name():
    kit_body = get_kit_body()
    user_body = data.user_body
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
#11
def test_negative_create_kit_name_diftype():
    kit_body = get_kit_body(123)
    user_body = data.user_body
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
