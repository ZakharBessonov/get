import r2r_dac as r2r
import triangle_generator as tr
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.2, True)
    start_time = time.time()
    now_time = 0.0

    while True:
        dac.set_voltage(amplitude * tr.get_triangle_wave_amplitude(signal_frequency, now_time))
        tr.wait_for_sampling_period(sampling_frequency)
        now_time = time.time() - start_time



finally:
        dac.deinit()