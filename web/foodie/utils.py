from cryptography.fernet import Fernet
from django.conf import settings

# Load the encryption key from settings
fernet = Fernet(settings.ENCRYPTION_SECRET_KEY)

def encrypt_id(id):
    """Encrypts an ID using Fernet symmetric encryption."""
    encrypted_id = fernet.encrypt(str(id).encode())
    return encrypted_id.decode()

def decrypt_id(encrypted_id):
    """Decrypts an encrypted ID using Fernet symmetric encryption."""
    decrypted_id = fernet.decrypt(encrypted_id.encode())
    return int(decrypted_id.decode())

def encrypt_object(obj, flag=0):
    """
    Encrypts an object's ID.

    Args:
        obj: The object to encrypt (single object or queryset).
        flag: 0 for single objects, 1 for querysets.

    Returns:
        The encrypted object(s).
    """
    if flag == 0:
        obj.encrypted_id = encrypt_id(obj.id)
        return obj
    elif flag == 1:
        encrypted_objs = []
        for item in obj:
            item.encrypted_id = encrypt_id(item.id)
            encrypted_objs.append(item)
        return encrypted_objs

def decrypt_object(obj, flag):
    """
    Decrypts an object's ID.

    Args:
        obj: The object to decrypt (single object or queryset).
        flag: 0 for single objects, 1 for querysets.

    Returns:
        The decrypted object(s).
    """
    if flag == 0:
        obj.id = decrypt_id(obj.encrypted_id)
        return obj
    elif flag == 1:
        decrypted_objs = []
        for item in obj:
            item.id = decrypt_id(item.encrypted_id)
            decrypted_objs.append(item)
        return decrypted_objs