from solution import Solution
import pytest # Biblioteca para testes unitários.

@pytest.fixture
def solution_instance():
    return Solution()

# Test 1: Entradas com texto correto.
def test_romanToInt_valid(solution_instance):
    assert solution_instance.romanToInt('III') == 3
    assert solution_instance.romanToInt('LVIII') == 58
    assert solution_instance.romanToInt('MCMXCIV') == 1994
    assert solution_instance.romanToInt('X') == 10
    assert solution_instance.romanToInt('LL') == 100
    assert solution_instance.romanToInt('XMM') == 1990
    assert solution_instance.romanToInt('IIV') == 5

# Test 2: Entradas com texto incorreto.
def test_romanToInt_invalid(solution_instance):
    assert solution_instance.romanToInt('A') == None
    assert solution_instance.romanToInt('AAA') == None
    assert solution_instance.romanToInt('0') == None
    assert solution_instance.romanToInt('XAAA') == None
    assert solution_instance.romanToInt('X1X') == None

# Test 3: Entradas com texto vazio.
def test_romanToInt_empyt(solution_instance):
    assert solution_instance.romanToInt('') == 0
