# JantarDosFilosofos
O objetivo é permitir que cinco filósofos alternem entre pensar e comer sem causar deadlock ou starvation. A solução utiliza threads e semáforos para controlar o acesso aos hashis.

1. Representação dos Hashis
Cada hashi é representado por um semáforo binário (Semaphore(1)). Isso garante que apenas um
filósofo por vez possa utilizar cada hashi.

3. Estratégia para Evitar Deadlock
Para impedir deadlock, os filósofos pares pegam primeiro o hashi da esquerda e depois o da direita. Já
os filósofos ímpares fazem o contrário. Essa inversão quebra a dependência circular que leva ao
deadlock.

5. Função do Filósofo
Cada filósofo pensa por um tempo aleatório, tenta pegar os hashis seguindo a estratégia de ordem
invertida, come por um tempo e devolve os hashis à mesa.
