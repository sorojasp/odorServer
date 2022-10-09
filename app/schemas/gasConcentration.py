from app.server.server import Server



server=Server()
class GasConcentrationSchema(server.getMarshmallowObject().Schema):
    class Meta:
        fields=('id','NH3','CO2','CH4','H2S','SO2','temperature','humidity','dateTime','ubication_id','probe_mode')
