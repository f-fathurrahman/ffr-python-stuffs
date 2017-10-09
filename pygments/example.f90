!!>
!!> This should be treated as usual text.
!!> An example of Latex equation
!!> \begin{equation}
!!> \alpha = \beta + \frac{x^2 - 1}{s - t^2}
!!> \label{eq:fabulous}
!!> \end{equation}
!!>
! This is a comment
SUBROUTINE test(x,y,s,t)
!!> The following modules will be imported:
  USE m_globals, ONLY : var1, var2
!!> Pygments \LaTeX macros should be available for use
!!> \PY{n}{DP} is for double precision
  USE m_prec, ONLY : DP
  IMPLICIT NONE
!!> An example of inline math: $\frac{4}{5\sqrt{x}}$
  REAL(8) :: x, y, s, t
  REAL(8) :: z
  z = x + y + sin(x*y)
  WRITE(*,*) 'This is a text'
!!> Implement the equation \ref{eq:fabulous}
  alpha = beta + (x**2 - 1.d0)/(s - t**2)
END SUBROUTINE

!!> OK, that's all folks!
