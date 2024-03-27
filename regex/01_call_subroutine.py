import re

pattern = re.compile(r"[Cc][Aa][Ll][Ll] [A-Za-z0-0]", re.IGNORECASE)
res = pattern.match("call something()")
print(res)

res = pattern.match("Call something()")
print(res)

res = pattern.match("  Call something()")
print(res)


pattern = re.compile(r"\W*[Cc][Aa][Ll][Ll] [A-Za-z0-0]", re.IGNORECASE)
res = pattern.match("  Call something()")
print(res)
res = pattern.match("  Call   something()")
print(res)


pattern = re.compile(r"\W*[Cc][Aa][Ll][Ll]\W*[A-Za-z0-0].", re.IGNORECASE)
res = pattern.match("  Call something()")
print(res)
res = pattern.match("  Call   something()")
print(res)
res = pattern.match("Locally   something()")
print(res)
res = pattern.match("call subroutine1(arg1, arg2)")
print(res)
