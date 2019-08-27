star = "\xe2\x98\x85"
x = "This is a star " + star.encode("latin1").decode("utf-8")
print(x)

emoji1 = "\x1F\x60\x00"
print(emoji1.encode("latin1").decode("utf-8"))
