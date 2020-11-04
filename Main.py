import xml_msg as msg
import ConexionSSH as c
import random

# Establecemos la variable para el manejo de archivos en el OPI
sftp = c.connect_sftp()

doc = "/home/opi4qa/testClient/LogMensaje.xml"
fields = "C:/Users/rguerra/desktop/Campos.xml"


# Agregamos cuotas
msg.cuotas(msg.file(1), sftp, 3)

# Ejecutamos la compra
for i in range(5):

    # Cambiamos importe Random.
    importe = random.randrange(999)
    msg.cambiar_importe(msg.file(1), sftp, importe)

    # Ejecutar transaccion en OPI
    c.transaccion(msg.tipo_transaccion(1))

    # Cambios DE 11 por ejecución
    msg.cambiar_11(msg.file(1), sftp)

    # Buscamos campos para anular en Response
    campo11, campo37, campo38, campo4 = msg.mensaje_210(fields)
    msg.campos_anulacion(msg.file(2), sftp, campo11, campo37, campo38, campo4)

    # Ejecutar anulacion de la compra
    c.transaccion(msg.tipo_transaccion(2))

