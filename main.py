import time

from interactions.controller import Controller

if __name__ == '__main__':

    con = Controller()

    while True:

        con.process_key_buffer()
        time.sleep(0.01)
