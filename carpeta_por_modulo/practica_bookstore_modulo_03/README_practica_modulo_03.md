# QubiQ 01 Formacion Tecnica

# PRÁCTICA MÓDULO 3

### Indicaciones

● Recuerda escribir todos los campos en Ingles, y hacer las traducciones al final de la práctica.

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

● Creación de submenus.

● Creación de nuevos modelos.

● Creación de filtros.

● Agregar atributos de invisibilidad en los campos de forma condicionada.

● Establecer filtros por defecto desde una acción.

● Establecer un dominio por defecto en una acción.

● Establecer valores por defecto en una acción.

● Creación de permisos de acceso para modelos.

------------------------------------------------------------------------------------------------------------------

### Historia de usuario

● Yo como usuario de Odoo, [quiero registrar géneros en el sistema] para [poder clasificarlos].

● Yo como usuario de Odoo, [quiero registrar socios en el sistema] para [poder alquilar libros en un futuro].

● Yo como usuario de Odoo, [quiero registrar autores en el sistema] para [poder asignar libros en un futuro].

● Yo como usuario de Odoo, quiero poder filtrar los socios dentro de la aplicación de librería.

------------------------------------------------------------------------------------------------------------------

### Criterios de aceptación

● Como estoy en la aplicación de librería, cuando yo dé clic en el submenú Datos, entonces deben aparecer 4 submenús en un desplegable. Libros, Géneros, Autores y Socios.

● Cuando de clic en el submenú Libros entonces me debe de llevar al listado de libros.

● Como he dado clic en Géneros entonces deben aparecer una lista con los géneros creados, además he de poder crear los géneŕos directamente desde la lista.

● Como estoy en Contactos, cuando le de clic en crear, entonces debe aparecer en el formulario un campo para marcar que es un socio de la librería.

● Como he indicado que es un socio, entonces debe mostrarse un campo para rellenar un número de socio.

● Como he dado clic en el menú Socios, entonces se ha de abrir un kanban y tree, como opción, filtrando solo los contactos que tiene marcado que són socios.

● Como he dado clic en crear desde el punto de menú Socios, entonces en el formulario del contacto, debe aparecer marcado que es un socio por defecto.

● Como estoy dentro del menú de contactos entonces ha de aparecer un filtro para mostrar solo los contactos que són socios.

● Como estoy en Contactos, cuando le de clic en crear, entonces debe aparecer en el formulario un campo para marcar que es un autor de libros.

● Como he dado clic en el menú Autores, entonces se ha de abrir un kanban y tree, como opción, y deben aparecer solo los contactos que són autores.

● Como he dado clic en crear desde el punto de menú Autores, entonces en el formulario del contacto, debe aparecer marcado que es un autor por defecto.

------------------------------------------------------------------------------------------------------------------

### Descripción técnica

● Asegúrate de tener instalada la aplicación de Contactos dentro de un entorno. Deben de ser dependientes de tu módulo.

● Para distinguir qué Contactos son Socios o Autores, crear dos campos en el modelo de contactos que sean booleanos. Uno que indique si es socio y el otro que indique si es autor.

● Crearemos otro campo en contactos para agregar el número de socio, solo debe ser visible si el campo boleando del socio está marcado.

● Vamos a crear un nuevo modelo llamado library.book.genre para los géneros. Recuerda agregar permisos de acceso desde la carpeta security.

● Aplicaremos valores y un dominio por defecto a al punto de menú Librería / Datos / Socio, para que desde ese punto de menú, solo muestre los contactos que són socios y además se marque por defecto es socio cuando se crea un contacto desde allí.

● Para los autores vamos hacer lo mismo a excepción de que en vez de aplicar un filtro agregaremos un dominio a la acción.

● Aplicar un filtro por defecto dentro de la vista de Socios para visualizar únicamente aquellos Contactos que sí lo son.

● Crea las traducciones de los campos para este módulo Consejos.

● Cada vez que creamos un nuevo modelo, hemos de permisos de acceso, se puede hacer en el archivo /security/ir.model.acess.csv

● Cada vez que agregamos un nuevo .py en el módulo nos hemos de asegurar que se indique su carga en el archivo __init__.py de la carpeta.

● Las traducciones no se visualizan si tenemos el –dev=xml activado en el docker-compose

------------------------------------------------------------------------------------------------------------------

### Recursos

● Cómo heredar un modelo existente para modificarlo.

https://drive.google.com/file/d/1AJrHPqcvmEaAJxnjWbqtkyz7QxcIsjiU/view

● Como crear submenus.

https://drive.google.com/file/d/1j2GncG_KcXv6dWKGLrktw3FiYTczOcbm/view

● Como condicionar visibilidad de campos según otros valores.

https://drive.google.com/file/d/1RmasapD6k27rgVrgQjiUdWtXIPXHJ4my/view

● Como poner valores por defecto en una acción.

https://drive.google.com/file/d/1IrjYCRtrp-gJBriAuoUJslmCNkb9exly/view

● Como poner filtros por defecto en una acción.

https://drive.google.com/file/d/1Q8RnKUhiDE8kyJZe9EiovgVoN8YzqMOF/view