!! This should be treated as usual text.
! This is a comment
SUBROUTINE test(x,y)
  IMPLICIT NONE
  REAL(8) :: z
  z = x + y + sin(x*y)
  WRITE(*,*) 'This is a text'
END SUBROUTINE
