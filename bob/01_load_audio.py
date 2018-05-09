import bob.io.audio

audio = bob.io.audio.reader("L_02_Mic.wav")
print(audio.rate)

signal = audio.load()
print(signal.shape)
