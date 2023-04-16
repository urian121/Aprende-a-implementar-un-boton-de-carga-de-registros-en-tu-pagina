`Pequeño desarrollo con Python 3 la idea es poder cargar mas registros desde una BD, sin recargar la
pagina donde te encuentras, usando un emjemplo practico y facil de implementar en la vida real.`

# PASO 1, Crear mi entorno virtual

`python -m venv env `

# PASO 2, Activar el entorno virtual ejecutando;

`. env/Scripts/activate`

# PASO 3, Ya dentro del entorno virtual instalar flask

`pip install flask`

# PASO 4, Instalar Python MySQL Connector, es una bibliote (Driver) para conectar Python con MySQL

`pip install mysql-connector-python`

# Crear/Actualizar el fichero requirements.txt:

`pip freeze > requirements.txt`

# (env)$ deactivate Para desactivar nuestro entono virtual

# IMPORTANTE, para correr el proyecto solo debes ejecutar el archivo requirements.txt con el comando;

`pip install -r requirements.txt`

# en el mismo se encuentran todas las dependecias del proyecto.
