import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    mcp4725 = mcp.MCP4725(5.19)
    start_time = time.time()
    now_time = 0.0

    while True:
        mcp4725.set_voltage(amplitude * sg.get_sin_wave_amplitude(signal_frequency, now_time))
        sg.wait_for_sampling_period(sampling_frequency)
        now_time = time.time() - start_time



finally:
        mcp4725.deinit()