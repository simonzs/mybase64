import base64
import random

class MyBase64(object):

    STANDARD_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    def __init__(self, alphabet=None):
        if alphabet == None:
            alphabet = MyBase64.STANDARD_ALPHABET
        if len(alphabet) != len(MyBase64.STANDARD_ALPHABET):
            raise RuntimeError('MyBase64 init error:alphabet len should equal 64')
        self.alphabet = alphabet

    def encode(self, data:str):
        encoded = base64.b64encode(data.encode('utf-8')).decode('utf-8')
        return encoded.translate(str.maketrans(MyBase64.STANDARD_ALPHABET, self.alphabet))

    def decode(self, data:str):
        encoded = data.translate(str.maketrans(self.alphabet, MyBase64.STANDARD_ALPHABET))
        return base64.b64decode(encoded).decode('utf-8')

    @staticmethod
    def random_alphabet():
        temp = MyBase64.STANDARD_ALPHABET
        out = ''
        while (True):
            size = len(temp)
            if size <= 0:
                break
            index = random.randint(0, size - 1)
            out = out + temp[index]
            if index + 1 >= size:
                temp = temp[0:index]
            else:
                temp = temp[0:index] + temp[index + 1:]
        return out
alphabet = 'stMiqpWmcJvAe3H+DTuRdoIkZ2UCGhl98aXBgE/Pw6r1x5z4LVONnjyb0fKFSQY7'

mybase64 = MyBase64(alphabet)
