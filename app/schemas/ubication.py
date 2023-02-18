



def definition_ubicationSchema(ma):
    class UbicationSchema(ma.Schema):
        class Meta:
            fields=('id','lat','lng')

    return [UbicationSchema(), UbicationSchema(many=True)]

