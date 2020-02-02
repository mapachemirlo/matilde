# matilde
Matilde es un script de pruebas, para extraer información de las cabeceras, sea de un dominio o un subdominio; como también Tipos de consultas DNS, ejemplo:Dirección de host, Servidor de nombre de autorización, Nombre canónico para un alias, Destino de correo, Reemisor de correo, Inicio de una zona de autorización, Información del host, Información de buzón o de lista de correos, Transferencia de una zona entera, etc. También obtendrá información sobre la geolocalización del dominio. Por otra parte se generará un archivo .html del dominio o subdominio consultado.

# Requisitos
Python 3.*

# Instalación
Clone el repositorio a su directorio local:

`git clone https://github.com/mapachemirlo/matilde.git`

Instale las dependencias:

`pip install -r requirements.txt`

# Uso
Ejecute:

`python matilde.py -d dominio`

