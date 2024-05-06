from django.urls import path
from .views import mostrarIndex, mostrarLogin, inicioSesion, cierreSesion, mostrarProductos, mostrarProducto, mostrarCarrito, agregarAlCarrito, cambiarCantidad, sacarDelCarro, mostrarCrearCuenta, registrarUsuario, sumarStock, restarStock, mostrarCrearProducto, crearUnProducto, pagandoCarrito, mostrarPedidos, mostrarConsultas, enviarConsulta

urlpatterns=[

    ###No cuenta
    path('',mostrarIndex,name="mostrarIndex"),
    path('login/',mostrarLogin,name="mostrarLogin"),
    path('crear-cuenta/',mostrarCrearCuenta,name="mostrarCrearCuenta"),
    path('consultas/',mostrarConsultas,name="mostrarConsultas"),
    path('crear-producto/',mostrarCrearProducto,name="mostrarCrearProducto"),
    path('productos/<id_cate>',mostrarProductos,name="mostrarProductos"),
    path('pedidos/',mostrarPedidos,name="mostrarPedidos"),
    path('producto/<id_prod>',mostrarProducto,name="mostrarProducto"),
    path('carrito',mostrarCarrito,name="mostrarCarrito"),
    path('inicioSesion/',inicioSesion, name="inicioSesion"),
    path('cierreSesion/',cierreSesion,name="cierreSesion"),
    path('cambiarCantidad/<cod_detalle>',cambiarCantidad,name="cambiarCantidad"),
    path('sacarDelCarro/<cod_detalle>',sacarDelCarro,name="sacarDelCarro"),
    path('agregarAlCarrito/',agregarAlCarrito,name="agregarAlCarrito"),
    path('registrarUsuario/',registrarUsuario,name="registrarUsuario"),
    path('sumarStock/<cod_prod>',sumarStock,name="sumarStock"),
    path('restarStock/<cod_prod>',restarStock,name="restarStock"),
    path('pagandoCarrito/<id_venta>',pagandoCarrito,name="pagandoCarrito"),
    path('crearUnProducto/',crearUnProducto,name="crearUnProducto"),
    path('enviarConsulta/',enviarConsulta,name="enviarConsulta"),
]