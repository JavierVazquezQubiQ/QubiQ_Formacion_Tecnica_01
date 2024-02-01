# QubiQ 01 Formacion Tecnica

# PRÁCTICA FINAL 3

### Introducción

● Esta práctica va relacionada con la práctica número 2, donde hicimos packs de productos con componentes.

● A nuestro departamento de ventas le ha encantado ver en la descripción de venta, los componentes que forman el pack.

● Ahora nos propone mejorar el módulo para desglosar en líneas de ventas los componentes de un pack.

● Utiliza el módulo de la [práctica anterior](https://docs.google.com/document/d/1CFpCpLgT1qACPe2l4bYJI8KKf6ix-dQyw61SMq6wBP4/edit) para realizar esta práctica.

------------------------------------------------------------------------------------------------------------------

### Historia de usuario

1 ● Yo como usuario quiero poder indicar que una venta corresponde a un pack.

2 ● Yo como usuario quiero que al seleccionar que una venta incluye un pack, tener la posibilidad de seleccionar el pack a incluir.

3 ● Yo como usuario quiero que al seleccionar un pack, la línea de venta se actualice automáticamente incluyendo los productos de este pack.

4 ● Yo como usuario quiero que al cambiar de pack, los productos añadidos anteriormente desaparezcan y sean sustituidos por el nuevo pack.

------------------------------------------------------------------------------------------------------------------

### Descripción técnica

1 ● En esta historia de usuario, debemos de heredar la vista 'sale.view_order_form' por tal de poder crear un checkbox para indicar si la venta corresponde a un pack.

2 ● En el caso de que el check box este marcado, es decir, que la venta incluye un pack, aparecerá un nuevo campo en el que podemos seleccionar que los packs que tenemos disponibles.

3 ● Para ello debemos de crear una función o método que al seleccionar el pack, se creará una o más líneas de venta correspondientes a los productos que incluye este. Para crear una línea, una posibilidad es utilizar el método 'new'. La [función ‘new’](https://github.com/odoo/odoo/blob/db927e1a95c035c96b102a08df50bee92eecb9a2/addons/sale_management/models/sale_order.py#L221) es muy parecida al create, con la diferencia de que el nuevo registro no se crea en la base de datos, sino que se mantiene en la memoria caché.

4 ● Por tal de que no se acumulen productos de packs que ya no están seleccionados, debemos eliminarlos primero de la línea de venta cada vez que cambiamos de pack.

------------------------------------------------------------------------------------------------------------------

### Recursos / Solución

● [Mapa conceptual creado por un alumno](https://drive.google.com/file/d/1c46kzTYvCJHkCqS90Rmqd2k0Er26ObD3/view).

● [Campo](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_3/models/pack.py#L64),[vista](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_3/views/pack.xml#L127).

● [Vista](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_3/views/pack.xml#L129).

● [Agregando líneas de packs](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_3/models/pack.py#L71).

● [Eliminar productos anteriores](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_3/models/pack.py#L74).

------------------------------------------------------------------------------------------------------------------

> [!IMPORTANT]
> Es determinante cumplir con todos los criterios de aceptación.

> [!WARNING]
> Recuerda subir el PR y mencionar a Jesús Ramoneda para que haga las correcciones concretas.

> [!CAUTION]
> Corrige los fallos.
