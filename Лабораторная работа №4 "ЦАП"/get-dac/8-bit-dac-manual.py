import RPi.GPIO as GPIO

def voltage_to_number(voltage):
    dynamic_range = 3.17
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
        print("Устанавливаем 0.0 B")
        return 0
    
    return int((voltage / dynamic_range) * 255)

def number_to_dac(number, dac_bits):
    array = [int(element) for element in bin(number)[2:].zfill(8)]
    print("Число на вход ЦАП: ", number, ", , биты: ", array)
    GPIO.output(dac_bits, array)


# dac_bits = [22, 27, 17, 26, 25, 21, 20, 16]
dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_bits, GPIO.OUT)

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number, dac_bits)

        except ValueError:
            print("Вы ввели не число. Попробуйте снова\n")

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()
