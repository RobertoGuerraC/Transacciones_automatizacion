from lxml import etree

# x = "C:/Users/rguerra/desktop/MensajedePrueba.xml"
# Cambiar el comercio de un mensaje


def cambiar_comercio(file, id_comercio, sftp):
    with sftp.open(file, "r") as f:

        et = etree.parse(f)
        root = et.getroot()

        field_42 = root.find("./field[@id='42']")
        # Value ser el ID del comercio dado de alta, por lo cual será una variable externa, scanntech.id_comercio
        field_42.attrib["value"] = '00000' + str(id_comercio)
        f.close()

    with sftp.open(file, "w") as f:
        et.write(f)
        f.close()
    return print(True)

# campos para la anulación.
def mensaje_210(file):

    with open(file, "r") as f:
        y = f.read()
        # index_send = y.rindex('<send>')
        index_send = y.rindex('<receive>')
        try:
            # range_send = y.rindex('<log')
            range_send = y.rindex('</receive>')
        except:
            range_send = len(y)
        s = ""
        for i in range(index_send, (range_send+len('</receive>'))):
            s += y[i]

        f.close()

    with open(file, "w") as f:
        f.write(s)
        f.close()

    with open(file, "r") as f:
        et = etree.parse(f)
        root = et.getroot()
        field_4 = root.find("./isomsg/field[@id='4']").attrib['value']
        field_11 = root.find("./isomsg/field[@id='11']").attrib['value']
        field_37 = root.find("./isomsg/field[@id='37']").attrib['value']
        field_38 = root.find("./isomsg/field[@id='38']").attrib['value']
        f.close()

        return field_11, field_37, field_38, field_4

# Se cambian los campos de la anulación.
def campos_anulacion(file, sftp, field11, field37, field38, field4):
    with sftp.open(file, "r") as f:

        et = etree.parse(f)
        root = et.getroot()
        field_4 = root.find("./field[@id='4']")
        field_38 = root.find("./field[@id='38']")
        field_37 = root.find("./field[@id='37']")
        field_11 = root.find("./field[@id='11']")
        field_4.attrib["value"] = str(field4)
        field_38.attrib["value"] = str(field38)
        field_37.attrib["value"] = str(field37)
        field_11.attrib["value"] = str(field11)
        f.close()

    with sftp.open(file, "w") as f:
        et.write(f)
        f.close()
    return True

def campos_reverso(file, sftp, field11, field4):
    with sftp.open(file, "r") as f:

        et = etree.parse(f)
        root = et.getroot()
        field_11 = root.find("./field[@id='11']")
        field_4 = root.find("./field[@id='4']")
        field_11.attrib["value"] = str(field11)
        field_4.attrib["value"] = str(field4)
        f.close()

    with sftp.open(file, "w") as f:
        et.write(f)
        f.close()
    return True

def cambiar_11(file, sftp):
    with sftp.open(file, "r") as f:

        et = etree.parse(f)
        root = et.getroot()
        field_11 = root.find("./field[@id='11']")
        x = int(field_11.attrib["value"]) + 1
        if len(field_11.attrib["value"]) == 3:
            field_11.attrib["value"] = "000" + str(x)
            print(field_11.attrib["value"])
        elif len(field_11.attrib["value"]) == 4:
            field_11.attrib["value"]= "00" + str(x)

        f.close()

    with sftp.open(file, "w") as f:
       et.write(f)
       f.close()
    return True

def cuotas(file, sftp, cuotas):
    with sftp.open(file, "r") as f:

        et = etree.parse(f)
        root = et.getroot()
        field_11 = root.find("./field[@id='48']")
        if len(str(cuotas)) == 2:
            field_11.attrib["value"] = '0' + str(cuotas)
        else:
            field_11.attrib["value"] = '00' + str(cuotas)
        f.close()

    with sftp.open(file, "w") as f:
        et.write(f)
        f.close()
    return True

def cambiar_importe(file, sftp, importe):
    with sftp.open(file, "r") as f:

        et = etree.parse(f)
        root = et.getroot()
        field_11 = root.find("./field[@id='4']")
        field_11.attrib["value"] = '0' + str(importe)
        print(field_11.attrib["value"])
        while len(str(field_11.attrib["value"])) != 10:
            field_11.attrib["value"] = '0' + str(field_11.attrib["value"])
        print(field_11.attrib["value"])
        field_11.attrib["value"] = str(field_11.attrib["value"]) + '00'
        print(field_11.attrib["value"])
        f.close()
    with sftp.open(file, "w") as f:
        et.write(f)
        f.close()
    return True

def file(id):
    switcher = {
        1: 'ManualCompra.xml',
        2: 'ManualAnulacion.xml',
        3: 'ManualDevolucion.xml',
        4: 'ManualReverso.xml',
        5: 'BandaCompra.xml',
        6: 'BandaAnulacion.xml',
        7: 'BandaDevolucion.xml',
        8: 'BandaReverso.xml',
        9: 'ChipCompra.xml',
        10: 'ChipAnulación.xml',
        11: 'ChipDevolución.xml',
        12: 'ChipReverso.xml',
        13: 'ContactlessCompra.xml',
        14: 'ContactlessAnulación.xml',
        15: 'ContactlessDevolución.xml',
        16: 'ContactlessReverso.xml',
        17: 'ManualXAnulacionDevolucion.xml',
        18: 'BandaXAnulaciónDevolución.xml',
        19: 'ChipXAnulaciónDevolución.xml',
        20: 'ContactlessXAnulaciónDevolución.xml'
    }
    return '/home/opi4qa/testClient/' + switcher.get(id)

def tipo_transaccion(id):
    switcher = {
        1: 'ManualCompra.xml',
        2: 'ManualAnulacion.xml',
        3: 'ManualDevolucion.xml',
        4: 'ManualReverso.xml',
        5: 'BandaCompra.xml',
        6: 'BandaAnulacion.xml',
        7: 'BandaDevolucion.xml',
        8: 'BandaReverso.xml',
        9: 'ChipCompra.xml',
        10: 'ChipAnulación.xml',
        11: 'ChipDevolución.xml',
        12: 'ChipReverso.xml',
        13: 'ContactlessCompra.xml',
        14: 'ContactlessAnulación.xml',
        15: 'ContactlessDevolución.xml',
        16: 'ContactlessReverso.xml',
        17: 'ManualXAnulacionDevolucion.xml',
        18: 'BandaXAnulaciónDevolución.xml',
        19: 'ChipXAnulaciónDevolución.xml',
        20: 'ContactlessXAnulaciónDevolución.xml'
    }
    return switcher.get(id)