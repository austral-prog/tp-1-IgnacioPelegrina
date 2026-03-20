def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665

    minutos = total_segundos // 60
    horas = minutos // 60
    minutos1 = minutos % 60
    segundos = total_segundos % 60

    print(horas)
    print(minutos1)
    print(segundos)