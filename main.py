import time
import board
import adafruit_dht
from pyiArduinoI2Ctds import *
import sys

def _tds_start():
    tds = pyiArduinoI2Ctds(None, NO_BEGIN)
    if len(sys.argv) < 2:
        newAddress = 0x09
    else:
        tmp = int(sys.argv[1])
        if tmp > 6:
            newAddress = tmp

    if tds.begin():
        print("Найден датчик " % tds.getAddress())
        if tds.changeAddress(newAddress):
                print("Адрес изменён на " % tds.getAddress())
        else:
                print("Адрес не изменён!")
        return tds
    else:
        print("Датчик не найден!")
        return None

#start connections
# DHT
dhtDevice = adafruit_dht.DHT11(board.D4)
pin = '4'

# TDS
tds = _tds_start()

#local variables
temperature_array = []
count = 10


def find_average(nums):
    total = 0
    for num in nums:
        total += num
    count = len(nums)
    average = total / count
    return average

def measure_temperature(sensor):
    try:
        value = dhtDevice.temperature
        print("measured")
    except:
        value = 20
    print("current value ",value)
    temperature_array.append(value)
    if len(temperature_array) == count+1:
        temperature_array = temperature_array[1:]
    return sum(temperature_array) / count

def main():
    if not dhtDevice:
        print("dht not found")
        return
    while True:
        temperature = measure_temperature(sensor)
        print(temperature)
        time.sleep(1)

main()

#def main():
#    check = _start()
#    if not check:
#        return
#    tds, dht = check
#    while True:
#        temperature = measure_temperature(dht)
#        tds.set_t(temperature) # Текущая температура в градусах цельсия
#        print("Ro="          , end='')
#        print(tds.getRo()    , end='')
#        print("Ом, S="       , end='')
#        print(tds.get_S()    , end='')
#        print("мкСм/см, EC=" , end='')
#        print(tds.getEC()    , end='')
#        print("мкСм/см, TDS=", end='')
#        print(tds.getTDS()   , end='')               #   Выводим количество растворённых твёрдых веществ в жидкости.
#        print(" мг/л\r\n"    , end='')
#        time.sleep(1)
