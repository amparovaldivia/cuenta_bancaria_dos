from usuario import Cuenta_bancaria

usuario_uno=[Cuenta_bancaria(100000,0.02),Cuenta_bancaria(50000,0.02)]
usuario_dos=[Cuenta_bancaria(250000,0.02),Cuenta_bancaria(80000,0.02)]

usuario_uno[0].deposito(50000).deposito(35000).deposito(12000).retiro(15000).generar_interes().mostrar_info_cuenta()
usuario_uno[1].deposito(10000).retiro(5000).mostrar_info_cuenta()
usuario_dos[0].deposito(520000).retiro(100000).retiro(30000).retiro(20000).retiro(15000).generar_interes().mostrar_info_cuenta()
usuario_dos[1].deposito(80000).mostrar_info_cuenta()
Cuenta_bancaria.todas_las_cuentas()
