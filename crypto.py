#Se importan las librerías necesarias
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from os import urandom

#Se genera una clave de 32 bytes y un IV de 16 bytes 
# IV se refiere a "Initialization Vector,"
def generar_clave_y_iv():
    key = urandom(32)  
    iv = urandom(16)     
    return key, iv

def encriptar(texto_plano, key, iv):
    #Se crea el cifrador AES en modo CBC
    #AES se refiere a "Advanced Encryption Standard"
    #CBC se refiere a "Cipher Block Chaining"
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    #Se convierte el texto plano a bytes
    # utf-8 se refiere a "Unicode Transformation Format - 8 bits"
    texto_plano_bytes = texto_plano.encode('utf-8')
    #Se agrega padding al texto plano para que su longitud sea múltiplo de 16
    padding_length = 16 - (len(texto_plano_bytes) % 16)
    padding = bytes([padding_length] * padding_length)
    texto_a_cifrar = texto_plano_bytes + padding

    #Se encripta el texto con padding
    texto_cifrado = encryptor.update(texto_a_cifrar) + encryptor.finalize()
    return texto_cifrado

#Función para desencriptar el texto cifrado
def desencriptar(texto_cifrado, key, iv):
    """Desencripta el texto cifrado usando AES en modo CBC."""
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    texto_desencriptado_padding = decryptor.update(texto_cifrado) + decryptor.finalize()
    
   #eliminar el padding
    padding_length = texto_desencriptado_padding[-1]
    # :-padding_length realiza un corte desde el inicio hasta la longitud del padding
    texto_desencriptado = texto_desencriptado_padding[:-padding_length]  
    # Se regresa el texto desencriptado como una cadena UTF-8
    return texto_desencriptado.decode('utf-8')

#Ejemplo de uso

#1 Se generan la clave y el IV
key, iv = generar_clave_y_iv()

#2 Se define el texto original
texto_original = "Carlos David Rojas Talavera"

#3 Se encripta el texto original
texto_encriptado = encriptar(texto_original, key, iv)
print("Texto Encriptado:", texto_encriptado)

#4 Se desencripta el texto encriptado
texto_desencriptado = desencriptar(texto_encriptado, key, iv)
print("Texto Desencriptado:", texto_desencriptado)