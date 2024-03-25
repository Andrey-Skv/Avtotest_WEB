""" Задание 1
С использованием фреймворка pytest написать тест операции checkText
SOAP API https://speller.yandex.net/services/spellservice?WSDL
Тест должен использовать DDT и проверять наличие определенного
верного слова в списке предложенных исправлений к определенному
неверному слову.
Слова должны быть заданы через фикстуры в conftest.py,
адрес wsdl должен быть вынесен в config.yaml.
Методы работы с SOAP должны быть вынесены в отдельную библиотеку.  """

from zeep import Client, Settings
import yaml

with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)
    wsdl_url = data['wsdl_url']


def check_text(text):
    settings = Settings(strict=False)
    client = Client(wsdl_url, settings=settings)
    result = client.service.checkText(text)[0]['s']
    return result


if __name__ == "__main__":
    print(check_text("корва"))
