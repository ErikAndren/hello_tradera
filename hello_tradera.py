import zeep
import logging

logging.getLogger('zeep').setLevel(logging.ERROR)

publicServiceUrl = 'https://api.tradera.com/v3/PublicService.asmx'

appId = 'REPLACE ME WITH TRADERA ID'
appKey = 'REPLACE ME WITH TRADERA KEY'

wsdl = 'https://api.tradera.com/v3/PublicService.asmx?WSDL'

client = zeep.Client(wsdl=wsdl)

authHeader = {
    'AuthenticationHeader' : {
        'AppId' : appId,
        'AppKey' : appKey
        }
    }

result = client.service.GetOfficalTime(_soapheaders = authHeader)

print(result)
