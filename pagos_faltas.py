sem_adeudo = imput("alumno presenta sem_adeudo:")

adeudo= float (sem_adeudo)

if adeudo>=1:
    print(f'El alumno tiene sem_adeudo{sem_adeudo} y por lo tanto tiene falta')

else:
    print("El alumno no tiene sem_adeudo entonces no tiene faltas")

    faltas= input ("Numero de faltas del alumno")

    faltas= int(faltas)

    if faltas>=3:
        print(f"El alumno tiene {Faltas} faltas por lo que esta REPROBADO")

    else:
        print("El alumno esta APROBADO")
        