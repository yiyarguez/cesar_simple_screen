def encrypt(text: str, shift: int):
    """Encrypt the message using Cesar's encrypter basis alphabet list."""
    alphabet = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ")
    result = ""

    for char in text:

        if char.upper() in alphabet:
            char = char.upper()
            # Calculate the position in the alphabet and change to "new letter" after shift
            original_index = alphabet.index(char)
            new_index = (original_index + shift) % len(alphabet)
            new_char = alphabet[new_index]
            result += new_char
        else:
            result += char

    return result

def crearCifrador(d: int):
    def encriptar(mensaje):
        alphabet = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ")
        result = ""

        for char in mensaje:

            if char.upper() in alphabet:
                char = char.upper()
                # Calculate the position in the alphabet and change to "new letter" after shift
                original_index = alphabet.index(char)
                new_index = (original_index + d) % len(alphabet)
                new_char = alphabet[new_index]
                result += new_char
            else:
                result += char

        return result
    
    return encriptar


class Cifrador:
    def __init__(self, d):
        self.d = d
        self.cifrados_pendientes = 5

    def cifrar(self, mensaje):
        if self.cifrados_pendientes == 0:
            return "Compre en cifrados pepe!"

        self.cifrados_pendientes = self.cifrados_pendientes - 1
        
        return encrypt(mensaje, self.d)
    
    def descifrar(self, mensaje):
        return encrypt(mensaje, -self.d)


c3 = crearCifrador(3)
d3 = crearCifrador(-3)

print(c3("lolailo"))