import pwm_dac as pwm
import triangle_generator as tg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = pwm.PWM_DAC(12, 500, 3.29, True)
    start_time = time.time()
    now_time = 0.0

    while True:
        dac.set_voltage(amplitude * tg.get_triangle_wave_amplitude(signal_frequency, now_time))
        tg.wait_for_sampling_period(sampling_frequency)
        now_time = time.time() - start_time



finally:
        dac.deinit()