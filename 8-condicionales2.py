#Ejemplo con elif
ocupacion = 'jubilado'

if ocupacion == 'Estudiante':
    print('Tiene 50% de descuento')
elif ocupacion == 'jubilado':
    print('tiene el 75% de descuento')
elif ocupacion =='desempleado':
    print('tiene el 10% de descuento')
else:
    print('tienes que pagar el 100%')
    