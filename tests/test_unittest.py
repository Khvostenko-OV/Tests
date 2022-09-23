import unittest
from main import search_person, search_shelf, add_document, del_document, move_document, add_shelf


class TestFunc(unittest.TestCase):
    def test_search_person(self):
        etalon = ("Аристарх Павлов", "")
        result = search_person("10006")
        self.assertEqual(etalon, result)

    def test_search_shelf(self):
        etalon = ("2", "")
        result = search_shelf("10006")
        self.assertEqual(etalon, result)

# Тестировать функции, которые меняют данные, надо наверное как-то по-другому?
# Не только по возвращаемым флагам, но и по самим данным
    def test_add_document(self):
        etalon = ("", "Неверный номер полки")
        result = add_document("1", "2", "3", "4")
        self.assertEqual(etalon, result)

    def test_del_document(self):
        etalon = ("", "В базе нет документа 123")
        result = del_document("123")
        self.assertEqual(etalon, result)

    def test_move_document(self):
        etalon = ("1", "")
        result = move_document("11-2", "3")
        self.assertEqual(etalon, result)

    def test_add_shelf(self):
        etalon = "Такая полка уже существует"
        result = add_shelf("3")
        self.assertEqual(etalon, result)
