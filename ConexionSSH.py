# Librerías necesarias
import xml_msg as fields
import paramiko
import time

# Conexion para manipulación de archivos
def connect_sftp():

    # Secure Data, this will not be avaliable in repository
    transport = paramiko.Transport(("", 22))
    transport.connect(username="", password="")
    sftp = paramiko.SFTPClient.from_transport(transport)
    return sftp


sftp = connect_sftp()
doc = "/home/opi4qa/testClient/LogMensaje.xml"

# Guardando evidencia en archivo separado
def save_evidencia(file, sftp):
    with sftp.open(file, "r") as f:
        z = f.readlines()
        with open("C:/Users/rguerra/desktop/Evidencia.txt", "a") as evidencia:
            for line in z:
                evidencia.write(str(line))
            evidencia.close()
        with open("C:/Users/rguerra/desktop/Campos.xml", "w+") as evidencia:
            for line in z:
                evidencia.write(str(line))
            evidencia.close()
    f.close
    print("lista evidencia")

# Ejecutando transacción el cual llama a guardar su evidencia
def transaccion(msg):

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Secure Data
    ssh_client.connect('', 22, '', '')

    entrada, salida, error = ssh_client.exec_command('./opi-switch/start.sh')

    entrada, salida, error = ssh_client.exec_command('cd testClient \n'
                                                     f'./tc-acq.sh {msg} | tee LogMensaje.xml')

    x = salida.readlines()
    for i in range(len(x)):
        print(x[i])

    save_evidencia(doc, sftp)

    ssh_client.close()
