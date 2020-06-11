# JWT Crack

Progetto di sicurezza - Anno accademico 2019/2020

Componente software per il brute force di un Token JWT basato su dizionario

## Creazione dell'environment per l'installazione del progetto

- Il primo step prevede l'installazione di [Python](https://www.python.org/) e di [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) disponibile per i principali sistemi operativi. Virtualenv permette di creare ambienti python virtuali senza alterare le installazioni presenti sul sistema operativo principale

- Una volta installato Virtualenv si può procedere all'attivazione dell'ambiente e all'installazione delle componenti necessarie

```
# Si crea una directory per il progetto
$ mkdir jwtcrack
$ cd jwtcrack

# Si crea un ambiente denominato jwtcrack
$ virtualenv -p python3 jwtcrack
$ source jwtcrack/bin/activate
```

- Lo step successivo è quello che prevende l'installazione dei pacchetti necessari al funzionamento del codice. Nello specifico il software qui implementato fa uso di alcune routine della libreria PyJWT per verificare la correttezza del token ed effettuare la decodifica dello stesso

```
# Installazione della libreria PyJWT
(jwtcrack) $ pip install PyJWT

# Installazione della libreria tqdm - utile per rappresentare una progress bar nel caso il dizionario sia particolarmente grande
(jwtcrack) $ pip install tqdm
```

## Esecuzione

- All'interno del progetto è presente il file "dizionario.txt" che contiene una lista di chiavi possibili per operare l'attacco di tipo brute force. Ovviamente è possibile modificare tale file oppure utilizzare un proprio file.

- Per l'esecuzione vera e propria del software la sintassi è la seguente

### python unimoljwtcrack.py [Token o file contenente il Token] dizionario.txt


- Qui un esempio concreto
```
(jwtcrack) $ python unimoljwtcrack.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.AKe1WKQ1_TCuiDjuVCZoGF1zxCBSeQRAoJmlFRqR1pc dizionario.txt 
Provo a trovare la chiave del JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.AKe1WKQ1_TCuiDjuVCZoGF1zxCBSeQRAoJmlFRqR1pc
4it [00:00, 445.14it/s]
Ecco la chiave: pippo
```
