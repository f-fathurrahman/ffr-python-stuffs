#!/usr/bin/python3

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

def toArabicInline(inString):
    str1 = '<span style="font-family: me_quran; font-size: 24;>'
    strArabic = transliterateString(inString)
    str2 = '</span>'
    return str1 + strArabic + str2

def toArabicParagraph(inStringP):
    lines = inStringP.split('\n')
    strOut = ''
    for l in lines:
        strOut = strOut + '\n' + transliterateString(l)
    str1 = '<p style="font-family: me_quran; font-size: 24; text-align: right;">'
    str2 = '</p>'
    return str1 + strOut + str2

def scan_until(chars):
    bws = ''
    sys.stdout.write(chars)
    for c in chars:
        if c == '@':
            break
        bws = bws + c
    return bws


import sys

infile = open( sys.argv[1], 'r' )

while True:
    line = infile.readline()
    if not line:
        break
    line = line.replace('\n','')
    #print('line = ', line)
    idx_char = 0
    lineout = ''
    start = False
    end = True
    indices = []
    ichars = 0
    lineout = ''
    # long lines
    if line == '@@@':
        linep = ''
        while True:
            line = infile.readline()
            #print(line)
            if line == '@@@\n':
                break
            linep = linep + line
        #
        lineout = toArabicParagraph(linep)
    else:
        #print('Not containing @@@')
        for c in line:
            if c == '@':
                indices.append(ichars)
            ichars = ichars + 1
        #
        N_indices = len(indices)
        start_prev = 0
        end_prev = 0
        if N_indices != 0:
            for i in range(0,N_indices,2):
                start = indices[i]
                end = indices[i+1]
                lineout = lineout + line[start_prev:start] + toArabicInline(line[start+1:end])
                start_prev = end+1
        else:
            lineout = lineout + line
    #
    print(lineout)  # output to file

#str1 = """ba bi bu
#ta ti tu"""
#
#print(toArabicParagraph(str1))


#    print(lineout)




#transliterateString("bisomi All~`hi Alr~aHom`ni Alr~aHom`ni Alr~aHiyomi")
