from flask import request,jsonify
from api.db.db import mysql
from api import app
from api.models.factura_producto import FacturaProducto


@app.route('/facturaProd', methods=['GET'])
def factura_productos():
    cur = mysql.cursor()
    cur.execute('SELECT f.facturaProd_id, u.usuario_id, u.nombre, p.producto_id, p.nombreProd, p.marca, p.precio, p.cantidad, p.descripcion FROM FacturaProducto f JOIN Usuario u ON f.usuario_id = u.usuario_id JOIN Producto p ON f.producto_id = p.producto_id')
    data = cur.fetchall()
    productosLista = []
    for row in data:
        factura = {
            'factProd_id': row[0],
            'usuario':{
                'usuario_id': row[1],
                'nombre': row[2],
            },
            'producto':{
                'producto_id': row[3],
                'nombreProd': row[4],
                'marca': row[5],
                'precio': row[6],
                'cantidad': row[7],
                'descripción': row[8],
            },
        }
        productosLista.append(factura)
    return jsonify(productosLista)