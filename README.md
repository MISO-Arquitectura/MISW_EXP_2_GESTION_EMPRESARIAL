# MISW_EXP_2_GESTION_EMPRESARIAL

Microservicio `Gestión empresarial` que se utiliza para simular el envío de solicitudes HTTP aleatorias hacia el microservicio `Detector intrusos`

El script genera datos aleatorios para representar solicitudes HTTP, como el método HTTP (POST, GET, PUT, DELETE), la URL de destino, el cliente (navegador web), el sistema operativo del cliente, la dirección IP y la fecha y hora de acceso. Luego, estos datos aleatorios se convierten en formato JSON y se enviarían a una URL específica en `http://127.0.0.1:5000/api/detector-intrusos` utilizando el método POST con los datos JSON como carga útil.

A continuación se ilustra el JSON y el diagrama para mayor comprensión de la arquitectura

 ```json
{
	"req": {
		"http_method": "get",
		"url_endpoint": "/ofertas",
		"user_agent": "safari",
		"operating_system": "macos",
		"ip_address": "127.5.87.255",
		"access_datetime": "2022-04-08T12:08:35"
	},
	"info": 1
}
```

![image](https://github.com/MISO-Arquitectura/MISW_EXP_2_GESTION_EMPRESARIAL/assets/54864717/4cff17c0-3098-4e1a-ae1a-8173fca9794a)


