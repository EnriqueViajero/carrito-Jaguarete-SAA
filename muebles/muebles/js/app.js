//Variables

const carrito = document.querySelector('#carrito');
const listaproductos = document.querySelector('#lista-cursos');
const contenedorCarrito = document.querySelector('#lista-carrito tbody');
const vaciarCarritoBtn = document.querySelector('#vaciar-carrito');
let articulosCarrito = [];

//Listeners
cargarEventListeners();

function cargarEventListeners() {
	// Dispara cuando se presiona "Agregar Carrito"
	listaproductos.addEventListener('click', agregarproducto);

	// Cuando se elimina un producto del carrito
	carrito.addEventListener('click', eliminarCurso);

	// Al Vaciar el carrito
	vaciarCarritoBtn.addEventListener('click', vaciarCarrito);
}

//Funciones
//Funcion que añade el producto al carrito
function agregarproducto(e) {
	e.preventDefault();
	// Delegation para agregar-carrito
	if (e.target.classList.contains('agregar-carrito')) {
		const producto = e.target.parentElement.parentElement;
		// Enviamos el producto seleccionado para tomar sus datos
		leerDatosproducto(producto);
	}
}

// Lee los datos del producto
function leerDatosproducto(producto) {
	const infoproducto = {
		imagen: producto.querySelector('img').src,
		titulo: producto.querySelector('h4').textContent,
		precio: producto.querySelector('.precio span').textContent,
		id: producto.querySelector('a').getAttribute('data-id'),
		cantidad: 1,
	};

	if (articulosCarrito.some((producto) => producto.id === infoproducto.id)) {
		const producto = articulosCarrito.map((producto) => {
			if (producto.id === infoproducto.id) {
				producto.cantidad++;
				return producto;
			} else {
				return producto;
			}
		});
		articulosCarrito = [...producto];
	} else {
		articulosCarrito = [...articulosCarrito, infoproducto];
	}

	console.log(articulosCarrito);

	// console.log(articulosCarrito)
	carritoHTML();
}

// Elimina el producto del carrito en el DOM
function eliminarproducto(e) {
	e.preventDefault();
	if (e.target.classList.contains('borrar-producto')) {
		// e.target.parentElement.parentElement.remove();
		const productoId = e.target.getAttribute('data-id');

		// Eliminar del arreglo del carrito
		articulosCarrito = articulosCarrito.filter((producto) => producto.id !== productoId);

		carritoHTML();
	}
}

// Muestra el producto seleccionado en el Carrito
function carritoHTML() {
	vaciarCarrito();

	articulosCarrito.forEach((producto) => {
		const row = document.createElement('tr');
		row.innerHTML = `
               <td>  
                    <img src="${producto.imagen}" width=100>
               </td>
               <td>${producto.titulo}</td>
               <td>${producto.precio}</td>
               <td>${producto.cantidad} </td>
               <td>
                    <a href="#" class="borrar-curso" data-id="${producto.id}">X</a>
               </td>
          `;
		contenedorCarrito.appendChild(row);
	});
}

/// Elimina los cursos del carrito en el DOM
function vaciarCarrito() {
	// forma lenta
	// contenedorCarrito.innerHTML = '';

	// forma rapida (recomendada)
	while (contenedorCarrito.firstChild) {
		contenedorCarrito.removeChild(contenedorCarrito.firstChild);
	}
}
