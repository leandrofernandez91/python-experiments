import datetime
class Calculadora():
    def sumar(self, x, y):
        return x+y

    def restar(self, x, y):
        return x-y

    # def edad(self, x, y, z):
    #     return 26

    def edad(self, dia, mes, anio):
        fechaNac =datetime.date(anio,mes,dia)
        hoy = datetime.date.today()
        edad = (hoy-fechaNac)
        anios = edad.day/360
        return anios