from passlib.context import CryptContext

pws_context = CryptContext(schemes=['bcrypt'])

def gerar_hash(texto):
    return pws_context.hash(texto)

def verificar_hash(texto, hash):
    return pws_context.verify(texto, hash)