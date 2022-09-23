import requests

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def search_person(doc_number):
  """p - поиск человека по номеру документа"""
#  doc_number = input('Введите номер документа: ')
  for doc in documents:
    if doc["number"] == doc_number:
#      print('Имя Фамилия -', doc["name"])
      return doc["name"], ""
  else:
#    print('В базе нет такого документа')
    return "", 'В базе нет документа ' + doc_number

def search_shelf(doc_number):
  """s - выдает номер полки, на которой хранится документ"""
#  doc_number = input('Введите номер документа: ')
  for shelf in directories:
    if doc_number in directories[shelf]:
#      print('Полка №', shelf)
      return shelf, ""
  else:
#    print('Документ на полках не найден')
    return "", 'Документ на полках не найден'

def add_document(doc_type, doc_number, person, shelf):
  """a - добавляет документ в архив"""
#  doc_type = input('Введите тип документа: ')
#  doc_number = input('Введите номер документа: ')
#  person = input('Введите Имя и Фамилию: ')
  documents.append({"type": doc_type, "number": doc_number, "name": person})
#  shelf = input('Введите номер полки: ')
  if shelf in directories:
    directories[shelf].append(doc_number)
#    print('Документ добавлен на',shelf,'полку')
    return shelf, ""
  else:
#    print('Неверный номер!')
    return "", 'Неверный номер полки'

def del_document(doc_number):
  """d - удаляет документ из архива"""
#  doc_number = input('Введите номер документа: ')
  for shelf in directories:
    if doc_number in directories[shelf]:
#      print('Удалён с полки №', shelf)
      directories[shelf].remove(doc_number)
  for doc in documents:
    if doc["number"] == doc_number:
#      print('Удалён ', doc["name"])
      name = doc["name"]
      documents.remove(doc)
      return name, ""
  return "", 'В базе нет документа ' + doc_number

def move_document(doc_number, to_shelf):
  """m - перемещает документ на другую полку"""
#  doc_number = input('Введите номер документа: ')
  for doc in documents:
    if doc["number"] == doc_number:
#      print('Имя Фамилия -', doc["name"])
      break
  else:
#    print('В базе нет такого документа')
    return "", 'В базе нет документа ' + doc_number
  for shelf in directories:
    if doc_number in directories[shelf]:
#      print('Полка №', shelf)
      from_shelf = shelf
      break
  else:
#    print('Документ на полках не найден')
    return "", f'Документ {doc_number} на полках не найден'
#  to_shelf = input('Введите целевую полку: ')
  if to_shelf in directories:
    directories[from_shelf].remove(doc_number)
    directories[to_shelf].append(doc_number)
#    print(doc_number, 'перемещён на полку', to_shelf)
    return from_shelf, ""
  else:
#    print('Целевая полка не найдена')
    return "", 'Целевая полка не найдена'

def add_shelf(new_shelf):
  """as - добавляет новую полку"""
#  new_shelf = input('Введите номер новой полки: ')
  if new_shelf not in directories:
    directories[new_shelf] = []
#    print('Полка добавлена')
    return ""
  else:
#    print('Такая полка уже существует!')
    return 'Такая полка уже существует'


YA_API_URL = 'https://cloud-api.yandex.net/v1/disk/resources/'


class YaDiskMakeDir:
  def __init__(self):
    with open('tt.txt') as file:
      self.token = file.readline().strip()
    self.headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth ' + self.token}

  def make_dir(self, file_path):
    return requests.put(YA_API_URL, headers=self.headers, params={'path': file_path}).status_code

  def check_dir(self, file_path):
    return requests.get(YA_API_URL, headers=self.headers, params={'path': file_path}).status_code

if __name__ == "__main__":
  print(search_person("10006"))
  print(search_shelf("10006"))

  yad = YaDiskMakeDir()
  print(yad.make_dir("TestDirectory"))
  print(yad.check_dir("TestDirectory"))
