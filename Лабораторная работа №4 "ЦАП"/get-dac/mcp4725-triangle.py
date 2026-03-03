import mcp4725_driver as mcp
import triangle_generator as tg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    mcp4725 = mcp.MCP4725(5.19)
    start_time = time.time()
    now_time = 0.0

    while True:
        mcp4725.set_voltage(amplitude * tg.get_triangle_wave_amplitude(signal_frequency, now_time))
        tg.wait_for_sampling_period(sampling_frequency)
        now_time = time.time() - start_time



finally:
        mcp4725.deinit()