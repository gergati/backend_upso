from flask import jsonify, request
from api import app
from api.db.db import mysql
from api.models.producto import Producto


# LLAMAR A LOS PRODUCTOS
@app.route('/productos', methods=['GET'])
def productos():
    cur = mysql.cursor()
    cur.execute('SELECT p.producto_id, p.nombreProd, p.marca, p.precio, p.cantidad, p.descripcion, u.usuario_id, u.nombre, c.cliente_id, c.nombre FROM Producto p JOIN Usuario u ON p.usuario_id = u.usuario_id JOIN Cliente c ON u.usuario_id = c.usuario_id'); 
    data = cur.fetchall()
    productosLista = []
    for row in data:
        producto = {
            'producto_id': row[0],
            'nombreProd': row[1],
            'marca': row[2],
            'precio': row[3],
            'cantidad': row[4],
            'descripcion': row[5],
            'usuario': {
                'usuario_id': row[6],
                'nombre': row[7]
            },
            'cliente': {
                'cliente_id': row[8],
                'nombre': row[9]
            }
        }
        productosLista.append(producto)
    return jsonify(productosLista)
    

    
# CAMBIAR DATOS A TRAVES DE SU ID
@app.route('/productos/<int:producto_id>', methods=['PUT'])
def actualizar_productos(producto_id):
    nombreProd = request.get_json()['nombreProd']
    marca = request.get_json()["marca"]
    precio = request.get_json()["precio"]
    cantidad = request.get_json()["cantidad"]
    descripcion = request.get_json()["descripcion"]

    cur = mysql.cursor()
    cur.execute('UPDATE Producto SET nombreProd = %s, marca = %s, precio = %s, cantidad = %s, descripcion = %s WHERE producto_id = %s', (nombreProd,marca, precio, cantidad, descripcion, producto_id))
    mysql.commit()
    return jsonify({'nombreProd': nombreProd,'marca': marca, 'precio': precio, "cantidad": cantidad, "descripcion": descripcion})


# CREAR PRODUCTOS NUEVOS
@app.route('/productos', methods=['POST'])
def crear_productos():
    usuario_id = request.get_json()['usuario_id']
    nombreProd = request.get_json()['nombreProd']
    marca = request.get_json()['marca']
    precio = request.get_json()['precio']
    cantidad = request.get_json()['cantidad']
    descripcion = request.get_json()['descripcion']

    cur = mysql.cursor()
    cur.execute('INSERT INTO Producto (usuario_id, nombreProd, marca, precio, cantidad, descripcion) VALUES (%s,%s,%s,%s, %s, %s)', (usuario_id, nombreProd, marca, precio, cantidad, descripcion))
    mysql.commit()
    return jsonify({'usuario_id': usuario_id, 'nombreProd': nombreProd, 'marca': marca, 'precio': precio, 'cantidad': cantidad, "descripcion": descripcion })



# ELIMINAR UN PRODUCTO POR ID
@app.route('/productos/<int:producto_id>', methods=['DELETE'])
def eliminar_productos(producto_id):
    cur = mysql.cursor()
    cur.execute('DELETE FROM Producto WHERE producto_id = {}'.format(producto_id))
    mysql.commit()
    return jsonify({'Eliminamos el producto con el id': producto_id})
