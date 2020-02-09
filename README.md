# matilde
Matilde es un script de pruebas, para extraer información de las cabeceras, sea de un dominio o un subdominio; como también Tipos de consultas DNS, ejemplo:Dirección de host, Servidor de nombre de autorización, Nombre canónico para un alias, Destino de correo, Reemisor de correo, Inicio de una zona de autorización, Información del host, Información de buzón o de lista de correos, Transferencia de una zona entera, etc. También obtendrá información sobre la geolocalización del dominio. Por otra parte se generará un archivo .html del dominio o subdominio consultado.

# Requisitos
Python 3.*

# Instalación
Clone el repositorio a su directorio local:

`git clone https://github.com/mapachemirlo/matilde.git`

Instale las dependencias:

Ingrese al directorio `matilde` y ejecute:

`pip install -r requirements.txt`

Puede agregar el archivo `matilde.py` al $PATH para más comodidad.

# Uso
Ejecute:

`python matilde.py -d dominio`

# Nota
Tal vez deba agregar utf-8 de la siguiente manera:
`export PYTHONIOENCODING=UTF-8`

Puede utilizar Python 2.* modificando el archivo matilde.py, remplazando la linea `urllib.request.urlopen` por `urllib.urlopen`.
