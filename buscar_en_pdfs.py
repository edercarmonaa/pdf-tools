from pathlib import Path
import msvcrt
import sys

try:
    from pypdf import PdfReader
except ImportError:
    print('Falta instalar pypdf. Ejecute: py -m pip install pypdf')
    sys.exit(1)


def cancelar():
    while msvcrt.kbhit():
        tecla = msvcrt.getwch()
        if tecla == '\x1b':
            return True
        if tecla in ('\x00', '\xe0') and msvcrt.kbhit():
            msvcrt.getwch()
    return False


def progreso(fraccion, archivo):
    porcentaje = min(100.0, max(0.0, fraccion * 100))
    llenos = int(porcentaje / 5)
    barra = '#' * llenos + '-' * (20 - llenos)
    # Limitar la longitud evita que la línea de progreso ocupe varias líneas.
    nombre = archivo if len(archivo) <= 40 else archivo[:37] + '...'
    print(f'\r[{barra}] {porcentaje:6.2f}% {nombre:<40}', end='', flush=True)


def mensaje(texto):
    print('\r' + ' ' * 75 + '\r' + texto, flush=True)


def buscar(carpeta, texto):
    archivos = sorted((p for p in carpeta.iterdir() if p.is_file() and p.suffix.lower() == '.pdf'), key=lambda p: p.name.casefold())
    if not archivos:
        print('No se encontraron archivos PDF en la carpeta.')
        return

    coincidencias = errores = completados = 0
    cancelado = False
    consulta = ' '.join(texto.split()).casefold()
    print('\nPresione Esc para detener la búsqueda.\n')
    for indice, archivo in enumerate(archivos):
        if cancelar():
            cancelado = True
            break
        progreso(indice / len(archivos), archivo.name)
        try:
            lector = PdfReader(str(archivo))
            if lector.is_encrypted and not lector.decrypt(''):
                mensaje(f'No se pudo abrir {archivo.name}: está protegido con contraseña.')
                errores += 1
            else:
                total_paginas = len(lector.pages)
                for numero, pagina in enumerate(lector.pages, start=1):
                    if cancelar():
                        cancelado = True
                        break
                    try:
                        contenido = ' '.join((pagina.extract_text() or '').split()).casefold()
                        if consulta in contenido:
                            mensaje(f'Encontrado: {archivo.name} — hoja {numero}')
                            coincidencias += 1
                    except Exception as error:
                        mensaje(f'No se pudo leer {archivo.name}, hoja {numero}: {error}')
                        errores += 1
                    progreso((indice + numero / total_paginas) / len(archivos), archivo.name)
        except Exception as error:
            mensaje(f'No se pudo leer {archivo.name}: {error}')
            errores += 1
        if cancelado:
            break
        completados += 1
        progreso(completados / len(archivos), archivo.name)

    mensaje('Búsqueda cancelada por el usuario.' if cancelado else 'Búsqueda terminada.')
    if not coincidencias:
        print('No se encontraron coincidencias en las hojas revisadas.')
    print(f'Archivos procesados: {completados} de {len(archivos)}. Hojas con coincidencias: {coincidencias}. Errores: {errores}.')
    print('Nota: los PDF escaneados sin texto reconocible requieren OCR.')


def main():
    print('BUSCADOR DE TEXTO EN PDF')
    ruta = input('Ruta de la carpeta con archivos PDF: ').strip().strip('"').strip("'")
    if not ruta:
        raise ValueError('Indique una carpeta.')
    carpeta = Path(ruta)
    if not carpeta.is_dir():
        raise ValueError('La carpeta indicada no existe.')

    while True:
        texto = input('\nTexto a buscar (deje vacío para salir): ').strip()
        if not texto:
            break
        buscar(carpeta, texto)


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as error:
        print(f'Error: {error}', file=sys.stderr)
        sys.exit(1)
