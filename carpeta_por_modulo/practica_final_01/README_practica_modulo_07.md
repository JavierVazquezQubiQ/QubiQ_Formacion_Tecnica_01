# QubiQ 01 Formacion Tecnica

# PRÁCTICA FINAL 1

### Introducción

● En esta práctica vamos a tratar algunos conceptos vistos en todo el curso. Crearemos un nuevo módulo para realizar las historias de usuario.

------------------------------------------------------------------------------------------------------------------

### Historia de usuario

1 ● Yo como usuario quiero indicar que un contacto es un comercial, agregar un código de comercial si es que lo fuera, y un % de comisión por defecto. Además tener un filtro para solo ver comerciales en contactos.

2 ● Yo como usuario quiero impedir eliminar un comercial que tenga un código establecido e impedir agregar un código ya repetido, para evitar errores.

3 ● Yo como usuario quiero agregar líneas de comisiones directamente desde la tabla dentro del pedido de venta debajo del total de la venta, además no quiero poder crear nuevos comerciales desde esas líneas.

4 ● Yo como usuario quiero establecer por defecto el % del comercial al agregar una línea de comisión, sin embargo este % ha de ser editable. Además calcular automáticamente el importe de las comisiones a repartir cada vez que el importe total de la venta cambie o el % de la comisión lo haga.

5 ● Yo como usuario quiero reemplazar el comercial original en el informe de pedido de ventas por el nuevo listado que yo hemos agregado.

------------------------------------------------------------------------------------------------------------------

### Descripción técnica

1 ● Vamos a heredar el modelo contactos para agregar un campo check que diga si es comercial, otro campo alfanumérico que representa un código y un campo float para el % . Estos dos últimos campos se muestran en la vista cuando el contacto es un comercial. Agregaremos un filtro en el search de contactos para buscar aquellos que tengan el check marcado Los campos los mostraremos debajo del Saleperson en la ficha del contacto.

2 ● Para impedir eliminar un contacto con un código de comercial vamos a heredar el método Unlink lanzando un raise UserError dentro de este, y para establecer como único el campo código podemos utilizar [_sql_constraints](https://www.odoo.com/es_ES/forum/ayuda-1/how-to-make-a-unique-field-in-a-module-16386), puedes ver este [ejemplo en Odoo](https://github.com/odoo/odoo/blob/f964b761eae32016e36dd9d39cc2c35fc2270eba/addons/account/models/account_account.py#L89). Este campo tiene que tener el parámetro [copy=False](https://github.com/odoo/odoo/blob/f964b761eae32016e36dd9d39cc2c35fc2270eba/addons/account/models/account_bank_statement.py#L213) para que cuando copiemos el contacto el código no se copie.

3 ● Creamos un nuevo modelo que represente las líneas de comisiones, los campos son:

    Name -> Relación a uno con el modelo res.partner filtrado por los que son comerciales.

    Comisión -> % de comisión

Hacemos una relación en el pedido de ventas con este nuevo modelo. Recordamos que se deben poder introducir muchas líneas y estas serán únicas para cada pedido. ¿Qué tipo de relación crees que es? Agregamos el campo en la vista y utilizamos el atributo editable dentro del tree y options en el campo comercial para impedir que se puedan crear desde la misma tabla.

4 ● Para establecer por defecto el % de comisión cada vez que cambio el comercial en una línea que decorador he de utilizar? Luego para calcular el importe vamos a crear un nuevo campo computado que dependa del total de las ventas y el % de comisión de las líneas.

5 ● Vamos a heredar el informe de Presupuesto para cambiar el valor del comercial para agregar un listado separado por comas de los nombres de los comerciales de la nueva tabla.

------------------------------------------------------------------------------------------------------------------

### Consejos

● Debemos instalar el módulo contacts y agregarlo como dependencia.

● En algunas vistas puede ser que un campo se repita, hemos de ser más específicos en el selector para encontrar el que queremos.

● En la declaración de un campo puede utilizar el [parámetro domain](https://github.com/odoo/odoo/blob/f964b761eae32016e36dd9d39cc2c35fc2270eba/addons/account/models/account_journal.py#L20) para filtrar los registros que se mostrarán.

● En el depends puedo indicar como disparador un campo dentro de un campo relacionado. (“<nombre_campo_relacionado>”.”<nombre_campo_dentro_del_modelo>”).

------------------------------------------------------------------------------------------------------------------

### Recursos / Solución

● [Campos](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_1/models/res_partner.py#L9), [vista Formulario](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_1/views/res_partner.xml#L10), [filtro](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_1/views/res_partner.xml#L24).

● [SQL constraint](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_1/models/res_partner.py#L14).

● [Nuevo Modelo](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_1/models/sale_commission.py#L8), [vista](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_1/views/sale_order.xml#L12).

● [Cambio de comisión](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_1/models/sale_commission.py#L19), [importe de comisión](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_1/models/sale_commission.py#L23).

● [Modificando informe](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_1/views/report_sale.xml#L6).

------------------------------------------------------------------------------------------------------------------

> [!IMPORTANT]
> Es determinante cumplir con todos los criterios de aceptación.

> [!WARNING]
> Recuerda subir el PR y mencionar a Jesús Ramoneda para que haga las correcciones concretas.

> [!CAUTION]
> Corrige los fallos.
