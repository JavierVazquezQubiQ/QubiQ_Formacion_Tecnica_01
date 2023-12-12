# QubiQ 01 Formacion Tecnica

# PRÁCTICA MÓDULO 5

### Requisitos

● Haber realizado el entrenamiento funcional de las aplicaciones de compras, ventas e inventario.

------------------------------------------------------------------------------------------------------------------

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

● Vas a configurar valores por defecto en acciones.

● Condicionar visibilidad de campos en las vistas.

● Crear filtros en las vistas.

● Utilizar el decorador @onchange en un método.

● Flujo funcional de compra y recepción de libros.

● Flujo de ventas de libros.

● Heredar métodos que llaman botones.

● Hacer un campos computados.

------------------------------------------------------------------------------------------------------------------

### Historia de usuario

● Yo como usuario de Odoo, [quiero distinguir los packs] para [poder catalogarlos como Sagas o Colecciones].

● Yo como usuario quiero separar el nombre y apellido de los autores para poder dirigirme a ellos de forma informal.

● Yo como usuario quiero poder traspasar los géneros de un autor en la creación de un nuevo libro.

● Yo como usuario de Odoo, quiero [poder realizar compras de libros para tener stock disponible] para cuando se precise realizar una venta.

● Yo como usuario de Odoo, quiero que a la hora de hacer una venta, [únicamente se debe poder hacer a los socios]

------------------------------------------------------------------------------------------------------------------

### Criterios de aceptación

● Dado que estoy en la creación de un nuevo libro, cuando yo seleccione un Autor que tiene géneros establecido, entonces estos géneros se han de pasar al campo géneros del libro.

● Dado que estoy en la creación de un nuevo libro desde Librería / Datos Libros, cuando marque el check es un pack, entonces debe aparecer un campo “Tipo de Pack” selector con las opciones de "Sagas" o "Colecciones". Por defecto debe de ser "Colecciones".

● Dado que estoy en Librería / Datos / Libros, cuando seleccione el filtro "Colecciones", deben aparecer todos los libros que tienen el check de pack marcado y el campo "Tipo de pack" como “Colecciones”. Hacer lo mismo para el filtro "Sagas".

● Dado que estoy en la creación de un nuevo Autor, cuando yo abra el formulario entonces he de ver el campo nombre y apellidos.

● Dado que estoy en la creación de un nuevo Autor, cuando yo rellene los campos nombre y apellidos entonces se debe completar el campo nombre, con la información del nombre completo.

● Dado que estoy en la creación de un libro con el check “Es un Pack” marcado y un valor establecido en el campo Tipo de Colección, cuando yo desmarque el check “Es un Pack” entonces se debe vaciar el campo Tipo de Colección.

● Dado que estoy en Librería / Datos / Libros, cuando yo cree un nuevo libro entonces por defecto se ha de marcar el tipo de producto como “Almacenable”.

● Dado que estoy en la aplicación de compras, cuando yo haga una compra y la confirme para el libro , cuando confirme el albarán generado entonces se ha de sumar el stock del libro.

● Dado que he creado una venta, con un cliente que no tiene el check de socio marcado, cuando yo confirme la venta, entonces debe aparecer un mensaje de error en la pantalla diciendo “You can only sell to members”.

------------------------------------------------------------------------------------------------------------------

### Descripción técnica

● Haz un método @onchange para que cuando cambie el check de es pack, el campo tipo de pack se vacíe o se ponga como "Colección" por defecto.

● Vamos a crear un campo selector en el modelo de libros.

● Para crear los filtros se utilizan dos condiciones, que sea un pack y que sea "Colección/Saga". La sintaxis para hacer esto, es [ (campo1’, 'op', valor1), (‘campo2’, ‘op’, valor2) ].

● Crea dos campos nuevos en el modelo de autor, uno será "first_name" y el otro "last_name".

● Haz que el campo name sea computado y dependa de el "first_name" y el "last_name" también haz que se guarde en la base de datos.

● ¿Recuerdas cómo agregar valores por defecto cuando se crean registros desde ciertas vistas?

● Genera una orden de compra para un libro que esté como tipo almacenable, confirma el albarán y comprueba que se ha sumado su stock.

● Vamos a heredar el método que se llama al confirmar una venta para modificarlo, vamos a comprobar que el cliente "partner_id" del pedido de venta tenga el check es un socio marcado, si no lo tiene, entonces debes lanzar un "UserError".

● Crea las traducciones de los campos para este módulo.

------------------------------------------------------------------------------------------------------------------

### Recursos

● Cómo heredar un método de un botón.

● Como hacer un onchange.

● Como hacer un campo computado.

● Cómo lanzar mensajes de error al usuario.

● Traduciendo valores en los métodos.

------------------------------------------------------------------------------------------------------------------

> [!IMPORTANT]
> Es determinante cumplir con todos los criterios de aceptación.

> [!WARNING]
> Recuerda subir el PR y mencionar a Jesús Ramoneda para que haga las correcciones concretas.

> [!CAUTION]
> Corrige los fallos.