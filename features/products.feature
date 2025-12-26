# features/products.feature

Feature: Product Management

  # Escenario de Leer un producto
  Scenario: Leer un producto
    Given que el producto con el id "1" existe
    When se solicita el producto con el id "1"
    Then la respuesta debe ser un código 200
    And el nombre del producto debe ser "Test Product"
    
  # Escenario de Actualizar un producto
  Scenario: Actualizar un producto
    Given que el producto con el id "1" existe
    When actualizo el producto con el id "1" con los siguientes datos:
      | name         | "Updated Product"     |
      | description  | "Updated description" |
      | price        | "150"                 |
      | available    | "true"                |
      | category     | "Electronics"         |
    Then la respuesta debe ser un código 200
    And el nombre del producto debe ser "Updated Product"

  # Escenario de Borrar un producto
  Scenario: Borrar un producto
    Given que el producto con el id "1" existe
    When se solicita la eliminación del producto con el id "1"
    Then la respuesta debe ser un código 204
    And el producto con el id "1" ya no debe existir

  # Escenario de Listar todos los productos
  Scenario: Listar todos los productos
    Given que hay 5 productos existentes
    When se solicita la lista de productos
    Then la respuesta debe ser un código 200
    And debe haber 5 productos en la lista

  # Escenario de Buscar productos por nombre
  Scenario: Buscar productos por nombre
    Given que hay un producto con el nombre "Test Product"
    When se solicita la lista de productos con el parámetro "name" igual a "Test Product"
    Then la respuesta debe ser un código 200
    And el nombre del producto en la lista debe ser "Test Product"

  # Escenario de Buscar productos por categoría
  Scenario: Buscar productos por categoría
    Given que hay un producto con la categoría "Electronics"
    When se solicita la lista de productos con el parámetro "category" igual a "Electronics"
    Then la respuesta debe ser un código 200
    And la categoría del producto en la lista debe ser "Electronics"

  # Escenario de Buscar productos por disponibilidad
  Scenario: Buscar productos por disponibilidad
    Given que hay un producto con disponibilidad "true"
    When se solicita la lista de productos con el parámetro "available" igual a "true"
    Then la respuesta debe ser un código 200
    And el producto en la lista debe estar disponible
