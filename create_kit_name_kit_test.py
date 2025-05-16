from data import longitud_nombre, longitud_caracteres_menor

#El número de caracteres permitido (1)
def test_el_no_permitido_de_caracteres():
    assert longitud_nombre("a") == 1
#El número de caracteres permitido (511)
def test_carateres_permitidos_dos():
    assert longitud_nombre("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC") <= 511
#El número de caracteres es menor que la cantidad permitida (0)
def test_caracteres_menor_cero():
    assert longitud_caracteres_menor("") >1
#El número de caracteres es mayor que la cantidad permitida (512)
def test_caracteres_mas_de_los_permitidos():
    assert longitud_nombre("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD") <=511
#Se permiten caracteres especiales
def test_caracteres_especiales():
    assert longitud_nombre("Ñ#@,")
#Se permiten espacios
def test_espacios():
    assert longitud_nombre("A Aaa")
#Se permiten números
def test_numeros():
    assert longitud_caracteres_menor("123")
#El parametro no se pasa en la solicitud
def test_parametro_null():
    assert longitud_nombre(None)
#Se ha pasado un tipo de parametro diferente
def test_parametro_diferente():
    assert longitud_nombre(123)