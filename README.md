# Herramientas para PDF

Dos utilidades de consola para buscar texto en archivos PDF y dividir un documento en partes de un número determinado de páginas.

## El problema

Revisar manualmente muchos PDF para localizar una frase o separar un documento extenso en archivos manejables puede consumir tiempo y provocar omisiones. Estas herramientas ayudan a personas que trabajan con documentos locales a realizar esas tareas desde la consola.

## La solución

El buscador revisa los PDF de una carpeta y muestra los archivos y páginas que contienen el texto indicado. El divisor recibe un PDF, el número de páginas por parte y un nombre base; crea los archivos en una carpeta `salida` junto al original.

## Funcionalidades principales

- Búsqueda de texto sin distinguir mayúsculas, con normalización de espacios, en los PDF situados directamente en una carpeta.
- Indicación de progreso, errores y posibilidad de cancelar la búsqueda con Esc.
- División de un PDF por cantidad de páginas, con nombres numerados y protección frente a sobrescritura.
- Aviso cuando un PDF está protegido con contraseña y no puede abrirse con una contraseña vacía.

## ¿Qué mejora este proyecto?

Permite localizar páginas con una frase sin abrir cada archivo manualmente y preparar partes numeradas de un documento largo sin separar sus páginas una a una.

## ¿Para quién está pensado?

Para personas que necesitan buscar o dividir documentos PDF desde una computadora Windows. No hay cuentas ni roles de usuario.

## Tecnologías utilizadas

- Python y biblioteca estándar.
- [pypdf](https://pypdf.readthedocs.io/) para leer y escribir PDF.
- `msvcrt` de la biblioteca estándar de Windows para cancelar la búsqueda.

## Requisitos

- Windows para ejecutar el buscador, que utiliza `msvcrt`.
- Python 3.13 y pip; es la versión con la que se verificó este proyecto.
- La dependencia indicada en `requirements.txt`.

## Instalación

Una vez publicado el repositorio, sustituya la dirección por la URL real:

```powershell
git clone <URL_DEL_REPOSITORIO>
cd <CARPETA_DEL_REPOSITORIO>
py -3.13 -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
```

## Configuración

No se requieren variables de entorno. `.env.example` documenta que actualmente no hay ninguna. Los PDF y hojas de cálculo locales están excluidos de Git para reducir la exposición accidental de documentos; guárdelos localmente y revise su contenido antes de compartirlos.

## Ejecutar el proyecto

Desde la carpeta del proyecto:

```powershell
.\.venv\Scripts\python buscar_en_pdfs.py
.\.venv\Scripts\python dividir_pdf.py
```

Ejecute el comando correspondiente a la tarea deseada.

## Uso

1. Para buscar, indique la ruta de una carpeta y el texto. El programa informa el archivo y la página de cada coincidencia. Pulse Esc para cancelar la búsqueda actual y escriba otra palabra o frase para iniciar una nueva búsqueda. Al terminar una búsqueda también puede buscar otro texto; deje la entrada vacía para salir.
2. Para dividir, indique la ruta del PDF, la cantidad de páginas por parte y un nombre base. Los archivos se crean en `salida` junto al PDF original; si ya existe un destino, el programa se detiene para evitar sobrescribirlo.

## Estructura del proyecto

```text
buscar_en_pdfs.py  Buscador interactivo de texto en PDF
dividir_pdf.py     Divisor interactivo de PDF
requirements.txt   Dependencia de Python
.env.example       Configuración de entorno, actualmente vacía
```

## Seguridad

No incluya credenciales ni documentos privados en el repositorio. Mantenga cualquier configuración sensible en variables de entorno y fuera de Git; `.env` está ignorado y `.env.example` no contiene secretos. Revise también el contenido y los metadatos de cualquier documento que decida compartir. Para reportar un problema, contacte de forma privada a quien mantenga el repositorio; todavía no se ha definido un canal específico.

## Pruebas

No se incluye una suite de pruebas automatizada. Puede comprobar la sintaxis con:

```powershell
.\.venv\Scripts\python -m py_compile buscar_en_pdfs.py dividir_pdf.py
```

## Estado del proyecto

Prototipo de utilidades de consola. Se ha verificado con Python 3.13; no se incluye una suite automatizada ni una versión publicada.

## Limitaciones actuales

- El buscador solo examina PDF directamente dentro de la carpeta elegida; no recorre subcarpetas.
- La búsqueda depende del texto extraíble del PDF. Los documentos escaneados sin OCR requieren reconocimiento de texto previo.
- Los PDF cifrados que requieren contraseña no se procesan.
- El buscador requiere Windows; no se ha verificado el divisor en otros sistemas.
- No hay suite automatizada ni configuración de CI.

## Próximas mejoras

No hay una hoja de ruta definida. Cualquier mejora deberá distinguirse de las funcionalidades existentes descritas arriba.

## Contribuciones

Cuando exista un repositorio público, cree un fork y una rama, realice cambios acotados, compruebe la sintaxis y el comportamiento afectado y abra un pull request describiendo el cambio y su verificación.

## Licencia

Distribuido bajo la [licencia MIT](LICENSE). El titular de los derechos debe completarse en el archivo de licencia.
