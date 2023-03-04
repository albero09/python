#operadores and y or
usuario_logeado =True
usuario_admin = True
if usuario_logeado and usuario_admin:
    print('ADMINISTRADOR')
elif usuario_logeado:
    print('ACCESO AL SISTEMA')
else:
    print('DEBES INICIAR SECION')
    
