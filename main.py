from interactions.controller import Controller

if __name__ == '__main__':

    con = Controller()

    while True:
        con.process_key_buffer()
