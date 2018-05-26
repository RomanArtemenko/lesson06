from datetime import datetime
import logging

class Greeter:

    def greet(self, name):
        logging.basicConfig(filename='example.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.info(" : method was called.")

        if 6 <= datetime.now().hour < 12:
            return "Доброе утро %s" % name.strip().capitalize()
        elif 18 <= datetime.now().hour < 22:
            return "Доброе вечер %s" % name.strip().capitalize()
        elif 22 <= datetime.now().hour or datetime.now().hour < 6:
            return "Доброй ночи %s" % name.strip().capitalize()
        return "Привет %s" % name.strip().capitalize()