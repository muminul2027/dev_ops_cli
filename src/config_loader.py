#devOps_CLI
#HANDLE:    _MUMINUL__ISLAM___



#CODE->
import json
from src.path_resolve import path_resolver

class config_load():
    #Config File Path
    path_to_config=path_resolver.config_file_path

    #Open Config File and Retrive API LINK
    with open(path_to_config,'r') as file:
        #JSON TO Python
        config_dict=json.load(file)

    api_link=config_dict["site_01"]
