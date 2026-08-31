#!/usr/bin/python3
# coding: latin-1
blob = """AAAAAAAAAAAAAAAAA"R÷C9¨15ºa-0JwàˆÈeu&–Aùï¿Î$Álô‘KÆZÄ;dK(t÷½ˆ<­‘øëê´Ä^™TÝ&4ò`}P„ç(ãñïê;ý9„Ÿ{Ë_'AØò´ª…è£^ª™ëd2þðä”ÔÑ±ÿ–FÆá6Bt½>"""
from hashlib import sha256
print(sha256(blob.encode("latin-1")).hexdigest())