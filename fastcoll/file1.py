#!/usr/bin/python3
# coding: latin-1
blob = """AAAAAAAAAAAAAAAAA"R÷C9¨15ºa-0JwàˆHeu&–Aùï¿Î$Álô‘KÆZÄ•:dK(t÷½ˆ<­‘xëê´Ä^™TÝ&4ò`}P„ç(ãñoê;ý9„Ÿ{Ë_'AØò´ª…è£^ª™ëd²þðä”ÔÑ±ÿ–FÆá¶Bt½>"""
from hashlib import sha256
print(sha256(blob.encode("latin-1")).hexdigest())