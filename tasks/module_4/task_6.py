"""Module4/Task6: Very sophisticated password breaker."""
from PyPDF2 import PdfFileReader
import threading


# Vars
DICTIONARY_PATH = 'resources/task_6/dictionary.txt'
PDF_PATH = 'resources/task_6/encrypted.pdf'


def decrypt_pdf_password():
    password = None

    with open(DICTIONARY_PATH, 'r') as eng_dict, open(PDF_PATH, 'rb') as enc_pdf:
        my_pdf = PdfFileReader(enc_pdf)
        for word in eng_dict.read().splitlines():
            if my_pdf.decrypt(word.upper()) or my_pdf.decrypt(word.lower()):
                password = word

        if password:
            print(f'Password decrypted: {password}')


if __name__ == '__main__':
    decrypt_pdf_password()
