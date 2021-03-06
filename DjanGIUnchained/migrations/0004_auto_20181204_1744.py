# Generated by Django 2.1.3 on 2018-12-04 17:44

from django.db import migrations


def fake_sql_script(apps, schema_editor):
    """
    This method is a fake sql script that introduces the data into the database.
    it is a f*cking mess due to making all this shit by hand, but at least, if the database collapses
    we have a recovery script
    :param apps: DjanGIUnchained
    :param schema_editor: IDK what this shit is
    :return: void
    """
    piece_type = apps.get_model("DjanGIUnchained", "PieceType")
    permission = apps.get_model("DjanGIUnchained", "Permission")
    pieces = apps.get_model("DjanGIUnchained", "pieces")
    role = apps.get_model("DjanGIUnchained", "Role")
    user = apps.get_model("DjanGIUnchained", "User")
    admin = role(name='administrador', description='administrador', admin=1)
    usr = role(name='usuario', description='usuario', admin=0)
    inv = role(name='invitado', description='invitado', admin=0)
    admin.save()
    usr.save()
    inv.save()
    user(name='user', password='user', roleName=usr).save()
    user(name='inv', password='inv', roleName=inv).save()
    user(name='admin', password='admin', roleName=admin).save()
    permission(screen='LOGIN', roleName=admin, access=1, modification=1).save()
    permission(screen='MATERIAS', roleName=admin, access=1, modification=1).save()
    permission(screen='LIBROS', roleName=admin, access=1, modification=1).save()
    permission(screen='LOGIN', roleName=usr, access=1, modification=1).save()
    permission(screen='MATERIAS', roleName=usr, access=1, modification=0).save()
    permission(screen='LIBROS', roleName=usr, access=1, modification=0).save()
    permission(screen='LOGIN', roleName=inv, access=1, modification=1).save()
    permission(screen='MATERIAS', roleName=inv, access=0, modification=0).save()
    permission(screen='LIBROS', roleName=inv, access=0, modification=0).save()
    chapa = piece_type(type_id='A', name='Chapa')
    motor = piece_type(type_id='B', name='Motor')
    iluminacion = piece_type(type_id='C', name='Iluminación')
    sensores = piece_type(type_id='D', name='Sensores')
    cristales = piece_type(type_id='E', name='Cristales')
    pintura = piece_type(type_id='F', name='Pintura')
    chapa.save()
    motor.save()
    iluminacion.save()
    sensores.save()
    cristales.save()
    pintura.save()
    pieces(name='PARAGOLPES DELANTERO NEGRO-LISO A IMPRIMAR', manufacturer='MAZDA', type_id=chapa).save()
    pieces(name='PARAGOLPES TRASERO-IMPRIMADO', manufacturer='MAZDA', type_id=chapa).save()
    pieces(name='REJILLA NEGRA', manufacturer='MAZDA', type_id=chapa).save()
    pieces(name='ALETA DELANTERA DCH CON AUJERO PARA PILOTO Cx3 16', manufacturer='MAZDA', type_id=chapa).save()
    pieces(name='ALETA DELANTERA IZQ CON AUJERO PARA PILOTO Cx3 16', manufacturer='MAZDA', type_id=chapa).save()
    pieces(name='Bombillas luz delantera', manufacturer='RENAULT', type_id=iluminacion).save()
    pieces(name='Bombillas luz trasera', manufacturer='RENAULT', type_id=iluminacion).save()
    pieces(name='Bombillas señalización delantera', manufacturer='RENAULT', type_id=iluminacion).save()
    pieces(name='Bombillas señalización trasera', manufacturer='RENAULT', type_id=iluminacion).save()
    pieces(name='Estuches de bombillas', manufacturer='RENAULT', type_id=iluminacion).save()
    pieces(name='Iluminación LED', manufacturer='RENAULT', type_id=iluminacion).save()
    pieces(name='Bombillas interior', manufacturer='RENAULT', type_id=iluminacion).save()
    pieces(name='Bombillas Xenon', manufacturer='RENAULT', type_id=iluminacion).save()
    pieces(name='Kits de distribución', manufacturer='FORD', type_id=motor).save()
    pieces(name='Correas', manufacturer='FORD', type_id=motor).save()
    pieces(name='Poleas', manufacturer='FORD', type_id=motor).save()
    pieces(name='Kits', manufacturer='FORD', type_id=motor).save()
    pieces(name='Válvulas', manufacturer='FORD', type_id=motor).save()
    pieces(name='Herramienta Específica', manufacturer='FORD', type_id=motor).save()
    pieces(name='Turbocompresores', manufacturer='FORD', type_id=motor).save()
    pieces(name='Sensores electrónicos y medidores de flujo',
           manufacturer='FORD', type_id=motor).save()
    pieces(name='Cable de acelerador y starter', manufacturer='FORD', type_id=motor).save()


class Migration(migrations.Migration):

    dependencies = [
        ('DjanGIUnchained', '0003_auto_20181204_1648'),
    ]

    operations = [
        migrations.RunPython(fake_sql_script)
    ]
