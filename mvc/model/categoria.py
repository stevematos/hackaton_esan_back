from mvc import db,ma


class Categoria(db.Model):
    __tablename__ = 'categoria'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))


class CategoriaSchema(ma.ModelSchema):

    class Meta:
        model = Categoria
        fields = (
            'nombre',
        )


categoria_schema = CategoriaSchema(many=True)