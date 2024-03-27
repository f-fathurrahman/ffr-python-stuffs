import re
pattern = re.compile(r"\W*[Cc][Aa][Ll][Ll]\W*[A-Za-z0-0].", re.IGNORECASE)

filestr = open("gndstate.f90").readlines()
called_subroutines = []
for l in filestr:
    res = pattern.match(l)
    if res is not None:
        called_subroutines.append(res.string)

tmp = []
for c in called_subroutines:
    r = re.sub("[Cc][Aa][Ll][Ll]", "", c.strip()).strip()
    tmp.append(r.split("(")[0])

called_subroutines = set(tmp)

