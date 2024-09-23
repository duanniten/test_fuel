import pytest

from fuel import convert, gauge

def test_convert_sepator():       
    text = '1/3'
    assert convert(text) == 33

def test_convert_str(): 
    text = 'cat'
    with pytest.raises(ValueError):
        convert(text)

def test_convert_no_separtor(): 
    text = '1.3'
    with pytest.raises(ValueError):
        convert(text)

def test_convert_x_greater(): 
    text = '3/2'
    with pytest.raises(ValueError):
        convert(text)

def test_convert_y_zero(): 
    text = '3/0'
    with pytest.raises(ZeroDivisionError):
        convert(text)

def test_E():
    valor = 1
    assert gauge(valor) == 'E'

def test_F():
    valor = 99
    assert gauge(valor) == 'F'

def test_valor():
    valor = 15
    assert gauge(valor) == '15%'