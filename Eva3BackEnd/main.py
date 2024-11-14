from PIL import Image
from cryptography.fernet import Fernet

def main():
    # Código que utiliza estas librerías
    img = Image.open('imagen.jpg')
    img.show()

    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(b"A really secret message. Not for prying eyes.")
    print(token)
    decrypted_token = f.decrypt(token)
    print(decrypted_token.decode())

if __name__ == "__main__":
    main()
    
 # Esto se utiliza para que el codigo superior solo se ejecute cuando el modulo se ejecute