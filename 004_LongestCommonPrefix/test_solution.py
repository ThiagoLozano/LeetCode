from solution import Solution
import pytest # Biblioteca para testes unitários.

@pytest.pytest.fixture
def solution_instance():
    return Solution()

# Test 1: Entradas com uma lista de prefixos iguais.
def test_longestCommonPrefix_with_prefix(solution_instance):
    assert solution_instance.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert solution_instance.longestCommonPrefix(["car","case"]) == "ca"
    assert solution_instance.longestCommonPrefix(["do","doctor"]) == "do"
    assert solution_instance.longestCommonPrefix(["hi","hello"]) == "h"

# Test 2: Entradas com uma lista de prefixos diferentes.
def test_longestCommonPrefix_no_prefix(solution_instance):
    assert solution_instance.longestCommonPrefix(["dog","racecar","car"]) == ""
    assert solution_instance.longestCommonPrefix(["house","pencil"]) == ""
    assert solution_instance.longestCommonPrefix(["do","work"]) == ""

# Test 3: Entrada com lista vazia.
def test_longestCommonPrefix_empty(solution_instance):
    assert solution_instance.longestCommonPrefix([""]) == ""
