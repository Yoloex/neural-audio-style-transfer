import numpy as np
import soundfile as sf

a = np.load('result.npy')

sf.write('result.wav', a, 22050)