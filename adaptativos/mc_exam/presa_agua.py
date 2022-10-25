import random 
from time import sleep, strftime, gmtime

def readSensor(sensor = 26):
    usage = random.random() * 0.10
    return sensor - usage

def calcDeltaTime(porc_actual, porc_ant):
    # Valor de Cambio por segundo
    delta = abs(porc_actual - porc_ant)
    return delta

CANT_TOTAL = 40

sensor = readSensor()
cant_actual = sensor
porcentaje = cant_actual/CANT_TOTAL

while True:
    # Calcula el porcentaje que se está vaciando
    sensor = readSensor(sensor)
    delta = calcDeltaTime(sensor/CANT_TOTAL, porcentaje)
    porcentaje = sensor/CANT_TOTAL
    flujo = 1

    if delta > 0.001:
        flujo = 0.8

    if porcentaje < 0.6:
        flujo = 0.8
    if porcentaje < 0.4:
        flujo = 0.6
    if porcentaje < 0.2:
        flujo = 0.4

    print("Fecha:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
    print("Flujo:", flujo)
    print()
    print("Cantidad Actual:", sensor)
    print("Porcentaje:", porcentaje)
    print("Valor delta:", delta)
    print('----------------------')
    sleep(1)
    #break

    