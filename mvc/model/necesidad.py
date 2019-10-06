from mvc import db,ma


class Necesidad(db.Model):
    __tablename__ = 'necesidad'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    link_icon = db.Column(db.String(200))


class NecesidadSchema(ma.ModelSchema):

    class Meta:
        model = Necesidad
        fields = (
            'id',
            'nombre',
            'link_icon'
        )



necesidad_schema = NecesidadSchema(many=True)
# ejecutivo_schema = EjecutivoSchema(many=True)