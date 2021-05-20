AUTH = {

        "login": "6dd490faf9cb87a9862245da41170ff2",
        "seed": "2017-07-24T15:21:10-05:00",
        "nonce": "ZjgzYzNkNzI1MmEwNjRlNzlhZDViOGIyNmQxNjcxZTg=",
        "tranKey": "024h1llD"   
}





	
from datetime import datetime
from time import strftime
from ctypes import cdll

using P2P = PlacetoPay.Integrations.Library.CSharp.PlacetoPay;
Gateway gateway = new P2P(YOUR_LOGIN,
                      YOUR_TRANKEY,
                      new Uri("URL_INTEGRATION"),
                      Gateway.TP_SOAP or Gateway.TP_REST);

mydll = cdll.LoadLibrary()
def obtenerSeed():
	now=datetime.now().strftime("%Y-%m-%dT%H:%M")
	return(now+"-15:00")


seed=obtenerSeed()
print(seed)
