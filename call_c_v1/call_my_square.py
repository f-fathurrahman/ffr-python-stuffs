import ctypes

libso_file = "my_square.so"

my_lib = ctypes.CDLL(libso_file)

print(type(my_lib))

my_lib.my_square.restype = ctypes.c_double # set the output type
res = my_lib.my_square( ctypes.c_double(3.0) )
print("res = ", res)
