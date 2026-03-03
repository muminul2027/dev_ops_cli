#devOps_CLI
#HANDLE: _MUMINUL__ISLAM___



#CODE->
from src.config_loader import config_load

import requests

class check():
    #Get Link
    requests_obj=requests.get(config_load.api_link)

    #Get Response Code
    response_code=requests_obj.status_code
    #Get Latency
    latency=requests_obj.elapsed.total_seconds()

    #Call Ping
