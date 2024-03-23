from time import sleep
from threading import Thread

class MeuThread(Thread):
    def __init__(self, text, tempo):
        self.text = text
        self.tempo = tempo 

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.text)



t1 = MeuThread('Thread 1' , 5)
t1.start()


t2 = MeuThread('Thread 2', 3)
t2.start()

t3 = MeuThread('Thread 4', 2)
t3.start()



