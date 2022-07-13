
import bitstring
from binaryparser import *

format = []                                         # primer prueba
print("\nPrimer prueba\n")

format.append(format_item("v1","float"))            # agrego algunos formatos de prueba        
format.append(format_item("v2","int",32))
format.append(format_item("v3","uint",32))
format.append(format_item("v4","ascii",7*4))
format.append(format_item("v5","test",1))           # verifico que detecte el error de tipo no valido      
for i in format:                                    # muestro el formato 
    i.show()

source = {} 
source["v1"] = 1.00                                 # creo el diccionario que va a ser mi objeto de datos
source["v2"] = 100
source["v3"] = 100
source["v4"] = "hola"
print(source)
test1_encode = encode(source,format)
print(test1_encode.bin)                             # cambiar a .hex para tenerlo en hexadecimal
test1_decode = decode(test1_encode,format)
print(test1_decode)

del format
format = []                                         # segunda prueba
print("\nSegunda prueba\n")

format.append(format_item("v0","int",8))
format.append(format_item("v1","int",8))
format.append(format_item("v2","int",8))

buffer = bitstring.BitArray('0x010203')

print(buffer.hex)
test1_decode = decode(buffer,format)
print(test1_decode)
test1_encode = encode(test1_decode,format)
print(test1_encode.hex)                             



