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

● Vas a crear un nuevo modelo.

● Vas a heredar los métodos create, unlink y write.

● Vas a llamar estos métodos.

● Vas a practicar la validación de datos con constraints.

● Creación de grupos de permisos y categoría de aplicaciones.

------------------------------------------------------------------------------------------------------------------

### Historia de usuario

● Como usuario de la aplicación Librería, quiero que se registre quién y cuándo alguien crea, modifica o elimina un registro de libro para mantener un control de las operaciones realizadas en el sistema.

● Como usuario de la aplicación Librería, quiero que al poner un precio negativo en un libro, aparezca un mensaje de error para controlar los precios.

------------------------------------------------------------------------------------------------------------------

### Criterios de aceptación

● Dado que un usuario ha creado, modificado o eliminado un libro y yo soy Administrador de la librería, cuando yo entré en el punto de Menú, Librería / Ajustes / Auditoría debe aparecer un registro de los cambios, con el tipo de acción (modificación, creación, eliminación), la fecha y hora de la acción y el usuario que la ha realizado.

● Dado que estoy en la creación o modificación de un libro, cuando ponga el precio menor que cero, entonces debe aparecer un mensaje de error.

------------------------------------------------------------------------------------------------------------------

### Descripción técnica

● Crea un nuevo modelo library.audit con los siguientes campos: operation selection de ‘create’,’write’,’unlink’, también "user_id" campo relacionado a un usuario, "date" (Datetime), "book_id".

● Crea un nuevo grupo de permisos, llamado Librería / Administrador, haz que solo este grupo tenga acceso al modelo library.audit. En el texto “Librería / Administrador” El valor Librería hace referencia a la categoría de aplicación y “Administrador” al grupo de permisos. Mira los recursos más abajo.

● Crea los puntos de menú Librería / Ajustes / Auditoría, para que muestre el listado de library.audit. En esta lista solo se han de poder modificar los registros.

● Hereda el método create dentro del modelo library.book para hacer que cada vez que se cree un libro, también se cree un registro en library.audit, con el usuario que la crea (self.env.user) la fecha actual y el tipo de operación “create”

● Haz lo mismo para el método write, y el método unlink.

● Utiliza el "@api.constrains" en el modelo library.book para evitar que el precio sea menor que cero.

------------------------------------------------------------------------------------------------------------------

### Recursos

● [Método Create](https://www.odoo.com/documentation/16.0/developer/reference/backend/orm.html?highlight=create#odoo.models.Model.create).

● [Método Write](https://www.odoo.com/documentation/16.0/developer/reference/backend/orm.html?highlight=write#odoo.models.Model.write).

● [Método Unlink](https://www.odoo.com/documentation/16.0/developer/reference/backend/orm.html?highlight=unlink#odoo.models.Model.unlink).

● [Crear categoría de aplicación](https://github.com/odoo/odoo/blob/38dbc6adbbc69218cfeaa7867558fbcb9488cfea/addons/account/security/account_security.xml#L31).

● [Crear grupos de permisos](https://github.com/odoo/odoo/blob/38dbc6adbbc69218cfeaa7867558fbcb9488cfea/addons/account/security/account_security.xml#L36).

● [Utilizar contraints](https://www.odoo.com/documentation/16.0/developer/reference/backend/orm.html?highlight=constrains#odoo.api.constrains).

------------------------------------------------------------------------------------------------------------------

> [!IMPORTANT]
> Es determinante cumplir con todos los criterios de aceptación.

> [!WARNING]
> Recuerda subir el PR y mencionar a Jesús Ramoneda para que haga las correcciones concretas.

> [!CAUTION]
> Corrige los fallos.