from solution import Solution
import pytest # Biblioteca para testes unitários.

@pytest.fixture
def solution_instance():
    return Solution()

# Test 1: Entrada com chaves abertas e fechadas corretamente.
def test_isValid_Correct(solution_instance):
    assert solution_instance.isValid('()') == True
    assert solution_instance.isValid('()[]') == True
    assert solution_instance.isValid('()[]{}') == True

# Test 2: Entrada com chaves abertas e fechadas incorretamente.
def test_isValid_Incorrect(solution_instance):
    assert solution_instance.isValid('(]') == False
    assert solution_instance.isValid('([)]') == False
    assert solution_instance.isValid('(})]}[') == False

# Test 3: Entrada com apenas uma chave aberta ou fechada.
def test_isValid_OneKey(solution_instance):
    assert solution_instance.isValid('(') == False
    assert solution_instance.isValid('[') == False
    assert solution_instance.isValid('{') == False
    assert solution_instance.isValid(')') == False
    assert solution_instance.isValid(']') == False
    assert solution_instance.isValid('}') == False
