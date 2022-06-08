-------------------------------------- README de EntregableFinal----------------------------------------

- La Applicacion es un blog de literatura que permite a los usuarios: 
	-Crear / Buscar usuario
	-Crear / Buscar / Leer Textos
	-Cargar / Buscar Bibliotecas

-Inicio-
La Web nos presenta una pestaña de inicio que presenta una barra de navegacion. En aquella barra, del la- 
do izquierdo se muestran el logo del blog que redirecciona al inicio sin importar la pestaña en la que uno
se encuentre. A su vez se pueden ver tres botones del lado derecho que nos llevan a tres direcciones distin-
tas. La primera es de "usuarios, la segunda de "textos" y la tercera de "bibliotecas".

url del inicio:

/entregableFinal/

-Usuario- 
En la pestaña de usuario se nos presenta dos botones. Uno redirecciona a un formulario donde se crean usuarios
y el otro nos redirecciona a una pestaña donde se pueden buscar usuarios por nombre de usuario. Al introducir 
el nombre en la busqueda no presentan el nombre, el apellido, el nombre de usuario y el email de contacto. 

urls:

Menu principal de Usuario
/entregableFinal/usuario/

Pagina para crear usuario
/entregableFinal/crearUsuario/

Pagina para buscar usuario
/entregableFinal/busquedaUsuario/

Pagina con la lista de datos del usuario buscado
/entregableFinal/buscar/


-Textos- 

La pesataña de textos nos prsentan 3 cuentos los los cuales todos pueden ser presionados para ser redirecciona-
dos para leer en profundidad los cuentos. Al final de las pestañas se pueden ver tres botones. El primero redi-
recciona al usuario a una pestaña donde puede cargar libros/cuentos/textos. El segundo boton redirecciona a una
pestaña donde hay un buscador, que busca a partir del nombre de un libro. El resultado de esa busqueda muestra 
el titulo, una breve descripcion y el nombre del autor. Por ultimo el tercer boton redirecciona a una busqueda 
de google de "cuentos cortos".

urls:

Menu Principal de los textos
entregableFinal/ textos/ 

Cuento completo de Hansel y Gretel
entregableFinal/ hansel-gretel/

Cuento Completo del Gato con Botas
entregableFinal/ gato-con-botas/

Cuento Completo de los Tres Cerditos
entregableFinal/ tres-cerditos/ 

Pagina para Cargar/crear libros
entregableFinal/ crear_libro/ 

Pagina para buscar libros por nombre
entregableFinal/ busqueda_libro/ 

Pagina con lista de libros
entregableFinal/ buscar_libro/ 

-Bibliotecas-

La pestaña de bibliotecas muestra un buscador donde un puede encontrar la direccion, un link de la biblioteca,
una imagen, el nombre, etc. Por debajo del buscador y su respectivo "submit", se encuentra el boton de ver el 
listado completo de bibliotecas. Subsecuente a aquel boton se encuentra el boton de cargar biblioteca la cual
redirecciona al usuario a un formulario donde puede cargar los datos necesarios. Por ultimo, el boton de eli-
minar se encarga de eliminar una biblioteca a partir del nombre de la biblioteca (actualmente esta funcion no 
esta implementada).

urls:

Menu Principal de biblioteca
entregableFinal/ bibliotecas/

Pagina con lista completa de Bibliotecas
entregableFinal/ biblio_list/ 

Pagina para cargar bibliotecas
entregableFinal/ carga_biblio/

Pagina para buscar biliotecas
entregableFinal/ busca_biblio/ 




