from nltk.corpus import reuters

# download: nltk.download("reuters")

files = reuters.fileids()
print(files[:5])