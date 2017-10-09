from __future__ import print_function

from pygments import highlight
from pygments.lexers import FortranLexer
from pygments.formatters import LatexFormatter

# code = '''
# SUBROUTINE test(x,y)
#   IMPLICIT NONE
#   REAL(8) :: x, y
#   WRITE(*,*) x + y
# END SUBROUTINE
# '''

lines = open('example.f90').readlines()

PRELINE = '''
\documentclass[a4paper]{article}
\usepackage{fancyvrb}
\usepackage{xcolor}\n\n
'''

MIDLINE = '''
\\begin{document}
'''

print(PRELINE)
print( LatexFormatter().get_style_defs() )

print(MIDLINE)

print('\\begin{Verbatim}[commandchars=\\\\\{\\}]')
for l in lines:
    str1 = highlight(l, FortranLexer(), LatexFormatter()).split('\n')
    Nlen = len(str1)
    for il in range(1,Nlen-2):
        print( str1[il] )

print('\\end{Verbatim}')


ENDLINE = '''
\\end{document}
'''

print(ENDLINE)
