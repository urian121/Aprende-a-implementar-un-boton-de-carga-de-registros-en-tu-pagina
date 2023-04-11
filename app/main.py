from flask import Flask, jsonify, json, request, render_template
from conexionBD import connectionBD #Importando conexión a BD


# Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)


@app.route("/", methods=['GET'])
def registros():
    if request.method == 'GET':
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        querySQL = f"SELECT * FROM personas order by id_persona DESC LIMIT 5"
        cursor.execute(querySQL)
        list_personas = cursor.fetchall()
        conexion_MySQLdb.commit()
        return render_template('public/index.html', list_personas=list_personas)
    else:
        return 'Método HTTP incorrecto'



#La primera línea es un decorador de ruta que define una ruta dinámica con una variable en la URL llamada "ultimoId"
@app.route("/loader_more/<int:ultimoId>", methods=['GET'])
@app.route("/loader_more", defaults={"ultimoId": 5})
def loader(ultimoId):
    """
    @app.route("/loader_more", defaults={"ultimoId": 5})
    La segunda línea también es un decorador de ruta que define una ruta sin variables en la URL,
    y que por defecto establece un valor "5" para la variable "ultimoId". En otras palabras,
    si se accede a la ruta sin proporcionar un valor para "ultimoId", se utilizará el valor predeterminado de 5
    """
    print(f"llegue ", ultimoId)
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)
    
      
    querySQL = f"SELECT * FROM personas WHERE id_persona < {ultimoId} ORDER BY id_persona DESC LIMIT 5"
    cursor.execute(querySQL)
    list_personas = cursor.fetchall()
    conexion_MySQLdb.commit()
    if(len(list_personas)>0):
        return render_template('public/load_more.html', list_personas=list_personas)
    else:
        return jsonify({'fin':0})



# Ejecutando el objeto Flask
if __name__ == '__main__':
    app.run(debug=True, port=5020)
