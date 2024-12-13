# Secret Santoshi Spritz Script 🎅🎁🍹

Un semplice script Python per generare abbinamenti casuali tra handle Telegram per il Secret Santa del Satoshi Spritz di Torino. Lo script garantisce che:
- ogni utente regala a un altro utente scelto casualmente;
- nessun utente può regalare a sé stesso;
- se l’utente A regala a B, B non può regalare ad A.

## Funzionalità
- **Input**: Una lista di handle Telegram fornita tramite un file .txt (uno per riga). 
- **Output**: Gli abbinamenti in formato mittente -> destinatario, visualizzati nella console.

## Esempio di utilizzo
1.	Prepara un file handle_telegram.txt con i nomi o gli handle degli utenti, uno per riga:

```
user1
user2
user3
user4
```

2. Posiziona il file nella **stessa directory** dello script.
3. Esegui lo script da linea di comando:
```
python main.py
```
4. In output vengono visualizzati gli abbinamenti generati:
```
user1 -> user3
user2 -> user4
user3 -> user2
user4 -> user1
```

## Struttura del progetto
```
SecretSanta/
├── handle_telegram.txt    # File di input con gli handle degli utenti
├── secret_santa.py        # Script principale
└── README.md              # Descrizione del progetto
```

## Satoshi Spritz Torino
Vuoi unirti ad un Satoshi Spritz a Torino? Unisciti al canale Telegram: @satoshispritztorino