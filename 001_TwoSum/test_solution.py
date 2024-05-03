from solution import Solution
import pytest # Biblioteca para testes unitários.

@pytest.pytest.fixture
def solution_instance():
    return Solution()

# Test 1: Entrada com valores corretos.
def test_twoSum_corret_numbers(solution_instance):
    assert solution_instance.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution_instance.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution_instance.twoSum([3, 3], 6) == [0, 1]

# Test 2: Entrada com lista de inteiros vazia.
def test_twoSum_empty_list(solution_instance):
    assert solution_instance.twoSum([], 5) == None

# Test 3: Entrada com apenas um valor inteiro na lista.
def test_twoSum_single_element_list(solution_instance):
    assert solution_instance.twoSum([5], 5) == None

# Test 4: Entrada com lista de inteiros que não resultam no target desejado.
def test_twoSum_no_solution(solution_instance):
    assert solution_instance.twoSum([1, 2, 3, 4], 10) == None

# Test 5: Entrada com lista de inteiros negativos.
def test_twoSum_negative_numbers(solution_instance):
    assert solution_instance.twoSum([-1, -2, -3, -4], -7) == [2, 3]

# Test 6: Entrada com lista de floats.
def test_twoSum_float_numbers(solution_instance):
    assert solution_instance.twoSum([2.5, 3.5, 1.0], 6.0) == [0, 1]
