from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io

samplerate, data = wavfile.read('output.wav')

Diff = 1000*(data[:, 1] - data[:, 0])

wavfile.write("key.wav", samplerate, Diff)

