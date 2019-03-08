import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

if len(sys.argv) < 2:
    raise RuntimeError("Need one argument")

img = cv2.imread(sys.argv[1], 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.clf()

plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.title("Input image")
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(magnitude_spectrum, cmap="gray")
plt.title("Magnitude spectrum")
plt.xticks([])
plt.yticks([])

plt.savefig("TEMP_test_fft.pdf")

