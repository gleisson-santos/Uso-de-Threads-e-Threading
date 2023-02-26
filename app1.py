import webbrowser
import threading
import time
import random



def comentar(site, comentario):
    print(f'Entrando no site {site}')
    print(f'Deixando um comentatio: {comentario}')
    time.sleep(5)
    print(f'Dados processads no site {site}')

comentario = ['oi', 'ola', 'gostei', 'curti', 'bom']
threads = []
for site in range(5):
    nova_thread = threading.Thread(target=comentar, args=(site, random.choice(comentario)))
    threads.append(nova_thread)

for thread in threads:
    thread.start()
    #print(f'Iniciando {thread.name}')

for thread in threads:
    thread.join()
    print(f'Finaliznaado {thread.name}')