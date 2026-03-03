import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = pwm.PWM_DAC(12, 500, 3.29, True)
    start_time = time.time()
    now_time = 0.0

    while True:
        dac.set_voltage(amplitude * sg.get_sin_wave_amplitude(signal_frequency, now_time))
        sg.wait_for_sampling_period(sampling_frequency)
        now_time = time.time() - start_time



finally:
        dac.deinit()