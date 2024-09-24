import argparse


def vigenere(entrada: str, key: str) -> str:
    entrada = entrada.upper()
    key = key.upper()
    salida = ''
    j = 0
    for i in range(len(entrada)):
        if entrada[i].isalpha():
            if ord(entrada[i]) >= ord(key[j]):
                salida += chr(65 + ord(entrada[i]) - ord(key[j]))
            else:
                salida += chr(91 + ord(entrada[i]) - ord(key[j]))
            if j == len(key)-1:
                j = 0
            else:
                j += 1
        else:
            salida += entrada[i]
    return salida


def main() -> None:
    parser = argparse.ArgumentParser(
        prog='Decodificador Vigenère',
        description='El programa decifra frases cifradas con la clave Vigenère. '
                    'Para esto requiere una frase y una palabra llave para decifrarla.')

    parser.add_argument('-c', '--code', type=str, help='Frase a decifrar entre doble comillas. Ejemplo: '
                                                       '"Hola mundo!"')
    parser.add_argument('-k', '--key', type=str, help='Palabra llave para decifrar entre comillas.'
                                                      ' Ejemplo: "llave"')
    args = parser.parse_args()

    print(vigenere(args.code, args.key))


if __name__ == '__main__':
    main()
