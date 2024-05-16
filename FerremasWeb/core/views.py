from django.shortcuts import render, redirect, reverse
from datetime import date, timedelta
from django.contrib import messages
import requests
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
import json

# Create your views here.


###Funciones de API
def obtener_categorias():
    url_servicio = 'http://127.0.0.1:8000/api/categorias/'
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None

def obtener_roles():
    url_servicio = 'http://127.0.0.1:8000/api/roles/'
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None

def obtener_consultas():
    url_servicio = 'http://127.0.0.1:8000/api/consultas/'
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None

def obtener_productos_cate(id_cate):
    url_servicio = f'http://127.0.0.1:8000/api/productos/?categoria={id_cate}'
    print(url_servicio)
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None 
    
def obtener_producto(id_prod):
    url_servicio = f'http://127.0.0.1:8000/api/producto/?cod_prod={id_prod}'
    print(url_servicio)
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None 

def obtener_stock(cod_prod):
    url_servicio = f'http://127.0.0.1:8000/api/stock-producto/?producto={cod_prod}'
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None 

def obtener_usuario(correo):
    url_servicio = f'http://127.0.0.1:8000/api/usuarioC/{correo}'
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None 

def obtener_usuarioRut(rut):
    url_servicio = f'http://127.0.0.1:8000/api/usuarioR/{rut}'
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
    
def buscarVentas_estado(estado):
    url_servicio = f'http://127.0.0.1:8000/api/ventas-estado/?estado={estado}'
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

def modificar_carrito_carrito(id_venta, carrito):
    url_servicio = f'http://127.0.0.1:8000/api/venta/{id_venta}/'
    data = {'carrito': carrito}  # Datos a enviar en la solicitud

    # Realizar la solicitud POST para modificar el total del carrito
    respuesta = requests.patch(url_servicio, data=data)

    if respuesta.status_code == 200:
        print('La venta paso a ser o no carrito')
    else:
        print('Hubo un problema en carrito_carrito')

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

def crearTransaccion(tipo_transaccion, cantidad, producto, fecha):
    data = {
    'tipo_transaccion': tipo_transaccion, 
    'cantidad': cantidad, 
    'fecha_transaccion' : fecha,
    'producto': producto
    }

    url_servicio = 'http://127.0.0.1:8000/api/crear-transaccion/'

    respuesta = requests.post(url_servicio, data=data)

    if respuesta.status_code == 201:
        print('Transaccion creada correctamente.')
    else:
        print('Error al crear la transaccion.')

def crearConsulta(nombre, asunto, mensaje):
    data = {
    'nombre_consultante': nombre, 
    'asunto_consulta': asunto, 
    'mensaje_consulta' : mensaje
    }
    print(data)
    url_servicio = 'http://127.0.0.1:8000/api/crear-consulta/'

    respuesta = requests.post(url_servicio, data=data)

    if respuesta.status_code == 201:
        print('Consulta creada correctamente.')
    else:
        print('Error al crear la consulta.')

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

import requests

def crearProducto(nombre, descripcion, precio, marca, imagen, unidad, categoria):
    data = {
        'nombre_prod': nombre,
        'descripcion': descripcion,
        'precio': precio,
        'marca': marca,
        'unidad_medida': unidad,
        'categoria': categoria
    }

    files = {
        'foto_prod': imagen
    }

    url_servicio = 'http://127.0.0.1:8000/api/crear-producto/'
    
    respuesta = requests.post(url_servicio, data=data, files=files)

    if respuesta.status_code == 201:
        print('Producto creado correctamente.')
    else:
        print('Error al crear el producto.')



def crearUsuario(rut, activo, dvrut, nombre, apellido, telefono, correo, clave, direccion, respuest, rol, pregunta):

    data = {
    'rut': rut,
    'activo': activo,
    'dvrut': dvrut,  
    'nombre': nombre,
    'apellido' : apellido,
    'telefono' : telefono,
    'correo' : correo,
    'clave' : clave,
    'direccion' : direccion,
    'respuesta' : respuest,
    'rol' : rol,
    'pregunta' : pregunta,
    }
    
    print(data)
    url_servicio = 'http://127.0.0.1:8000/api/crear-usuario/'

    respuesta = requests.post(url_servicio, data=data)

    print(respuesta)

    if respuesta.status_code == 201:
        print('Usuario creado correctamente.')
    else:
        print('Error al crear el usuario.')



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

    valorDelDolar = darValorDolar()
    
    
    rol = request.session.get('rol',0)

    contexto = {"categorias" : categorias, "rol": rol, "productos": productos, "dolar" : valorDelDolar}

    return render(request, 'core/productos.html',contexto)


def darValorDolar():

    cambio = valorDolar()
    cambio = cambio['Series']
    cambio = cambio['Obs']
    cambio = cambio[-1]
    valorDelDolar = cambio['value']
    valorDelDolar = float(valorDelDolar)

    return valorDelDolar

def mostrarProducto(request, id_prod):

    categorias = obtener_categorias()

    producto = obtener_producto(id_prod)

    stock = obtener_stock(id_prod)
    
    valorDelDolar = darValorDolar()

    rol = request.session.get('rol',0)

    contexto = {"categorias" : categorias, "rol": rol, "producto": producto, "stock" : stock, "dolar" : valorDelDolar}

    return render(request, 'core/producto.html',contexto)

def mostrarStock(request):

    categorias = obtener_categorias()

    rol = request.session.get('rol',0)

    contexto = {"categorias" : categorias, "rol": rol}

    return render(request, 'core/stock.html',contexto)

def mostrarPedidos(request):

    categorias = obtener_categorias()

    pedidos = buscarVentas_estado('PEDIDO SOLICITADO')

    rol = request.session.get('rol',0)

    contexto = {"categorias" : categorias, "rol": rol, 'pedidos' : pedidos}

    return render(request, 'core/pedidos.html',contexto)

def mostrarConsultas(request):

    categorias = obtener_categorias()

    rol = request.session.get('rol',0)

    if(rol == 2):
        consultas = obtener_consultas()
        contexto = {"categorias" : categorias, "rol": rol, "consultas": consultas}
    else:
         contexto = {"categorias" : categorias, "rol": rol}
    

    return render(request, 'core/consultas.html',contexto)

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
                eliminar_detalle(i['id_detalle'])
                
                return redirect('mostrarCarrito')
                    
            totalV += i['subtotal']
        modificar_total_carrito(carrito['id_venta'], totalV)
        valorDelDolar = darValorDolar()
        contexto = {"categorias" : categorias, "carrito" : detalles, "venta" : carrito, "dolar" : valorDelDolar}
        if not detalles:
            modificar_estado_carrito(carrito['id_venta'],'INACTIVO')
            
    else:
        contexto = {"categorias" : categorias, "rol": rol}


    
    return render(request, 'core/carrito.html',contexto)

def mostrarCrearCuenta(request):
    categorias = obtener_categorias()

    roles = obtener_roles()

    rol = request.session.get('rol',0)

    contexto = {"categorias" : categorias, "rol": rol, "roles": roles}

    return render(request, 'core/crearCuenta.html',contexto)

def mostrarCrearProducto(request):
    categorias = obtener_categorias()

    roles = obtener_roles()

    rol = request.session.get('rol',0)

    contexto = {"categorias" : categorias, "rol": rol, "roles": roles}

    return render(request, 'core/crearProducto.html',contexto)

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
        
    return redirect('mostrarLogin')
    
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

    stockC = obtener_stock(producto['cod_prod'])
    stockC = stockC['stock_total']
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
        
        carrito = crearVenta(fecha_hoy, 'ACTIVO', fecha_e, productoC['precio'], True, usuarioC['id_usuario'])
        venta = obtener_venta(usuarioC['id_usuario'], 'ACTIVO')
        venta = venta[0]
        idventa = venta['id_venta']
        crearDetalle(1, productoC['precio'], idventa, cod_produc)

    
    return redirect('mostrarCarrito')


def registrarUsuario(request):
    rutU = request.POST['rut']
    dvrutU = request.POST['dvrut']
    nombreU = request.POST['nombre']
    apellidoU = request.POST['apellido']
    telefonoU = request.POST['telefono']
    direccionU = request.POST['direccion']
    correoU = request.POST['correo']
    claveU = request.POST['clave']
    rolU = request.POST['rol']
    respuestaU = 'a'
    preguntaUid = 1
    usuario1 = False
    usuario2 = False

    if(rolU == '1'):
        rolU = 1

    usuarioPorCorreo = obtener_usuario(correoU)
    if usuarioPorCorreo:
        print('El correo '+correoU+' esta en uso')
        usuario1 = True

    
    usuarioPorRut = obtener_usuarioRut(rutU)
    if usuarioPorRut:
        print('El rut '+rutU+' esta en uso')
        usuario2 = True
    

    if usuario1 or usuario2:
        print(request,'Ya existe una cuenta con el correo/rut ingresado')
        return redirect('mostrarCrearCuenta')
    else:
        
        crearUsuario(rutU, True, dvrutU, nombreU, apellidoU, telefonoU, correoU, claveU, direccionU, respuestaU, rolU, preguntaUid)
        
        user = User.objects.create_user(username = correoU, email = correoU, password = claveU )
        user.is_staff = False
        user.is_active = True
        user.save()

        return redirect('mostrarLogin')

def sumarStock(request, cod_prod):

    tipo_transaccion = "Agregar"
    cantidad = request.POST['agregar']
    producto = cod_prod
    fecha_hoy = date.today()

    url_con_parametro = reverse('mostrarProducto', kwargs={'id_prod': producto})

    crearTransaccion(tipo_transaccion, cantidad, producto, fecha_hoy)
    return redirect(url_con_parametro)


def restarStock(request, cod_prod):

    tipo_transaccion = "Retirar"
    cantidad = request.POST['quitar']
    producto = cod_prod
    fecha_hoy = date.today()

    url_con_parametro = reverse('mostrarProducto', kwargs={'id_prod': producto})

    crearTransaccion(tipo_transaccion, cantidad, producto, fecha_hoy)
    return redirect(url_con_parametro)


def crearUnProducto(request):
    nombre = request.POST['nombre_prod']
    descripcion = request.POST['descripcion']
    precio = request.POST['precio']
    marca = request.POST['marca']
    imagen = request.FILES['foto_prod']
    unidad = request.POST['unidad_medida']
    categoria = request.POST['categoria']
    url_con_parametro = reverse('mostrarProductos', kwargs={'id_cate': categoria})

    crearProducto(nombre, descripcion, precio, marca, imagen, unidad, categoria)

    return redirect(url_con_parametro)


def pagandoCarrito(request, id_venta):

    modificar_estado_carrito(id_venta, 'PEDIDO SOLICITADO')

    return redirect('mostrarIndex')

def enviarConsulta(request):
    asunto = request.POST['asunto']
    mensaje = request.POST['mensaje']

    username = request.session.get('username')
    usuario = obtener_usuario(username)
    nombre = usuario['nombre']
    apellido = usuario['apellido']
    nombre_completo = nombre + " " + apellido

    crearConsulta(nombre_completo, asunto, mensaje)

    return redirect('mostrarConsultas')

def pagarConWebpay(request):

    orden_compra = "Ferre12121"
    sesion = "Ferres55552"
    monto = request.POST['total_webpay']

    response_dict = pagarWebpay(orden_compra, sesion, monto)

    if response_dict:
        url = response_dict['url']
        token = response_dict['token']
        print(f'{url}/?token={token}')
        return redirect(f'{url}/{token}')
    else:
        return redirect('mostrarIndex')

def buscarStock(request):
    if request.method == 'POST':
        codigo_producto = request.POST.get('codigo_producto')
        stock = obtener_stock(codigo_producto)
        return render(request, 'core/stock.html', {'stock': stock})
    else:
        return render(request, 'core/stock.html')
    
def valorDolar():
    
    url_servicio = 'https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user=abelx3678@gmail.com&pass=iMb2aUmdez.bYua&firstdate=2024-05-09&lastdate=&timeseries=F073.TCO.PRE.Z.D&function=GetSeries'
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None 
    
def pagarWebpay(orden_compra, sesion_id, monto):
    headers = {
        "Tbk-Api-Key-Id": "597055555532",
        "Tbk-Api-Key-Secret": "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C",
        "Content-Type": "application/json"
    }

    data = {
        "buy_order": orden_compra,
        "session_id": sesion_id,
        "amount": monto,
        "return_url": "http://127.0.0.1:8001/"
    }
    print(data)
    url_servicio = 'https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions'
    respuesta = requests.post(url_servicio, data=json.dumps(data), headers=headers)

    response_dict = {
        'token': respuesta.json()['token'],
        'url': respuesta.json()['url']
    }
    return response_dict




    
