from django.shortcuts import render
from django.shortcuts import render, redirect
from datetime import date, timedelta
from django.contrib import messages
import requests
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
# Create your views here.


###Funciones de API
def obtener_categorias():
    url_servicio = 'http://127.0.0.1:8000/api/categorias/'
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None

def obtener_productos_cate(id_cate):
    url_servicio = f'http://localhost:8000/api/productos/?categoria={id_cate}'
    print(url_servicio)
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None 
    
def obtener_producto(id_prod):
    url_servicio = f'http://localhost:8000/api/producto/?cod_prod={id_prod}'
    print(url_servicio)
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None 

def obtener_stock(cod_prod):
    url_servicio = f'http://localhost:8000/api/stock-producto/?producto={cod_prod}'
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None 

def obtener_usuario(correo):
    url_servicio = f'http://localhost:8000/api/usuario/{correo}'
    print(url_servicio)
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None 

def obtener_venta(usuario, estado):
    url_servicio = f'http://127.0.0.1:8000/api/filtrar-carrito/?usuario={usuario}&estado={estado}'
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        
        return respuesta.json()
    else:
        return None  

def obtener_detallesVenta(venta):
    url_servicio = f'http://127.0.0.1:8000/api/detalles-carrito/?venta={venta}'
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None
    
def obtener_detallesId(id):
    url_servicio = f'http://127.0.0.1:8000/api/detalles-id-carrito/?id_detalle={id}'
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None
    
def buscar_DetallesCarrito(venta, cod_prod):
    url_servicio = f'http://127.0.0.1:8000/api/detalles-buscar-carrito/?venta={venta}&producto={cod_prod}'
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None

def modificar_total_carrito(id_venta, nuevo_total):
    url_servicio = f'http://127.0.0.1:8000/api/venta/{id_venta}/'
    data = {'total': nuevo_total}  # Datos a enviar en la solicitud

    # Realizar la solicitud POST para modificar el total del carrito
    respuesta = requests.patch(url_servicio, data=data)

    if respuesta.status_code == 200:
        print('El total del carrito se modificó correctamente.')
    else:
        print('Hubo un error al modificar el total del carrito.')

def modificar_estado_carrito(id_venta, estado):
    url_servicio = f'http://127.0.0.1:8000/api/venta/{id_venta}/'
    data = {'estado': estado}  # Datos a enviar en la solicitud

    # Realizar la solicitud POST para modificar el total del carrito
    respuesta = requests.patch(url_servicio, data=data)

    if respuesta.status_code == 200:
        print('El estado del carrito se modificó correctamente.')
    else:
        print('Hubo un error al modificar el estado del carrito.')




def crearDetalle(cantidad, subtotal, venta, producto):
    data = {
    'cantidad': cantidad,
    'subtotal': subtotal,
    'venta': venta,  
    'producto': producto  
    }

    url_servicio = 'http://127.0.0.1:8000/api/crear-detalle/'

    respuesta = requests.post(url_servicio, data=data)

    if respuesta.status_code == 201:
        print('Detalle creado correctamente.')
    else:
        print('Error al crear el detalle.')

def crearVenta(fecha_venta, estado, fecha_entrega, total, carrito, usuario):

    data = {
    'fecha_venta': fecha_venta,
    'estado': estado,
    'fecha_entrega': fecha_entrega,  
    'total': total,
    'carrito' : carrito,
    'usuario' : usuario
    }

    url_servicio = 'http://127.0.0.1:8000/api/crear-venta/'

    respuesta = requests.post(url_servicio, data=data)

    if respuesta.status_code == 201:
        print('Venta creada correctamente.')
    else:
        print('Error al crear la venta.')

def modificar_cantidad_detalle(id_detalle, nueva_cantidad):
    url_servicio = f'http://127.0.0.1:8000/api/detalle/{id_detalle}/'
    data = {'cantidad': nueva_cantidad}  # Datos a enviar en la solicitud

    # Realizar la solicitud PUT para modificar la cantidad del detalle
    respuesta = requests.patch(url_servicio, data=data)

    if respuesta.status_code == 200:
        print('La cantidad del detalle se modificó correctamente.')
    else:
        print('Hubo un error al modificar la cantidad del detalle.')

def modificar_subtotal_detalle(id_detalle, nuevo_subtotal):
    url_servicio = f'http://127.0.0.1:8000/api/detalle/{id_detalle}/'
    data = {'subtotal': nuevo_subtotal}  # Datos a enviar en la solicitud

    # Realizar la solicitud PUT para modificar el subtotal del detalle
    respuesta = requests.patch(url_servicio, data=data)

    if respuesta.status_code == 200:
        print('El subtotal del detalle se modificó correctamente.')
    else:
        print('Hubo un error al modificar el subtotal del detalle.')

def eliminar_detalle(id_detalle):
    url_servicio = f'http://127.0.0.1:8000/api/delete-detalle/?id_detalle={id_detalle}'
    respuesta = requests.delete(url_servicio)
    if respuesta.status_code == 204:
        print('Detalle eliminado correctamente.')
    else:
        print('Error al eliminar el detalle.')

###Paginas

def mostrarIndex(request):

    categorias = obtener_categorias()

    rol = request.session.get('rol',0)

    contexto = {"categorias" : categorias, "rol": rol}

    return render(request, 'core/index.html',contexto)

def mostrarLogin(request):

    categorias = obtener_categorias()

    rol = request.session.get('rol',0)

    contexto = {"categorias" : categorias, "rol": rol}

    return render(request, 'core/login.html',contexto)

def mostrarProductos(request, id_cate):

    categorias = obtener_categorias()

    productos = obtener_productos_cate(id_cate)

    rol = request.session.get('rol',0)

    contexto = {"categorias" : categorias, "rol": rol, "productos": productos}

    return render(request, 'core/productos.html',contexto)


def mostrarProducto(request, id_prod):

    categorias = obtener_categorias()

    producto = obtener_producto(id_prod)

    stock = obtener_stock(id_prod)
    

    rol = request.session.get('rol',0)

    contexto = {"categorias" : categorias, "rol": rol, "producto": producto, "stock" : stock}

    return render(request, 'core/producto.html',contexto)

def mostrarCarrito(request):
    categorias = obtener_categorias()

    rol = request.session.get('rol',0)

    username = request.session.get('username')
    usuario1 = obtener_usuario(username)

    carrito = obtener_venta(usuario1['id_usuario'], 'ACTIVO')
    

    if carrito:
        carrito = carrito[0]
        detalles = obtener_detallesVenta(carrito['id_venta'])
        totalV = 0
        for i in detalles:
            producto = i['producto']
            stock = obtener_stock(producto['cod_prod'])
            if stock['stock_total'] <= 0:
                
                
                return redirect('mostrarCarrito')
                    
            totalV += i['subtotal']
        modificar_total_carrito(carrito['id_venta'], totalV)
        
        contexto = {"categorias" : categorias, "carrito" : detalles, "venta" : carrito}
        if not detalles:
            modificar_estado_carrito(carrito['id_venta'],'INACTIVO')
            
    else:
        contexto = {"categorias" : categorias, "rol": rol}


    
    return render(request, 'core/carrito.html',contexto)



def inicioSesion(request):
    if request.method == 'POST':
        correoI = request.POST['username']
        claveI = request.POST['password']

        try:
            user1 = User.objects.get(username=correoI)
        except User.DoesNotExist:
            return redirect('mostrarLogin')
        
        pass_valida = check_password(claveI, user1.password)
        if not pass_valida:
            return redirect('mostrarLogin')

        # Obtener usuario desde la API
        usuario_api = obtener_usuario(correoI)
        if usuario_api:
            request.session['username'] = user1.username
            request.session['rol'] = usuario_api['rol'] 
            user = authenticate(username=correoI, password=claveI)
            if user is not None:
                login(request, user)
                return redirect('mostrarIndex')
        
    return redirect('mostrarIni_sesion')
    
def cierreSesion(request):
    logout(request)
    return redirect('mostrarIndex')


def sacarDelCarro(request, cod_detalle):
    
    detalle = obtener_detallesId(cod_detalle)
    detalle = detalle[0]

    eliminar_detalle(cod_detalle)
        
    return redirect('mostrarCarrito')
   

def cambiarCantidad(request, cod_detalle):

    detalle = obtener_detallesId(cod_detalle)
    detalle = detalle[0]
    cant = int(request.POST['nueva_cantidad_{}'.format(cod_detalle)])
    producto = detalle['producto']

    stockC = producto['stock']
    cantidadC = int(cant)

    if cantidadC >= 0:
        if cantidadC <= stockC:
            modificar_cantidad_detalle(cod_detalle, cantidadC)
            modificar_subtotal_detalle(cod_detalle, producto['precio'] * cantidadC )
            return redirect('mostrarCarrito')
        else:
            messages.warning(request,'La cantidad no puede exceder el stock disponible')
            return redirect('mostrarCarrito')
    else:
        messages.warning(request,'La cantidad no puede ser menor a 1')
        return redirect('mostrarCarrito')

def agregarAlCarrito(request):
    cod_produc = request.POST['codigo']
    productoC = obtener_producto(cod_produc)
    productoC = productoC[0]

    username = request.session.get('username')
    usuarioC = obtener_usuario(username)
        
    fecha_hoy = date.today()
    entrega = timedelta(999)
    fecha_e = fecha_hoy + entrega

    carrito = obtener_venta(usuarioC['id_usuario'],'ACTIVO')
    

    if carrito:
        carrito = carrito[0]
        detalle1 = buscar_DetallesCarrito(carrito['id_venta'], cod_produc)
        if detalle1:
            detalle1 = detalle1[0]
            modificar_cantidad_detalle(detalle1['id_detalle'], detalle1['cantidad']+1)
            modificar_subtotal_detalle(detalle1['id_detalle'], detalle1['subtotal'] + productoC['precio'])
                
        else:
            detalle1 = crearDetalle(1, productoC['precio'], carrito['id_venta'], cod_produc)
            idventa = carrito['id_venta']

    else:
        
        carrito = crearVenta(fecha_hoy, 'ACTIVO', fecha_e, productoC['precio'], 1, usuarioC['id_usuario'])
        venta = obtener_venta(usuarioC['id_usuario'], 'ACTIVO')
        venta = venta[0]
        idventa = venta['id_venta']
        crearDetalle(1, productoC['precio'], idventa, cod_produc)

    
    return redirect('mostrarCarrito')