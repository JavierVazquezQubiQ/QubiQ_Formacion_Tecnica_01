# QubiQ 01 Formacion Tecnica

# PRÁCTICA MÓDULO 7 - INFORMES

### Indicaciones

● Recuerda escribir todos los campos en Ingles, y [hacer las traducciones al final de la práctica](https://drive.google.com/file/d/14LcmPF8f3URBcCmgtlFl17REJXxWKKWt/view).

● Asegúrate de tener la rama principal de tu repositorio actualizada.

● Crea una nueva rama en tu repositorio de GIT local para trabajar en esta práctica.

● Continua ampliando el mismo módulo que hiciste en la práctica anterior.

● Para completar esta práctica, asegúrate de cumplir con todos los criterios de aceptación.

● En la descripción técnica vas a tener solo los conceptos más relevantes para la práctica.

● En recursos verás contenido para poder completar esta práctica.

● Si té quedas encallad@, utiliza chat GPT, si aún así no te salé, revisa la solución.

● Haz un PR contra la rama principal de tu repositorio asignado y confirmalo.

------------------------------------------------------------------------------------------------------------------

### Que vas a practicar

● Vas a crear un nuevo modelo.

● Vamos a utilizar campos para imágenes y html.

● Vamos a crear un nuevo informe.

● Vamos a modificar un informe ya existente.

------------------------------------------------------------------------------------------------------------------

### Historia de usuario

● Como usuario de la aplicación quiero agregar imagen de portada a los libros y una sinopsis.

● Como usuario de la aplicación Libreria, quiero sacar un listado de todos los libros disponibles, con su imagen, descripción, autor y año de publicación.

● Como usuario de la aplicación, quiero que al imprimir un presupuesto de venta, aparezca el número de socio al lado de donde aparece el comercial.

● Como usuario del sistema quiero quitar el número de página a todos los informes que imprima.

------------------------------------------------------------------------------------------------------------------

### Criterios de aceptación

● Al acceder al formulario de creación o edición de un libro, debería haber un campo para cargar una imagen de portada y para poner la sinopsis en formato html.

● Dado que estoy en el listado de libros, cuando yo seleccione uno o varios, debe aparecer la opción Imprimir portfolios.

● Como que dado clic a Imprimir portfolios entonces debe aparecer una página por libro seleccionado, con el título,autor, año publicación, imagen de portada, sinopsis.

● Como tengo un presupuesto para un cliente que es socio de la librería, entonces cuando imprima el presupuesto debe aparecer el número de socio al lado del comercial.

● Como he impreso un presupuesto cualquiera, entonces no debe aparecer el número de página debajo.

------------------------------------------------------------------------------------------------------------------

### Descripción técnica

● En la práctica 4 hicimos una herencia de delegación del modelo library.book con el modelo product.template, recuerdas? Esto quiere decir que ya disponemos un campo para la imagen del libro, porque el product.template lo tiene de base. Averigua cual es el nombre de ese campo y agregalo en el formulario de la creación de libros, dentro de la app Librería.

● Para la sinopsis vamos a crear un nuevo campo HTML.

● Pregunta al chat GPT que es Qweb. Configura en Ajustes / Parámetros del sistema / la clave report.url con el valor http://localhost:8069 esto es para cargar el css dentro de los informes.

● Vamos a crear un nuevo report con su diseño y vamos hacer que aparezca en el modelo de libros, el diseño es abierto siempre y cuando aparezca la información que se pide en los criterios de aceptación.

● Vamos a heredar el report de presupuestos de ventas para modificar el diseño y hacer que aparezca el número de socio al lado del comercial, si el cliente del presupuesto es socio. Utiliza el atributo t-if para condicionar elementos de qweb.

● Vamos a heredar la plantilla de la compañía, visible en Ajustes / Ajustes General. Para modificarla y quitar el pie de página.

------------------------------------------------------------------------------------------------------------------

### Recursos

● [Creación de informes](https://www.odoo.com/documentation/16.0/developer/reference/backend/reports.html#).

● [Sintaxis herencia informes](https://github.com/odoo/odoo/blob/0a8e42027b5adea48554ada87fc70632a19c6a60/addons/account/views/account_portal_templates.xml#L15).

● [Sintaxis de t-if](https://github.com/odoo/odoo/blob/0a8e42027b5adea48554ada87fc70632a19c6a60/addons/account/data/mail_template_data.xml#L19).

------------------------------------------------------------------------------------------------------------------

> [!IMPORTANT]
> Es determinante cumplir con todos los criterios de aceptación.

> [!WARNING]
> Recuerda subir el PR y mencionar a Jesús Ramoneda para que haga las correcciones concretas.

> [!CAUTION]
> Corrige los fallos.
