import data
from sender_stand_request import post_new_kits

#Prueba 1 El número permitido de caracteres (1)
def test_kit_name_1_caracter():
    data.kit_body = {"name": "a"}
    response = post_new_kits(data.kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == "a"

#Prueba 2 El número permitido de caracteres (511)
def test_kit_name_511_caracteres():
    name = "a" * 511
    data.kit_body = {"name": name}
    response = post_new_kits(data.kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == name

#Prueba 3 El número de caracteres es menor que la cantidad permitida (0)
def test_kit_name_0_caracteres():
    data.kit_body = {"name": ""}
    response = post_new_kits(data.kit_body)
    assert response.status_code == 400

#Prueba 4 El número de caracteres es mayor que la cantidad permitida (512)
def test_kit_name_512_caracteres():
    data.kit_body = {"name": "a" * 512}
    response = post_new_kits(data.kit_body)
    assert response.status_code == 400

#Prueba 5 Se permiten caracteres especiales
def test_kit_name_caracteres_especiales():
    special_name = '""№%@",'
    data.kit_body = {"name": special_name}
    response = post_new_kits(data.kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == special_name

#Prueba 6 Se permiten números
def test_kit_name_espacios():
    spaced_name = " A Aaa "
    data.kit_body = {"name": spaced_name}
    response = post_new_kits(data.kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == spaced_name

#Prueba 7 Se permiten números
def test_kit_name_numeros():
    numeric_name = "123"
    data.kit_body = {"name": numeric_name}
    response = post_new_kits(data.kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == numeric_name

#Prueba 8 El parámetro no se pasa en la solicitud
def test_kit_name_missing():
    data.kit_body = {}
    response = post_new_kits(data.kit_body)
    assert response.status_code == 400

#Prueba 9 Se ha pasado un tipo de parámetro diferente (número)
def test_kit_name_parametro_diferente():
    data.kit_body = {"name": 123}
    response = post_new_kits(data.kit_body)
    assert response.status_code == 400