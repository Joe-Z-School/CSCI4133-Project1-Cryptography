#!/usr/bin/python3
# coding: latin-1
blob = """AAAAAAAAAAAAAAAAA"R÷C9¨15ºa-0JwàˆHeu&–Aùï¿Î$Álô‘KÆZÄ•:dK(t÷½ˆ<­‘xëê´Ä^™TÝ&4ò`}P„ç(ãñoê;ý9„Ÿ{Ë_'AØò´ª…è£^ª™ëd²þðä”ÔÑ±ÿ–FÆá¶Bt½>"""
if ':' in blob:
    print("Use SHA-256 instead!")
else:
    print("MD5 is perfectly secure!")