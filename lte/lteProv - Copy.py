import requests
import const
from log import Logger

logger = Logger.getLogger('lte', 'logs/lte')


class Lteprov:
    def lteProv(data, ref):
        logger.info("LTE : %s" % ref + " - " + str(data))

        if retTaxPrice is not None:                                        
            retmsgadjustment = CreateSO.Create_SO (data ['msisdnNo'],(retTaxPrice),"1") 
            loggerocsApi.info(ref + ": " + "retmsgAdjustment: %s" % retmsgadjustment)
            return {'result': 'error','dataOcs': 'ADJUSTMENT ' + retmsgadjustment['resultHeader']['resultDesc'],'dataPcrf' : 'PCRF error provisioned'}                                                                         
        else:
            return {'result': 'error','dataOcs': 'TaxPrice null against productId','dataPcrf' : 'PCRF error provisioned'}                               
        #resmsg= {"status": "success","description": "Connection success"}
        #return resmsg
        
class CreateSO:

    def Create_SO:
    
        url = "http://172.25.16.218:8080/ClarityServiceManagement-war/ServiceManagementAPIService?wsdl"
        
        # structured XML
        payload = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://webservices/clarity/api/servicemanagement">
                       <soapenv:Header/>
                       <soapenv:Body>
                          <ser:getVersion/>
                       </soapenv:Body>
                    </soapenv:Envelope>"""                  
        try:
            # headers
            headers = {'Content-Type': 'text/xml; charset=utf-8'}
            # POST request
            response = requests.request("POST", url, headers=headers, data=payload)
            
            loggeroffer.info("Response Code: %s" % response.status_code)
            resmsg = response.text
            print(resmsg)
            loggeroffer.info("Response : %s" % resmsg)      
            return resmsg
            
        except Exception as e: 
            print("Exception : %s" % e)
            loggeroffer.info("Exception : %s" % e)     
