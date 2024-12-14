import random
import hashlib

# Leggi gli handle da un file txt
def leggi_handle(path: str) -> list:
    with open(path, 'r') as file:
        lista_handle = [line.strip() for line in file.readlines()]
    handle_hash = [(handle, hashlib.sha256(handle.encode()).hexdigest()) for handle in lista_handle]
    handle_hash.sort(key=lambda x: x[1])  # Ordina per hash

    # Scrivi gli hash ordinati su un file
    with open('hash_ordinati.txt', 'w') as hash_file:
        for handle, hash_value in handle_hash:
            hash_file.write(f"{handle}: {hash_value}\n")
    return handle_hash

# Funzione per generare gli abbinamenti dei regali
def genera_abbinamenti(lista_handle_hash, seed: str) -> list[tuple[str, str]]:
    random.seed(seed)
    regali = lista_handle_hash[:]
    random.shuffle(regali)  # Mescola gli utenti

    abbinamenti = []
    for i in range(len(lista_handle_hash)):
        if lista_handle_hash[i][0] == regali[i][0]:
            for j in range(i + 1, len(lista_handle_hash)):
                if regali[j][0] != lista_handle_hash[i][0]:
                    regali[i], regali[j] = regali[j], regali[i]
                    break

        abbinamenti.append((lista_handle_hash[i], regali[i]))

    return abbinamenti

# Funzione per visualizzare gli abbinamenti
def visualizza_abbinamenti(abbinamenti):
    for mittente, destinatario in abbinamenti:
        print(f"{mittente[0]} -> {destinatario[0]}")

# Funzione per scrivere gli abbinamenti su un file
def scrivi_abbinamenti(abbinamenti, path: str):
    with open(path, 'w') as file:
        for mittente, destinatario in abbinamenti:
            file.write(f"{mittente[1]} -> {destinatario[1]}\n")

# Funzione principale
def main(path: str) -> None:
    seed = input("Inserisci il seed per la generazione degli abbinamenti: ")
    handle_list = leggi_handle(path)
    abbinamenti = genera_abbinamenti(handle_list, seed)
    visualizza_abbinamenti(abbinamenti)
    scrivi_abbinamenti(abbinamenti, 'abbinamenti.txt')

if __name__ == '__main__':
    file_path = 'handle_telegram.txt'
    main(file_path)