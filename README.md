Grupo de Investigación en Informática y Telecomunicaciones i2T
Universidad Icesi
Cali, Colombia

DESCRIPCIÓN:

Esta aplicación web permite controlar un USRP (GNURadio) usando Django y Node.js. El código fuente está en /remote y en /nodeserver, que corresponden al módulo de Django y al servidor Node.js respectivamente.


REQUERIMIENTOS:

Django: https://www.djangoproject.com/
Node.js: http://nodejs.org/


INSTRUCCIONES:

1. En /nodeserver/server.js vaya a la última línea y ponga el puerto UDP por el que va a escuchar al USRP, dentro de socket.bind(PUERTO_USRP). Debe poner un bloque UDP Sink en el USRP.

2. En /remote/views.py, busque las variables usrp_ip_address y ponga la dirección IP del USRP. Debe poner un bloque XML RPC Server en el USRP.

3. En /remote/templates/remote/index.html, busque las siguientes líneas de código y modifíquelas según su configuración:
	
	Dirección IP del servidor Node.js
		<script src="http://localhost:1337/socket.io/socket.io.js"></script>
		var serverSocketIPAddress = "http://localhost:1337";
	
	Dirección IP del servidor Django
		var serverIPAddress = "http://localhost:8000";
	
4. Ejecute 'python manage.py runserver' y node 'nodeserver/server.js'

5. Visite http://localhost:8000/remote/