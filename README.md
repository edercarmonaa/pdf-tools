# Herramientas para PDF

Dos utilidades de consola para buscar texto en archivos PDF y dividir un documento en partes de un n?mero determinado de p?ginas.

## El problema

Revisar manualmente muchos PDF para localizar una frase o separar un documento extenso en archivos manejables puede consumir tiempo y provocar omisiones. Estas herramientas ayudan a personas que trabajan con documentos locales a realizar esas tareas desde la consola.

## La soluci?n

El buscador revisa los PDF de una carpeta y muestra los archivos y p?ginas que contienen el texto indicado. El divisor recibe un PDF, el n?mero de p?ginas por parte y un nombre base; crea los archivos en una carpeta `salida` junto al original.

## Funcionalidades principales

- B?squeda de texto sin distinguir may?sculas, con normalizaci?n de espacios, en los PDF situados directamente en una carpeta.
- Indicaci?n de progreso, errores y posibilidad de cancelar la b?squeda con Esc.
- Divisi?n de un PDF por cantidad de p?ginas, con nombres numerados y protecci?n frente a sobrescritura.
- Aviso cuando un PDF est? protegido con contrase?a y no puede abrirse con una contrase?a vac?a.

## ?Qu? mejora este proyecto?

Permite localizar p?ginas con una frase sin abrir cada archivo manualmente y preparar partes numeradas de un documento largo sin separar sus p?ginas una a una.

## ?Para qui?n est? pensado?

Para personas que necesitan buscar o dividir documentos PDF desde una computadora Windows. No hay cuentas ni roles de usuario.

## Tecnolog?as utilizadas

- Python y biblioteca est?ndar.
- [pypdf](https://pypdf.readthedocs.io/) para leer y escribir PDF.
- `msvcrt` de la biblioteca est?ndar de Windows para cancelar la b?squeda.

## Requisitos

- Windows para ejecutar el buscador, que utiliza `msvcrt`.
- Python 3.13 y pip; es la versi?n con la que se verific? este proyecto.
- La dependencia indicada en `requirements.txt`.

## Instalaci?n

Una vez publicado el repositorio, sustituya la direcci?n por la URL real:

```powershell
git clone <URL_DEL_REPOSITORIO>
cd <CARPETA_DEL_REPOSITORIO>
py -3.13 -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
```

## Configuraci?n

No se requieren variables de entorno. `.env.example` documenta que actualmente no hay ninguna. Los PDF y hojas de c?lculo locales est?n excluidos de Git para reducir la exposici?n accidental de documentos; gu?rdelos localmente y revise su contenido antes de compartirlos.

## Ejecutar el proyecto

Desde la carpeta del proyecto:

```powershell
.\.venv\Scripts\python buscar_en_pdfs.py
.\.venv\Scripts\python dividir_pdf.py
```

Ejecute el comando correspondiente a la tarea deseada.

## Uso

1. Para buscar, indique la ruta de una carpeta y el texto. El programa informa el archivo y la p?gina de cada coincidencia. Pulse Esc para cancelar.
2. Para dividir, indique la ruta del PDF, la cantidad de p?ginas por parte y un nombre base. Los archivos se crean en `salida` junto al PDF original; si ya existe un destino, el programa se detiene para evitar sobrescribirlo.

## Estructura del proyecto

```text
buscar_en_pdfs.py  Buscador interactivo de texto en PDF
dividir_pdf.py     Divisor interactivo de PDF
requirements.txt   Dependencia de Python
.env.example       Configuraci?n de entorno, actualmente vac?a
```

## Seguridad

No incluya credenciales ni documentos privados en el repositorio. Mantenga cualquier configuraci?n sensible en variables de entorno y fuera de Git; `.env` est? ignorado y `.env.example` no contiene secretos. Revise tambi?n el contenido y los metadatos de cualquier documento que decida compartir. Para reportar un problema, contacte de forma privada a quien mantenga el repositorio; todav?a no se ha definido un canal espec?fico.

## Pruebas

No se incluye una suite de pruebas automatizada. Puede comprobar la sintaxis con:

```powershell
.\.venv\Scripts\python -m py_compile buscar_en_pdfs.py dividir_pdf.py
```

## Estado del proyecto

Prototipo de utilidades de consola. Se ha verificado con Python 3.13; no se incluye una suite automatizada ni una versi?n publicada.

## Limitaciones actuales

- El buscador solo examina PDF directamente dentro de la carpeta elegida; no recorre subcarpetas.
- La b?squeda depende del texto extra?ble del PDF. Los documentos escaneados sin OCR requieren reconocimiento de texto previo.
- Los PDF cifrados que requieren contrase?a no se procesan.
- El buscador requiere Windows; no se ha verificado el divisor en otros sistemas.
- No hay suite automatizada ni configuraci?n de CI.

## Pr?ximas mejoras

No hay una hoja de ruta definida. Cualquier mejora deber? distinguirse de las funcionalidades existentes descritas arriba.

## Contribuciones

Cuando exista un repositorio p?blico, cree un fork y una rama, realice cambios acotados, compruebe la sintaxis y el comportamiento afectado y abra un pull request describiendo el cambio y su verificaci?n.

## Licencia

Distribuido bajo la [licencia MIT](LICENSE). El titular de los derechos debe completarse en el archivo de licencia.
