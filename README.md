# JWT Crack

Progetto di sicurezza - Anno accademico 2019/2020

Componente software per il brute force di un Token JWT basato su dizionario

## Creazione dell'environment per l'installazione del progetto

- Il primo step prevede l'installazione di [Anaconda](https://www.anaconda.com/products/individual) disponibile per i principali sistemi operativi. Anaconda permette di creare ambienti python virtuali senza alterare le installazioni presenti sul sistema operativo principale

- Una volta installato Anaconda si può procedere all'attivazione dell'ambiente e all'installazione delle componenti necessarie

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
# Si installa PyJWT
(jwtcrack) $ pip install PyJWT
```

# Appunti su esecuzione
