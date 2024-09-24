import argparse


def caesar(entrada: str, shift: int) -> str:
    entrada = entrada.upper()
    salida = ''
    for i in range(len(entrada)):
        if not entrada[i].isalpha():
            salida += entrada[i]
        elif ord(entrada[i]) + shift < 65:
            salida += chr(ord(entrada[i]) + shift + 26)
        elif ord(entrada[i]) + shift > 90:
            salida += chr(ord(entrada[i]) + shift - 26)
        else:
            salida += chr(ord(entrada[i]) + shift)

    return salida


def main() -> None:
    parser = argparse.ArgumentParser(
        prog='Decodificador Caesar',
        description='El programa decifra frases cifradas con la clave Caesar.'
                    'Para esto requiere una frase y un número entero que corresponde al número de espacio'
                    'que se deben correr los caracteres en el abecedario.')

    parser.add_argument('-c', '--code', type=str, help='Código para decifrar')
    parser.add_argument('-s', '--shift', type=int, help='Número de espacios a correrse. Positivo para adelante'
                                                        ' y negativo para atrás.')
    args = parser.parse_args()

    print('\n' + caesar(args.code, args.shift))


if __name__ == '__main__':
    main()
