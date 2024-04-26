from django.urls import path
from .views import mostrarIndex, mostrarLogin, inicioSesion, cierreSesion, mostrarProductos, mostrarProducto, mostrarCarrito, agregarAlCarrito, cambiarCantidad, sacarDelCarro, mostrarCrearCuenta

urlpatterns=[

    ###No cuenta
    path('',mostrarIndex,name="mostrarIndex"),
    path('login/',mostrarLogin,name="mostrarLogin"),
    path('crear-cuenta/',mostrarCrearCuenta,name="mostrarCrearCuenta"),
    path('productos/<id_cate>',mostrarProductos,name="mostrarProductos"),
    path('producto/<id_prod>',mostrarProducto,name="mostrarProducto"),
    path('carrito',mostrarCarrito,name="mostrarCarrito"),
    path('inicioSesion/',inicioSesion, name="inicioSesion"),
    path('cierreSesion/',cierreSesion,name="cierreSesion"),
    path('cambiarCantidad/<cod_detalle>',cambiarCantidad,name="cambiarCantidad"),
    path('sacarDelCarro/<cod_detalle>',sacarDelCarro,name="sacarDelCarro"),
    path('agregarAlCarrito/',agregarAlCarrito,name="agregarAlCarrito"),
]