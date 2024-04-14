import urllib.request
import urllib
from time import sleep
import datetime

t1 = datetime.datetime.now().time()
time = datetime.datetime.now()

while True:
    try:
        site = urllib.request.urlopen('http://pudim.com.br')
        seconds1 = int(datetime.timedelta(hours=t1.hour, minutes=t1.minute, seconds=t1.second).total_seconds())
    except KeyboardInterrupt:
        break
    except urllib.error.URLError:
        print(f'Erro! não foi possível conectar ao site         {time}')
        with open("Conenction.txt", 'a') as file:
            file.write(f"Falha de conexão com a internet (urllib) na data e hora: {time}\n")
        sleep(1)
    except ConnectionResetError:
        print(f'Erro! não foi possível conectar ao site         {time}')
        with open("Conenction.txt", 'a') as file:
            file.write(f"Falha de conexão com a internet (ConnectionReset) na data e hora: {time}\n")
        sleep(1)
    else:
        t2 = datetime.datetime.now().time()
        seconds2 = int(datetime.timedelta(hours=t2.hour,
                                          minutes=t2.minute,
                                          seconds=t2.second).total_seconds())
        total_time = seconds2 - seconds1
        if total_time > 10:
            try:
                print(f'Conexão Lenta! Tempo para resposta: {total_time} seconds')
                raise urllib.error.URLError('Conexão demorou mais que 10 segundos')
            except (urllib.error.URLError, TimeoutError):
                print(f'Erro ! Não foi possível conectar-se ao site !         {time}')
                with open("Conenction.txt", 'a') as file:
                    file.write(f"Falha de conexão na data e hora: {time}\n")
                sleep(1)
        if 3 < total_time <= 10:
            print(f'Conecxão Lenta! Resposta demorou {total_time} segundos')
            with open('Conenction.txt', 'a') as file:
                file.write(
                    f"Conexão lenta com a internet, demorou {total_time} para respoder na data e hora de {time}\n")
        print(f'Consegui acessar o site !        {time}')
        t1 = t2
        sleep(1)
