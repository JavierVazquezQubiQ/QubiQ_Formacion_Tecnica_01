# QubiQ 01 Formacion Tecnica

# PRÁCTICA MÓDULO 4

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

● Creación de campos relacionados Many2one, Many2many y One2many.

● Aplicar herencia de delegación en los modelos.

● Creación de pestañas en formularios.

● Diseño de tabla de one2many en campos formulario.

● Utilizar widget many2many_tags.

------------------------------------------------------------------------------------------------------------------

### Historia de usuario

● Yo como usuario quiero [poder vincular libros] para [poder visualizarlos en Productos].

● Yo como usuario de Odoo, [quiero asignar autores a los libros] para [clasificarlos].

● Yo como usuario de Odoo, [quiero asignar generós a los libros] para clasificarlos.

● Yo como usuario de Odoo quiero crear packs de libros.

● Yo como usuario de Odoo, quiero poder filtrar los tipos de packs dentro de la aplicación de librería.

------------------------------------------------------------------------------------------------------------------

### Criterios de aceptación

● Como he creado un libro desde el punto de menú Librería / Datos / Libros, entonces en el Inventario deben aparecer los libros dentro del submenú Productos.

● Como estoy dentro del formulario de un libro, cuando de clic en editar entonces he de poder agregar un autor, ya creado o por crear, en un campo del formulario.

● Como estoy dentro de un libro, cuando de clic en el campo géneros, entonces he de poder seleccionar varios géneros a la vez.

● Dado que estoy en el punto de menú Librería / Datos / Autores, cuando cree un autor entonces debo poder establecer varios géneros.

● Como estoy dentro de un formulario de un libro, ha de aparecer un check que indique si se trata de un pack.

● Como estoy dentro de un formulario de un libro, cuando de clic en el check es un pack, entonces ha de aparecer una nueva pestaña en el formulario, llamada componentes.

● Como estoy dentro de la pestaña componentes, cuando de clic en la tabla de componentes, entonces he de poder agregar, en la misma tabla, un nuevo libro y la cantidad del libro que incluye el pack.

● Como estoy dentro del menú Libros, cuando de clic en el filtro Packs, entonces solo se han de mostrar los libros que están marcados como Packs.

------------------------------------------------------------------------------------------------------------------

### Descripción técnica

● Asegúrate de tener instaladas las aplicaciones de Inventario y Contactos dentro de un entorno. Deben de ser dependientes de tu módulo.

● Vamos a hacer una herencia de delegación del libro con el producto.

● Vamos a hacer una herencia de delegación del modelo de autor que has creado en la práctica anterior, con el modelo de contactos.

● Vamos a relacionar el modelo de autor dentro del modelo de Libros. Si quiero que muchos libros tengan el mismo autor, ¿qué tipo de relación he de establecer?

● Del modelo de library.genre que has creado en la práctica anterior. Vincula este modelo con el libro con un campo llamado genre_ids. Quiero utilizar más de un género para un libro y los libros pueden compartir los mismos géneros. ¿Qué tipo de relación he de establecer?

● También vincula el campo de géneros con el autor.

● Crea un nuevo Boelano en el libro para determinar qué es un pack. Crea un nuevo modelo llamado library.book.component.line para crear la tabla de componentes. Relaciona esta tabla con el libro con un campo llamado component_ids. Quiero que un pack tenga muchas líneas de componentes y que estas sean únicas para el pack. ¿Que tipo de relación he de establecer?

● Crea un notebook en el libro, la página solo será visible si el libro se ha establecido como pack.

● Aplicar un filtro dentro de la vista de Libros para visualizar únicamente aquellos que forman packs.

● Crea las traducciones de los campos para este módulo.

------------------------------------------------------------------------------------------------------------------

### Recursos

● Como hacer una herencia de delegación.

https://drive.google.com/file/d/1xGosQzEsxMs4TpKrDlUbSGuIOrvHywl4/view

● Como relacionar campos Many2one.

https://drive.google.com/file/d/1eNfYWEqa4cTKdj4Yq69wAaxaIP55DbaJ/view

● Agregar pestañas en un formulario.

https://drive.google.com/file/d/1iFnOz1xaE4hpxJ9zXarCt6VdZ6TRvSVM/view