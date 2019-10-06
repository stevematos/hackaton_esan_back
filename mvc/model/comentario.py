from mvc import db,ma
from marshmallow import fields

# from mvc.model.proyecto import ProyectoSchema



class Comentario(db.Model):
    __tablename__ = 'comentario'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    puntaje = db.Column(db.Float)
    detalle = db.Column(db.String(100))
    id_proyecto = db.Column(db.Integer,db.ForeignKey("proyecto.id"))


    # proyecto = db.relationship("Proyecto", back_populates="comentario")


class ComentarioSchema(ma.ModelSchema):

    # proyecto = fields.Nested(ProyectoSchema)

    class Meta:
        model = Comentario
        fields = (
            'puntaje',
            'detalle'
        )


comentario_schema = ComentarioSchema(many=True)