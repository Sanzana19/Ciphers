import argparse


def a1z26(entrada: str) -> str:
    salida = ''
    salida_final = ''

    for i in range(len(entrada)):
        if entrada[i] == '-' or entrada[i].isdigit():
            salida += entrada[i]
        else:
            salida += '-' + str(ord(entrada[i])+300) + '-'

    if salida[0] == '-':
        salida = salida[1:len(salida)]
    if salida[-1] == '-':
        salida = salida[0:len(salida) - 1]

    salida = salida.replace('--', '-')
    salida = salida.split('-')

    for i in range(len(salida)):
        if int(salida[i]) < 300:
            salida_final += chr(int(salida[i]) + 64)
        else:
            salida_final += chr(int(salida[i]) - 300)
    return salida_final


def main() -> None:
    parser = argparse.ArgumentParser(
        prog='Decodificador Caesar',
        description='El programa decifra frases cifradas con la clave A1Z26.'
                    'Para esto requiere una frase.')

    parser.add_argument('-c', '--code', type=str, help='Código para decifrar')
    args = parser.parse_args()

    print('\n' + a1z26(args.code))


if __name__ == '__main__':
    main()
