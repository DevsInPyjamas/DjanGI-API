# DjanGI

Se llama DjanGI porque es un trabajo de Gestión de la Información (GI) y lo vamos a desarrollar en Django por eso DjanGI es ingenioso no creen.

#### DjanGI API

Este respositorio contiene la API que se usará para realizar
el trabajo de la asignatura de Gestión de la Información (UMA curso 18-19)
en el que se nos propone realizar, en una tecnología alternativa, 
una conexión a una base de datos con una interfaz.

El objetivo de nuestra solución es crear una API en django para el backend
y utilizar REACT para la parte de interfaz.

### Testing the API
Pa hacerle tests a estas cosas hemos utilizado la herramienta `curl` para obtener
los JSONS generados por la API: varios ejemplos

```
curl -X POST -d '{"type_id": "B", "name": "PIEZA DE PRUEBA", "manufacturer": "RENLOL"}' localhost:8000/new_piece
```

Que inserta con un POST una pieza de prueba dentro de la BBDD
```
curl localhost:8000/all_types
```
que devuelve un JSON de todos los tipos de piezas