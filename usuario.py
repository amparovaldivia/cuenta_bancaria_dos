class Cuenta_bancaria:
    todas_cuentas = []

    def __init__(self, cuenta, interes):
        self.cuenta = cuenta
        self.interes = interes
        Cuenta_bancaria.todas_cuentas.append(self)

    def deposito(self, monto):
        self.cuenta = self.cuenta+monto
        return self

    def retiro(self, monto):
        self.cuenta = self.cuenta-monto
        return self

    def mostrar_info_cuenta(self):
        print(self.cuenta)
        return self

    def generar_interes(self):
        self.cuenta = self.cuenta+self.interes*self.cuenta
        return self

    @classmethod
    def todas_las_cuentas(cls):
        for cuenta in cls.todas_cuentas:
            print(cuenta.__dict__)
