# QubiQ 01 Formacion Tecnica

# PRÁCTICA MÓDULO 2

Importante mira este video para saber cómo entregar las prácticas:

https://drive.google.com/file/d/1M-EO7EpAKfuPV3aawmip5uWua1unhjav/view

También puedes ver el documento PDF "Como crear PR de las prácticas".

------------------------------------------------------------------------------------------------------------------

### Indicaciones

● Crea un nuevo módulo para esta práctica

● Utiliza Odoo en su última versión EE.

● Para completar esta práctica, asegúrate de cumplir con todos los criterios de aceptación.

● En la descripción técnica vas a tener solo los conceptos más relevantes para la práctica.

● En recursos verás contenido para poder completar esta práctica.

● Si té quedas encallad@, utiliza chat GPT, si aún así no te salé, revisa la solución.

● Recuerda escribir todos los campos en Ingles, y hacer las traducciones al final de la práctica.

● Crea un repositorio en Gitlab para subir las prácticas.

● Haz un clon de tu repositorio en local.

● Crea una nueva rama y agrega solo el módulo de esta práctica.

● Haz un PR contra la rama principal de tu repositorio asignado y confirmalo.

------------------------------------------------------------------------------------------------------------------

### Historia de usuario

Yo como usuario quiero [poder registrar libros] para [poder tener una librería en Odoo].

------------------------------------------------------------------------------------------------------------------

### Criterios de aceptación

● Como he instalado el módulo, entonces en el menú principal debe aparecer la aplicación librería, con un icono personalizado.

● Como he hecho clic en la aplicación librería, entonces me deben aparecer un listado de libros registrados, si lo hubiera.

● Como he dado clic en crear, entonces me debe aparecer un formulario para rellenar la información del libro.

------------------------------------------------------------------------------------------------------------------

### Descripción técnica

● Crea un nuevo módulo llamado library.

● Crea un nuevo modelo llamado library.book para guardar la siguiente información:

Nombre Libro - Caracteres

Precio N- úmeros con Decimales

Edición - Números Enteros

Impreso o Digital - Selector

Enlace web de compra - Caracteres

Se ha comprado - Booleano (Si o No)

Fecha de la compra - Fecha

● Crear un punto de menú en la ventana principal para acceder a los libros.

● Agregale este icono al menú de la aplicación.

● El menú lanzará una vista para ver el nombre, precio y el enlace de compra de los libros que se han registrado.

● Y un formulario para rellenar la información de los campos, distribuidos en dos columnas por el espacio de este.

● Crea las traducciones de los campos para este módulo.

A pesar de haber dicho que el argumento string es opcional, vamos a incluirlo en todos los campos para tomar consciencia de que existe.

------------------------------------------------------------------------------------------------------------------

### Recursos

● Mirar esta referencia para saber los diferentes tipos de campos:

https://www.odoo.com/documentation/16.0/developer/reference/backend/orm.html#basic-fields

● Mira este video para saber como agregar iconos en los menu:

https://drive.google.com/file/d/1_qbedLk-fJP65SAD-Hr1TC4I3O_hD65K/view

● Como hacer traducciones con PO Edit:

https://drive.google.com/file/d/14LcmPF8f3URBcCmgtlFl17REJXxWKKWt/view

● Dar permisos al nuevo modelo. con ir.model.access.csv:

https://www.odoo.com/documentation/16.0/developer/tutorials/getting_started/05_securityintro.html#access-rights

● Cargar los documentos .py en el __init__.py y .xml en el data del manifest.

------------------------------------------------------------------------------------------------------------------

# Solución

https://drive.google.com/file/d/1h8v-s2sg6q1O3IA1k4qoMhbeOoGzqx_m/view
