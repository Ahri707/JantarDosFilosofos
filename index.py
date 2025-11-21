import threading
import time
import random

N = 5

hashis = [threading.Semaphore(1) for _ in range(N)]

def filosofar(nome, id_filosofo):
    esquerda = id_filosofo
    direita = (id_filosofo + 1) % N

    while True:
      
        print(f"{nome} esta pensando...")
        time.sleep(random.uniform(1, 3))

        print(f"{nome} esta com fome e tentara pegar os hashis.")

       
        if id_filosofo % 2 == 0:
            primeiro, segundo = esquerda, direita
        else:
            primeiro, segundo = direita, esquerda

       
        hashis[primeiro].acquire()
        print(f"{nome} pegou o primeiro hashi ({primeiro}).")

      
        hashis[segundo].acquire()
        print(f"{nome} pegou o segundo hashi ({segundo}).")

      
        print(f"{nome} esta comendo...")
        time.sleep(random.uniform(1, 2))

      
        hashis[primeiro].release()
        hashis[segundo].release()

        print(f"{nome} terminou de comer e devolveu os hashis.")

def main():
    nomes = ["Filosofo 1", "Filosofo 2", "Filosofo 3", "Filosofo 4", "Filosofo 5"]
    threads = []

    for i in range(N):
        t = threading.Thread(target=filosofar, args=(nomes[i], i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
