from flask import jsonify, render_template, flash, request
from api import app
from api.db.db import mysql
from api.models.cliente import Cliente
from api.models.producto import Producto


# LLAMAR A LOS PRODUCTOS
@app.route('/productos', methods=['GET'])
def get_all_products():
    cur = mysql.cursor()
    cur.execute('SELECT p.producto_id, p.nombreProd, p.marca, p.precio, p.cantidad, p.descripcion, u.usuario_id, u.nombre, c.cliente_id, c.nombre FROM Producto p JOIN Usuario u ON p.usuario_id = u.usuario_id JOIN Cliente c ON u.usuario_id = c.usuario_id'); 
    datos_todos= cur.fetchall()
    return jsonify(datos_todos)
    

    
# CAMBIAR DATOS A TRAVES DE SU ID
@app.route('/productos/<int:producto_id>', methods=['PUT'])
def update_product(producto_id):
    marca = request.get_json()["marca"]
    precio = request.get_json()["precio"]
    cantidad = request.get_json()["cantidad"]
    descripcion = request.get_json()["descripcion"]

    cur = mysql.cursor()
    cur.execute('UPDATE Producto SET marca = %s, precio = %s, cantidad = %s, descripcion = %s WHERE producto_id = %s', (marca, precio, cantidad, descripcion, producto_id))
    mysql.commit()
    return jsonify({'marca': marca, 'precio': precio, "cantidad": cantidad, "descripcion": descripcion})

# ELIMINAR UN PRODUCTO POR ID
@app.route('/products/<int:producto_id>', methods=['DELETE'])
def remove_product(producto_id):
    cur = mysql.cursor()
    cur.execute('DELETE FROM Producto WHERE producto_id = {}'.format(producto_id))
    mysql.commit()
    return jsonify({'Eliminamos el producto con el id': producto_id})
