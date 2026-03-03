import numpy
import time
import math

def get_triangle_wave_amplitude(freq, time):
    return (math.asin(math.sin(2 * math.pi * freq * time))*2/math.pi + 1) * 0.5

def wait_for_sampling_period(sampling_frequency):
    time.sleep(1 / sampling_frequency)