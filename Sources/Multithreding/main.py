import threading
import time


def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking {first} {last}")


def take_out_trash():
    time.sleep(2)
    print("You take out the trash")


def get_mail():
    time.sleep(4)
    print("You get the mail")


chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Dooby"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")
