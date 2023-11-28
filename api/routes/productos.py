from flask import jsonify, render_template, flash, request
from api import app
import mysql.connector
from api.models.cliente import Cliente
from api.models.producto import Producto


# LLAMAR A LOS PRODUCTOS
@app.route('/products', methods=['GET', 'POST'])
def get_all_products():
    if request.method == 'POST':
        username = request.form['nombre']
        password = request.form['contraseña']

        cur = mysql.cursor()
        cur.execute("SELECT usuario_id FROM Usuario WHERE nombre = %s AND contraseña = %s", (username, password,))
        user_data = cur.fetchone()

        cur.execute('SELECT p.producto_id, p.nombreProd, p.marca, p.precio, p.cantidad, p.descripcion, u.usuario_id, u.nombre, c.cliente_id, c.nombre FROM Producto p JOIN Usuario u ON p.usuario_id = u.usuario_id JOIN Cliente c ON u.usuario_id = c.usuario_id WHERE u.usuario_id = %s', (user_data)); 
        datos_todos= cur.fetchall()
        #print({'DATOs':datos_todos})
        for dato in datos_todos:
        # Asegúrate de que datos_todos no sea un solo valor
            if isinstance(dato, int):
                print(f'El resultado es un solo valor: {dato}')
            else:
                print({
                    'producto_id': dato[0],
                    'nombreProd': dato[1],
                    'marca': dato[2],
                    'precio': dato[3],
                    'cantidad': dato[4],
                    'descripcion': dato[5],
                    'usuario_id': dato[6],
                    'nombre_usuario': dato[7],
                    'cliente_id': dato[8],
                    'nombre_cliente': dato[9]
                })          
        if user_data:
            # Usuario autenticado correctamente
            user_id = user_data[0]

            cur.execute("SELECT * FROM Cliente WHERE usuario_id = {}".format(user_id))
            data_client = cur.fetchall()
            print(data_client)

            if data_client:
                # Cliente encontrado
                cur.execute("SELECT * FROM Producto WHERE cliente_id = {}".format(data_client))
                productos = cur.fetchall()

                product_list = []
                for producto_row in productos:
                    objProducto = Producto(producto_row)
                    product_list.append(objProducto.to_json())

                return jsonify(product_list)
            else:
                return jsonify({"error": "Usuario autenticado, pero no se encontró el cliente."})
        else:
            # Usuario no autenticado
            return jsonify({"error": "Nombre de usuario o contraseña incorrectos"})

    return render_template('auth/login.html')
        

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
