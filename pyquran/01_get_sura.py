import pyquran

sura = pyquran.quran.get_sura(1, with_tashkeel=True)
Nayahs = len(sura)

print("Nayahs = ", Nayahs)

for l in sura:
    print(l)
