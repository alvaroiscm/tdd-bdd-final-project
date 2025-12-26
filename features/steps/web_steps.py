# features/steps/web_steps.py

from behave import given, when, then
import requests
from requests.exceptions import HTTPError

BASE_URL = "http://localhost:5000/products"  # Ajusta la URL según tu configuración

# Given step para asegurar que un producto con un id específico existe
@given('que el producto con el id "{product_id}" existe')
def step_impl(context, product_id):
    url = f"{BASE_URL}/{product_id}"
    response = requests.get(url)
    if response.status_code == 404:
        raise HTTPError(f"Producto con id {product_id} no encontrado")
    context.product = response.json()

# When step para obtener un producto por id
@when('se solicita el producto con el id "{product_id}"')
def step_impl(context, product_id):
    url = f"{BASE_URL}/{product_id}"
    context.response = requests.get(url)

# Then step para verificar que la respuesta tenga el código 200
@then('la respuesta debe ser un código 200')
def step_impl(context):
    assert context.response.status_code == 200

# Then step para verificar que el nombre del producto es correcto
@then('el nombre del producto debe ser "{product_name}"')
def step_impl(context, product_name):
    product = context.response.json()
    assert product['name'] == product_name

# When step para actualizar un producto
@when('actualizo el producto con el id "{product_id}" con los siguientes datos:')
def step_impl(context, product_id):
    url = f"{BASE_URL}/{product_id}"
    data = {row['name']: row['value'] for row in context.table}
    response = requests.put(url, json=data)
    context.response = response

# Then step para verificar que el código de la respuesta es 200
@then('la respuesta debe ser un código 200')
def step_impl(context):
    assert context.response.status_code == 200

# When step para borrar un producto por id
@when('se solicita la eliminación del producto con el id "{product_id}"')
def step_impl(context, product_id):
    url = f"{BASE_URL}/{product_id}"
    context.response = requests.delete(url)

# Then step para verificar que el código de respuesta es 204
@then('la respuesta debe ser un código 204')
def step_impl(context):
    assert context.response.status_code == 204

# Given step para crear productos adicionales
@given('que hay {product_count} productos existentes')
def step_impl(context, product_count):
    for i in range(int(product_count)):
        data = {
            "name": f"Product {i}",
            "description": f"Description of Product {i}",
            "price": 100 + i,
            "available": True,
            "category": "Electronics"
        }
        response = requests.post(BASE_URL, json=data)
        assert response.status_code == 201

# When step para listar todos los productos
@when('se solicita la lista de productos')
def step_impl(context):
    context.response = requests.get(BASE_URL)

# Then step para verificar la cantidad de productos
@then('debe haber {product_count} productos en la lista')
def step_impl(context, product_count):
    data = context.response.json()
    assert len(data) == int(product_count)

# When step para filtrar productos por nombre
@when('se solicita la lista de productos con el parámetro "name" igual a "{name}"')
def step_impl(context, name):
    response = requests.get(f"{BASE_URL}?name={name}")
    context.response = response

# When step para filtrar productos por categoría
@when('se solicita la lista de productos con el parámetro "category" igual a "{category}"')
def step_impl(context, category):
    response = requests.get(f"{BASE_URL}?category={category}")
    context.response = response

# When step para filtrar productos por disponibilidad
@when('se solicita la lista de productos con el parámetro "available" igual a "{available}"')
def step_impl(context, available):
    response = requests.get(f"{BASE_URL}?available={available}")
    context.response = response
