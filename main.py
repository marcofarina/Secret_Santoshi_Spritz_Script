import random

# Leggi gli handle da un file txt
def leggi_handle(path: str) -> list:
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Funzione per generare gli abbinamenti dei regali
def genera_abbinamenti(lista_handle) -> list[tuple[str, str]]:
    # Crea una lista di abbinamenti, garantendo che nessun utente dia un regalo a sé stesso
    regali = lista_handle[:]
    random.shuffle(regali)  # Mescola gli utenti

    abbinamenti = []
    for i in range(len(lista_handle)):
        # A ogni utente assegno il prossimo nella lista, ma se è se stesso lo scambio
        if lista_handle[i] == regali[i]:
            for j in range(i + 1, len(lista_handle)):
                if regali[j] != lista_handle[i]:
                    regali[i], regali[j] = regali[j], regali[i]
                    break

        abbinamenti.append((lista_handle[i], regali[i]))

    return abbinamenti

# Funzione per visualizzare gli abbinamenti
def visualizza_abbinamenti(abbinamenti):
    for mittente, destinatario in abbinamenti:
        print(f"{mittente} -> {destinatario}")



# Funzione principale
def main(path: str) -> None:

    handle_list = leggi_handle(path)
    abbinamenti = genera_abbinamenti(handle_list)

    visualizza_abbinamenti(abbinamenti)


if __name__ == '__main__':
    # Percorso del file txt contenente gli handle
    file_path = 'handle_telegram.txt'
    main(file_path)