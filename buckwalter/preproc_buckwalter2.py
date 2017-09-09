# Part of this script is taken from:
#
# Andrew Roberts (andyr [at] comp (dot) leeds [dot] ac (dot) uk)
# Project homepage: http://www.comp.leeds.ac.uk/andyr/software/
#

buck2uni = {"'": u"\u0621", # hamza-on-the-line
            "|": u"\u0622", # madda
            ">": u"\u0623", # hamza-on-'alif
            "&": u"\u0624", # hamza-on-waaw
            "<": u"\u0625", # hamza-under-'alif
            "}": u"\u0626", # hamza-on-yaa'
            "A": u"\u0627", # bare 'alif
            "b": u"\u0628", # baa'
            "p": u"\u0629", # taa' marbuuTa
            "t": u"\u062A", # taa'
            "v": u"\u062B", # thaa'
            "j": u"\u062C", # jiim
            "H": u"\u062D", # Haa'
            "x": u"\u062E", # khaa'
            "d": u"\u062F", # daal
            "*": u"\u0630", # dhaal
            "r": u"\u0631", # raa'
            "z": u"\u0632", # zaay
            "s": u"\u0633", # siin
            "$": u"\u0634", # shiin
            "S": u"\u0635", # Saad
            "D": u"\u0636", # Daad
            "T": u"\u0637", # Taa'
            "Z": u"\u0638", # Zaa' (DHaa')
            "E": u"\u0639", # cayn
            "g": u"\u063A", # ghayn
            "_": u"\u0640", # taTwiil
            "f": u"\u0641", # faa'
            "q": u"\u0642", # qaaf
            "k": u"\u0643", # kaaf
            "l": u"\u0644", # laam
            "m": u"\u0645", # miim
            "n": u"\u0646", # nuun
            "h": u"\u0647", # haa'
            "w": u"\u0648", # waaw
            "Y": u"\u0649", # 'alif maqSuura
            "y": u"\u064A", # yaa'
            "F": u"\u064B", # fatHatayn
            "N": u"\u064C", # Dammatayn
            "K": u"\u064D", # kasratayn
            "a": u"\u064E", # fatHa
            "u": u"\u064F", # Damma
            "i": u"\u0650", # kasra
            "~": u"\u0651", # shaddah
            "o": u"\u0652", # sukuun
            "`": u"\u0670", # dagger 'alif
            "{": u"\u0671", # waSla
}

def transliterateString(inString):
    out = ""
    # Loop over each character in the string, inString.
    for char in inString:
        # Look up current char in the dictionary to get its
        # respective value. If there is no match, e.g., chars like
        # spaces, then just stick with the current char without any
        # conversion.
        out = out + buck2uni.get(char, char)
    return out

HTML_PRE = """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>ffr&#39;s pages</title>
  <meta name="description" content="Some description">
  <style>
    .arabic {
      font-family: me_quran;
      font-size: 12pt;
    }
    .new-style {
      font-style: italic;
      text-decoration: overline;
      color: gray;
    }
  </style>
</head>

<body>
This is an Arabic text: <span class="arabic">
"""

# another font: noorehira

HTML_END = """</span> Another text.
</body>
</html>
"""

print(HTML_PRE +
    transliterateString("bisomi All~`hi Alr~aHom`ni Alr~aHom`ni Alr~aHiyomi")
     + HTML_END)
