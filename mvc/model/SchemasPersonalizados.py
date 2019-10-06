from mvc import ma

class CuposEventoEjecutivoSchema(ma.ModelSchema):

    class Meta:
        fields = (
            'cantidad_cupos',
            'cupo',
            'peso',
            'nombre_evento',
            'nombre_ejecutivo'
        )

cupos_evento_ejecutivos_schema = CuposEventoEjecutivoSchema(many=True)
