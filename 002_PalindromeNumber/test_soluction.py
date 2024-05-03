from solution import Solution
import pytest # Biblioteca para testes unitários.

@pytest.pytest.fixture
def solution_instance():
    return Solution()

# Test 1: Entradas com valores que são Palíndromos;
def test_isPalindrome_true(solution_instance):
    assert solution_instance.isPalindrome(0)  == True
    assert solution_instance.isPalindrome(101)  == True
    assert solution_instance.isPalindrome(222)  == True
    assert solution_instance.isPalindrome(1221) == True

# Test 2: Entradas com valores que NÃO são Palíndromos;
def test_isPalindrome_false(solution_instance):
    assert solution_instance.isPalindrome(123)  == False
    assert solution_instance.isPalindrome(500)  == False
    assert solution_instance.isPalindrome(1002) == False
