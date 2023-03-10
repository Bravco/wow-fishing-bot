import pyaudio
import numpy as np
import win32gui
import win32api
import win32con
import time
import random

p = pyaudio.PyAudio()
hwnd = win32gui.FindWindow(None, "World of Warcraft")

while True:
	start_time = time.time()
	stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, input_device_index = 2)

	while stream.is_active():
		data = stream.read(1024, exception_on_overflow = False)
		data = np.frombuffer(data, dtype=np.int16) / 32768.0
		rms = np.sqrt(np.mean(data**2))
		db = 20 * np.log10(rms / ((2**15) / 32768.0))
		print(db)
		if db > -45:
			print("CATCH")
			win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F6, 0)
			win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_F6, 0)
			break
		elif (time.time() - start_time) > 17:
			break

	time.sleep(random.uniform(2, 4))
	print("BAIT")
	win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F6, 0)
	win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_F6, 0)
	start_time = time.time()
	time.sleep(random.uniform(2, 4))

	stream.stop_stream()
	stream.close()


# p.terminate()