from pathlib import Path
import sys

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    print('Falta instalar pypdf. Ejecute: python -m pip install pypdf')
    sys.exit(1)


def main():
    print('DIVISOR DE PDF')
    ruta = Path(input('Ruta del archivo PDF: ').strip().strip('"').strip("'"))
    if not ruta.is_file():
        raise ValueError('El archivo indicado no existe.')

    try:
        hojas = int(input('Número de hojas por archivo: ').strip())
        if hojas <= 0:
            raise ValueError
    except ValueError:
        raise ValueError('La cantidad de hojas debe ser un número entero mayor que cero.')

    nombre = input('Nombre base para los archivos: ').strip()
    if not nombre or nombre in ('.', '..') or any(c in nombre for c in '<>:"/\\|?*') or nombre.endswith(('.', ' ')):
        raise ValueError('Indique un nombre válido, sin caracteres como / \\ : * ? " < > |.')
    if nombre.lower().endswith('.pdf'):
        nombre = nombre[:-4]
    if not nombre:
        raise ValueError('El nombre base no puede estar vacío.')

    lector = PdfReader(str(ruta))
    if lector.is_encrypted and not lector.decrypt(''):
        raise ValueError('El PDF está protegido con contraseña y no se puede abrir.')
    total = len(lector.pages)
    if not total:
        raise ValueError('El PDF no contiene hojas.')

    salida = ruta.resolve().parent / 'salida'
    partes = (total + hojas - 1) // hojas
    digitos = max(3, len(str(partes)))
    destinos = [salida / f'{nombre}_{i:0{digitos}d}.pdf' for i in range(1, partes + 1)]
    existentes = [p for p in destinos if p.exists()]
    if existentes:
        raise ValueError(f'Ya existe el archivo {existentes[0]}. Use otro nombre base para evitar sobrescribirlo.')
    salida.mkdir(exist_ok=True)
    for indice, inicio in enumerate(range(0, total, hojas)):
        escritor = PdfWriter()
        fin = min(inicio + hojas, total)
        for pagina in range(inicio, fin):
            escritor.add_page(lector.pages[pagina])
        # El modo exclusivo evita sobrescribir archivos creados durante el proceso.
        with destinos[indice].open('xb') as archivo:
            escritor.write(archivo)
        print(f'{destinos[indice].name}: hojas {inicio + 1} a {fin} de {total}')
    print(f'\nListo. Se crearon {partes} archivos en: {salida}')


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f'Error: {error}', file=sys.stderr)
        sys.exit(1)

