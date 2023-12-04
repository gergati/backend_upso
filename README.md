
# API Usuarios UPSO

API donde traemos datos del usuario, clientes, productos, etc.


## Installation

instalar my-project con pip

```bash
  pip install flask
  pip install PyJWT
  pip install mysql
```
    
## base de datos MySQL

Crear la conexion a la base de dato.

```bash
    mysql = mysql.connector.connect(
        host='host',
        user='user',
        password='password',
        database='database'
    )
```


## API Reference

#### Get all items

```http
  GET /login/
```

| x-access-token | user-id     | Description                |
| :-------- | :------- | :------------------------- |
| `token` | `int` | **Required**. Your API token |

#### Endpoints

```http
  GET /usuario/usuario_id/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `usuario_id`      | `int` | **Required**. Id of item to fetch |

```http
  POST /usuario/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `usuario_id`      |  | **Required**. usuario_id of item to fetch |

```http
  PUT /usuario/usuario_id/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `usuario_id`      | `int` | **Required**. usuario_id of item to fetch |

```http
  DELETE /usuario/usuario_id/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `usuario_id`      | `int` | **Required**. Id of item to fetch |



## 🚀 Sobre mí
Estudiante de la carrera de Tecnicatura en Lenguajes de Programacion. En constante formacion, me gusta el mundo de Javascript y Python.


## 🛠 Herramientas
Javascript, HTML, CSS, React, Node, Python, Flask, MySQL, MongoDB.


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

