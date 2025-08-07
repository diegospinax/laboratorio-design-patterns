async function listarComentarios() {
  const res = await fetch(API_BASE + ENDPOINTS.read_all);
  const data = await res.json();
  const lista = document.getElementById("listaComentarios");
  lista.innerHTML = "";
  data.forEach((c) => {
    const item = document.createElement("li");
    item.textContent = `ID: ${c.id} - ${c.usuario_email} - ${c.texto} (${c.calificacion})`;
    lista.appendChild(item);
  });
}

async function listarProductos() {
  const resP = await fetch(API_BASE + ENDPOINTSPRODUCTO.read_all);
  const dataPro = await resP.json();
  const listaP = document.getElementById("listaProductos");
  listaP.innerHTML = "";
  dataPro.forEach((e) => {
    const itemP = document.createElement("li");
    itemP.textContent = `ID: ${e.id} - ${e.nombre} - ${e.descripcion} - ${e.precio} - ${e.categoria}`;
    listaP.appendChild(itemP);
  });
}
document.addEventListener("DOMContentLoaded", () => {
  const formComentario = document.getElementById("formComentario")
  if(formComentario){
      formComentario.addEventListener("submit", async function (e) {
        e.preventDefault();
        const body = {
          texto: document.getElementById("texto").value,
          usuario_email: document.getElementById("email").value,
          calificacion: parseInt(document.getElementById("calificacion").value),
        };
        await fetch(API_BASE + ENDPOINTS.create, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(body),
        });
        alert("Comentario creado.");
        listarComentarios();
        mostrarSeccion("lista");
      });
    }

    const formProductElement = document.getElementById("formProducto");
  if(formProductElement){
      formProductElement.addEventListener("submit", async function (e) {
        e.preventDefault();

        const data = {
          nombre: document.getElementById("nombre").value,
          descripcion: document.getElementById("descripcion").value,
          precio: Number(document.getElementById("precio").value),
          categoria: document.getElementById("categoria").value,
        };

        await fetch(API_BASE + ENDPOINTSPRODUCTO.create, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(data),
        });
        
        alert("Producto creado.");
        listarProductos() ;
        mostrarSeccion("listaPro");
      });

    } 
});



async function buscarComentario() {
  const id = document.getElementById("idBuscar").value;
  const res = await fetch(API_BASE + ENDPOINTS.read_one.replace("{id}", id));
  if (res.ok) {
    const data = await res.json();
    document.getElementById("textoAccion").value = data.texto;
    document.getElementById("emailAccion").value = data.usuario_email;
    document.getElementById("calificacionAccion").value = data.calificacion;
    mostrarSeccion("acciones");
    alert("Comentario cargado para edición.");
  } else {
    alert("Comentario no encontrado.");
  }
}

async function actualizarComentario() {
  const id = document.getElementById("idBuscar").value;
  const body = {
    texto: document.getElementById("textoAccion").value,
    usuario_email: document.getElementById("emailAccion").value,
    calificacion: parseInt(document.getElementById("calificacionAccion").value),
  };
  const res = await fetch(API_BASE + ENDPOINTS.update.replace("{id}", id), {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  const result = await res.json();
  alert(result.mensaje || "Actualizado");
  listarComentarios();
  mostrarSeccion("lista");
}

async function eliminarComentario() {
  const id = document.getElementById("idBuscar").value;
  const res = await fetch(API_BASE + ENDPOINTS.delete.replace("{id}", id), {
    method: "DELETE",
  });
  const result = await res.json();
  alert(result.mensaje || "Eliminado");
  listarComentarios();
  mostrarSeccion("lista");
}

async function buscarProducto() {
  const searchProductElement = document.getElementById("productIdInput").value;

  const response = await fetch(API_BASE + ENDPOINTSPRODUCTO.read_one.replace("{id}", searchProductElement));

  if (response.ok) {
    const data = await response.json();
    document.getElementById("nombreAccion").value = data.nombre;
    document.getElementById("descripcionAccion").value = data.descripcion;
    document.getElementById("precioAccion").value = data.precio;
    document.getElementById("categoriaAccion").value = data.categoria;
    mostrarSeccion("accionesPro");
    alert("Producto con posibilidad de editar");
  } else {
    alert("Producto no encontrado.");
  }
}

  async function actualizarProducto() {
  const inputElement = document.getElementById("productIdInput").value;
  const data = {
      nombre: document.getElementById("nombreAccion").value,
      descripcion: document.getElementById("descripcionAccion").value,
      precio: Number(document.getElementById("precioAccion").value),
      categoria: document.getElementById("categoriaAccion").value,
  };
  const res = await fetch(API_BASE + ENDPOINTSPRODUCTO.update.replace("{id}", inputElement), {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  const result = await res.json();
  alert(result.mensaje || "Actualizado");
  listarProductos();
  mostrarSeccion("listaPro");
}

async function eliminarProducto() {
  const deleteProduct = document.getElementById("productIdInput").value;
  const res = await fetch(API_BASE + ENDPOINTSPRODUCTO.delete.replace("{id}", deleteProduct), {
    method: "DELETE",
  });
  const results = await res.json();
  alert(results.mensaje || "Eliminado");
  listarProductos();
  mostrarSeccion("listaPro");
}

function mostrarSeccion(id) {
  const sectionList = document.querySelectorAll(".seccion");
  sectionList.forEach((seccion) => (seccion.style.display = "none"));
  document.getElementById(id).style.display = "block";
}

listarProductos();
listarComentarios();
mostrarSeccion("crear");
