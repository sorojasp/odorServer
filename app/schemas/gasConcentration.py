

def definition_GasConcentrationSchema(ma):
    class GasConcentrationSchema(ma.Schema):
        class Meta:
            fields=('id','NH3','CO2','CH4','H2S','SO2','temperature','humidity','dateTime','ubication_id','probe_mode')
    
    return [GasConcentrationSchema(), GasConcentrationSchema(many=True)]
