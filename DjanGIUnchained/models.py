from django.db import models
# JuanSalmeronM si que ha currado, ha arrancado la cachimba


class PieceType(models.Model):
    """
        Model that represents the MIGHTY POWER OF THE types of the pieces
    """
    type_id = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=80, blank=False)

    def to_dict(self):
        return {'type_id': self.type_id, 'name': self.name}

    def __str__(self):
        return '{} {}'.format(self.type_id, self.name)


class Pieces(models.Model):
    """
        Model that represents the MIGHTY POWER OF THE pieces
    """
    name = models.CharField(max_length=255, blank=False)
    manufacturer = models.CharField(max_length=255, blank=False)
    type_id = models.ForeignKey(PieceType, on_delete=models.CASCADE, related_name='pieces', null=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'manufacturer': self.manufacturer, 'type_id': self.type_id}

    def __str__(self):
        return '{} {}'.format(self.id, self.name)


class Role(models.Model):
    """
        Model that represents the MIGHTY POWER OF THE roles
    """
    name = models.CharField(max_length=50, primary_key=True)
    description = models.CharField(max_length=255)
    admin = models.BooleanField(null=False)

    def to_dict(self):
        return {'name': self.name, 'description': self.description, 'admin': self.admin}

    def __str__(self):
        return '{} {}'.format(self.name, self.admin)


class Permission(models.Model):
    """
            Model that represents the MIGHTY POWER OF THE permissions
    """
    class Meta:
        unique_together = (('screen', 'roleName'),)
    screen = models.CharField(max_length=50, blank=False)
    roleName = models.ForeignKey(Role, max_length=50, on_delete=models.CASCADE,
                                 related_name='permissions')
    access = models.BooleanField(null=False)
    modification = models.BooleanField(null=False)

    def to_dict(self):
        return {'id': self.id, 'screen': self.screen, 'roleName': self.roleName, 'access': self.access,
                'modification': self.modification}

    def __str__(self):
        return '{} {}'.format(self.roleName, self.screen)


class User(models.Model):
    """
            Model that represents the MIGHTY POWER OF THE users
    """
    name = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50, blank=False)
    roleName = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='links', null=False)

    def to_dict(self):
        return {'name': self.name, 'password': self.password, 'roleName': self.roleName}

    def __str__(self):
        return '{} {} {}'.format(self.name, self.password, self.roleName)
