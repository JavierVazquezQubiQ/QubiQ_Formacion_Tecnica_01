# QubiQ 01 Formacion Tecnica

# PRÁCTICA FINAL 2

### Introducción

● En esta segunda práctica final vamos a seguir practicando conceptos vistos en todo el curso. Crearemos un nuevo módulo para realizar las historias de usuario. Esta práctica está ambientada en la creación de productos pack.

------------------------------------------------------------------------------------------------------------------

### Historia de usuario

1 ● Yo como usuario quiero poder definir si un producto es un pack, en caso afirmativo habilitar una nueva pestaña en la ficha del producto para agregar líneas con el producto componente, su cantidad y el precio.

2 ● Yo como usuario quiero poder seleccionar el método para calcular el precio, si es el total de el precio de cada componente o un precio que yo establezca.

3 ● Yo como usuario quiero que al agregar una pack en un pedido de venta agregando en la descripción los nombres componentes del pack - y su cantidad.

4 ● Yo como usuario quiero poder filtrar los productos que son packs y poder agrupar los packs por sus componentes.

5 ● Yo como usuario quiero extraer un informe dentro del producto para ver el desglose de sus componentes la cantidad y el precio.
------------------------------------------------------------------------------------------------------------------

### Descripción técnica

1 ● Creamos un nuevo modelo para hacer referencia a las líneas de los packs. Los campos han de ser los siguientes:
    ● Un campo que se relacione con el producto pack.
    ● Un campo para definir el producto componente (product.product) **obligatorio**.
    ● Cantidad.
    ● Precio de venta.
Este precio de venta se ha de recoger de la ficha del componente **cuando cambie** el producto en la línea.

Además queremos agregar estos componentes en la ficha del producto por lo que agregaremos:
    ● Relación de este nuevo modelo con la plantilla de producto.
    ● Así mismo un check para indicar que se trata de un pack y en caso afirmativo mostrar en una nueva pestaña del formulario **agregar** estas líneas desde una **tabla directamente**.

2 ● Vamos a crear nuevos campo en la plantilla de producto.
    ● Poder seleccionar métodos de cálculo del precio, Suma componentes, Precio normal. Por defecto que sea el precio normal.
Luego haremos un método para calcular el precio del pack Si el método es suma de componentes será el sumatorio de la cantidad por el precio de cada línea de componente, **si es normal**, se **habilita al usuario la edición del precio** ¿De qué **campos** puede **depender** el cálculo del precio?
Hay que agregar estos campos en la pestaña de los componentes.

3 ● **Herencia del modelo de líneas de venta** para modificar el método **que se ejecuta al cambiar** el producto en la línea de venta.
Para modificar la descripción hemos de agregar a lo que ya viene lo siguiente:
<texto_original>
-- Components --
<nombre_componente> - <cantidad>
<nombre_componente_2> - <cantidad>

4 ● Vamos a heredar la vista de búsqueda de los productos para agregar un filtro de solo packs. Recordamos que hemos creado un nuevo modelo para los componentes así pues para ver la agrupación de estos por cada pack hemos de crear un punto de menu una vista lista y una búsqueda para poder visualizar las líneas de cada componente y poder agruparlas por pack. Vamos hacer que no se puedan ni crear ni editar componentes desde ese listado.
Agregamos el punto de menú debajo de Variantes de producto en el módulo Ventas.

5 ● Creamos un nuevo informe con un [diseño similar a este](https://drive.google.com/file/d/17oyYtPVPsBHnU3qa_79XglwF7FB_b0WG/view).

------------------------------------------------------------------------------------------------------------------

### Consejos

● Podemos utilizar un compute para calcular el precio de venta.

● Buscar por el código original el lugar de creación del modelo sale.order.line para ver como se llama el método que se ejecuta al cambiar el producto.

● Puedo traducir string escritos en python “-- Components --” con la librería _ [ejemplo](https://github.com/odoo/odoo/blob/f882512fea32784944ecccdd921c96576869b2e6/addons/account/wizard/account_move_reversal.py#L115). Este valor saldra para traducirlo con el poedit.

● Para evitar la creación o edición de registros en una vista lista podemos utilizar [create y edit](https://github.com/odoo/odoo/blob/96564dd64bdbd426ae87444fd75a822074a37fc0/addons/account/views/account_move_views.xml#L140).

------------------------------------------------------------------------------------------------------------------

### Recursos / Solución

● [Nuevo modelo](https://github.com/QubiQ/sistema-doq/blob/master/practica_final_2/models/product_pack_line.py#L6), [campos en producto](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_2/models/product_template.py#L7), [vista](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_2/views/product_template.xml#L11).

● [Calculando precio producto](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_2/models/product_template.py#L27),[vista](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_2/views/product_template.xml#L19).

● [Onchange descripción](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_2/models/sale_order.py#L8).

● [Vistas](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_2/views/product_pack_line.xml#L6).

● [Diseño](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_2/views/report_product_template.xml#L4),[informe](https://github.com/QubiQ/sistema-doq/blob/4de257c1348b32afc309593936b6a58ee40ae4bd/practica_final_2/views/reports.xml#L5).

------------------------------------------------------------------------------------------------------------------

> [!IMPORTANT]
> Es determinante cumplir con todos los criterios de aceptación.

> [!WARNING]
> Recuerda subir el PR y mencionar a Jesús Ramoneda para que haga las correcciones concretas.

> [!CAUTION]
> Corrige los fallos.
