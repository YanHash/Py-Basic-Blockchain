import hashlib

"""Renvoie, en hexadécimal, le resultat de la fonctrion de hashage SHA256

:param hashable: la donnée dont on souhaite avoir le hash
"""
def hashFunction(hashable):
    return hashlib.sha256(hashable.encode()).hexdigest()