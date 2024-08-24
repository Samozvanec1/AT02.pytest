import  pytest
from  DZ import count_glass
def test_pusto_stok():
    assert count_glass("") == 0

def test_no_glass():
    assert count_glass("СССРжiв") == 0

def test_all_glass():
    assert count_glass("аЁИоуыЭюя") == 9

def test_mixed_case():
    assert count_glass("Ленин жил,Ленин жив, ЛЕНИН БУДЕТ жить") == 11

