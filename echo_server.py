"""
Сценарий реализует программу, которая просто ждет подключение к сокету и отправляет обратно всё, что она через него
получает, добовляя строку префикса Echo=>. сервер => <= клиент

На стороне сервера: открыть сокет TCP/IP с указанным номером порта, ждать появления сообщения от клиента, отправить
этоже сообщение обратно;
Это реализация простого одноступенчатого диалога вида запрос/ответ, но сценарий выполняет бесконечный цикл и пока он
действует, может обслужить клиентов;
Клиент может выполняться как на удаленном, так и на локальном компьютере, если в качестве имени сервера будет
использоваться 'localhost'
"""

from socket import *   # получить конструктор сокета и константы
myHost = ''            # '' = все доступные интерфейсы хоста
myPort = 50007         # использовать незарезервированный номер порта
sockobj = socket(AF_INET, SOCK_STREAM) # создать объект сокета ТСР
sockobj.bind((myHost, myPort))         # связать с номером порта сервера
sockobj.listen(5)                      # не более 5 ожидающих запросов

while True:                                   # пока процесс работает
    connection, address = sockobj.accept()    # ждать запроса очередного криента
    print('Server connected by', address)     # соединение является новым сокетом

    while True:
        data = connection.recv(1024)          # читать следующую строку из сокета
        if not data: break                    # отправить ответ клиенту
        connection.send(b'Echo=>' + data)     # и так пока от клиента поступают данные после чего закрыть сокет
    connection.close()