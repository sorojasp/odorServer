from app.server.server import Server

server=Server()
class UbicationSchema(server.getMarshmallowObject().Schema):
    class Meta:
        fields=('id','lat','lng')
