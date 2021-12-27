# 03 - Cara Kerja Program dan Bytecode

import time
start_time = time.time()

print("Hello")
print("world")
print("Hello world")

print("Hello Ukhty")
# ini adalah comment
a = 10
"""ada apa dengan 
ucup dan otong si ganteng 
dalam comment multiline"""
print(a)
print(time.time()-start_time, "detik")

# kita bisa mengcompile python ke
# yang namanya  bytecode
# cara mencompile, buka terminal dan tuliskan
# python -m py_compile Main.py