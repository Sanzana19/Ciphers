import argparse


def atbash(entrada: str) -> str:
    entrada = entrada.upper()
    salida = ''
    for i in range(len(entrada)):
        if not entrada[i].isalpha():
            salida += entrada[i]
        elif ord(entrada[i]) < 78:
            salida += chr(90 - (ord(entrada[i]) - 65))
        else:
            salida += chr(65 - (ord(entrada[i]) - 90))

    return salida


def main() -> None:
    parser = argparse.ArgumentParser(
        prog='Decodificador Caesar',
        description='El programa decifra frases cifradas con la clave Atbash.'
                    'Para esto requiere una frase.')

    parser.add_argument('-c', '--code', type=str, help='Código para decifrar')
    args = parser.parse_args()

    print('\n' + atbash(args.code))


if __name__ == '__main__':
    main()
