from mvc import db,ma

from mvc.model.dimensiones import EventoSchema
from marshmallow import fields


class OportunidadCupos(db.Model):
    __tablename__ = 'oportunidad_cupos'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer)
    monto_final = db.Column(db.Float)
    idetapa = db.Column(db.Integer, db.ForeignKey("etapa.id"))
    idcliente= db.Column(db.Integer, db.ForeignKey("cliente.id"))
    idcupo = db.Column(db.Integer, db.ForeignKey("cupo.id"))
    idejecutivo = db.Column(db.Integer, db.ForeignKey("ejecutivo.id"))
    idfecha = db.Column(db.Integer, db.ForeignKey("fecha.id"))
    idevento = db.Column(db.Integer, db.ForeignKey("evento.id"))
    activo = db.Column(db.Boolean)

    # relaciones
    evento = db.relationship("Evento")
    ejecutivo = db.relationship("Ejecutivo")
    cupo = db.relationship("Cupo")
    etapa = db.relationship("Etapa")


class OportunidadCuposSchema(ma.ModelSchema):

    evento = fields.Nested(EventoSchema)

    class Meta:
        model = OportunidadCupos
        fields = (
            'cantidad',
            'monto_final',
            'evento'
        )


oportunidad_cupos_schema = OportunidadCuposSchema(many=True)
