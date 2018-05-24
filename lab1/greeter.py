from datetime import datetime

class Greeter:

    def greet(self, name):
        if 6 <= datetime.now().hour < 12:
            return "Доброе утро %s" % name.strip().capitalize()
        elif 18 <= datetime.now().hour < 22:
            return "Доброе вечер %s" % name.strip().capitalize()
        elif 22 <= datetime.now().hour or datetime.now().hour < 6:
            return "Доброй ночи %s" % name.strip().capitalize()
        return "Привет %s" % name.strip().capitalize()