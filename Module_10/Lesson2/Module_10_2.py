import time
import threading
from datetime import datetime

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0
        while self.enemies > 0:
            self.enemies -= self.power
            days += 1
            print(f"{self.name} сражается {days}..., осталось {self.enemies} воинов.")
            time.sleep(2)

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)


start_time1 = datetime.now()
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
stop_time1 = datetime.now()

print("Битвы завершены.")
print(f'Работа потоков: {stop_time1 - start_time1}')