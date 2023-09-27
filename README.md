# MISW_EXP_2_GESTION_EMPRESARIAL

Microservicio `Gestión empresarial` que se utiliza para simular el envío de solicitudes HTTP aleatorias hacia el microservicio `Detector intrusos`

El script genera datos aleatorios para representar solicitudes HTTP, como el método HTTP (POST, GET, PUT, DELETE), la URL de destino, el cliente (navegador web), el sistema operativo del cliente, la dirección IP y la fecha y hora de acceso. Luego, estos datos aleatorios se convierten en formato JSON y se imprimen en la consola.

 ```json
{
     "http_method": "post",
     "url_endpoint": "/ofertas",
     "client": "safari",
     "operating_system": "macos",
     "ip_address": "127.5.87.255",
     "access_datetime": "2020-04-15T12:19:50"
}
```

Estas solicitudes se enviarían a una URL específica en "http://127.0.0.1:5000/api/detector-intrusos" utilizando el método POST con los datos JSON como carga útil; a continuación se ilustra en un diagrama para mayor comprensión de la arquitectura

![image](https://github.com/MISO-Arquitectura/MISW_EXP_2_GESTION_EMPRESARIAL/assets/54864717/8c03b81e-743f-49ac-8613-423ae4263e84)
