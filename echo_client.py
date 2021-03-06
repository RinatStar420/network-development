"""
Программы подключающиеся к серверу, который ждёт входящих соединений, обычно называют клиенатми.
Реализуем простого клиента на языке питона.

На стороне клиента: использует сокеты для передачи данных серверу и выводит ответ сервера на каждую строку соощения;
'localhost' означает, что сервер выполняется на одном компьютере с клиентом, что позволяет тестировать клиента и сервер
на одном компьютере;
для тестирования через интернет запустите сервер на удаленном компьютере и установите serverHost или argv[1] равным
домену имени компьютера или его IP-адресу;
сокеты Python являются переносимым интерфейсом к сокетам BSD, с методами объетов для стандартных функций сокетов,
доступных библиотеке С.
"""

import sys
from socket import *     # переносимый интерфейс сокетов плюс константы
serverHost = 'localhost' # имя сервера
serverPort = 50007       # незарезервированный порт, используемый нашим сервером

message = [b'Hello network world']   # текст, посылаемы серверу обязательно типа bytes: b'' или str.encode()

if len(sys.argv) > 1:
    serverHost = sys.argv[1]         # сервер в аргументе 1 командной строки
    if len(sys.argv) > 2:            # сервер в аргументе 2 командной строки 2..n
        message = (x.encode() for x in sys.argv[2:])

sockobj = socket(AF_INET, SOCK_STREAM)    # создать объект сокета TCP/IP
sockobj.connect((serverHost, serverPort)) # соединение с сервером и портом

for line in message:
    sockobj.send(line)                    # послать серверу строчку через сокет
    data = sockobj.recv(1024)             # получить строку от сервера до 1к
    print('Client received:', data)       # строка bytes выводится в кавычках, было 'x', repr(x)

sockobj.close()         # закрыть сокет, чтобы послать серверу eof
