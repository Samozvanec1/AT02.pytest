import pytest
from main import is_palindrome, sort_list, init_db, add_user, get_user  # замените my_module на имя вашего модуля

def test_is_palindrome_true():
   assert is_palindrome("madam") == True

def test_is_palindrome_false():
   assert is_palindrome("hello") == False

@pytest.mark.parametrize("s, expected", [
   ("racecar", True),
   ("python", False),
   ("level", True),
   ("", True),  # Пустая строка является палиндромом
])
def test_is_palindrome_parametrized(s, expected):
   assert is_palindrome(s) == expected

def test_sort_list_ascending():
   assert sort_list([3, 1, 2, 5, 4]) == [1, 2, 3, 4, 5]

def test_sort_list_descending():
   assert sort_list([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

@pytest.fixture
def db_conn():
   conn = init_db()
   yield conn # возвращаем контекстный менеджер

def test_add_and_get_user(db_conn):
   add_user(db_conn, "testuser", "18")
   assert get_user(db_conn, "testuser") == (1, 'testuser', 18)


