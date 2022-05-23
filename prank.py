import winsound
import time
time.sleep(10)
for i in range(0,5):
    # winsound.PlaySound(sound,flags)
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)