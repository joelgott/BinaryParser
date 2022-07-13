import bitstring

# los objeto datos van a ser un diccionario 
# las tramas un BitArray
# los format una lista de format_items

class format_item:
    def __init__(self, tag, typevar, len=32):
        self.tag = tag
        self.typevar = typevar
        self.len = len
    def show(self):
        print("tag:" + self.tag + ", type:" + self.typevar + ", len:" + str(self.len))

def decode(buffer, format): # trama -> ObjetoDatos
    result = {}
    bits = buffer.copy()
    for format_item in format:
        lenght = format_item.len
        if format_item.typevar == "int":
            result[format_item.tag] = bits[:lenght].int
            del bits[:lenght]
        elif format_item.typevar == "uint":
            result[format_item.tag] = bits[:lenght].uint
            del bits[:lenght]
        elif format_item.typevar == "float":
            result[format_item.tag] = bits[:lenght].float
            del bits[:lenght]
        elif format_item.typevar == "ascii":
            result[format_item.tag] = ''
            for i in range(int(lenght/7)):
                result[format_item.tag] += chr(bits[:7].uint)
                del bits[:7]
        else:
            error_handler() # manejo de error de tipo no encontrado
    return result



def encode(src, format): # ObjetoDatos -> trama  
    result = bitstring.BitArray('')
    for format_item in format:
        if format_item.typevar == "int":
            result.append(bitstring.BitArray(int=src[format_item.tag], length=format_item.len))
        elif format_item.typevar == "uint":
            result.append(bitstring.BitArray(uint=src[format_item.tag], length=format_item.len))
        elif format_item.typevar == "float":
            result.append(bitstring.BitArray(float=src[format_item.tag], length=32))
        elif format_item.typevar == "ascii":
            for char in src[format_item.tag]:
                bits = list(bytes(char, 'ascii'))
                result.append(bitstring.BitArray(uint=bits[0], length=7))
        else:
            error_handler() # manejo de error de tipo no encontrado
    return result

def error_handler():
    print("error")

