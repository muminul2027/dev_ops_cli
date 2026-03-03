#devOps_CLI
#HANDLE:    _MUMINUL__ISLAM___


#CODE->
from src.checker_module import check
from src.config_loader import config_load
from src.logging_module import logger
from src.path_resolve import path_resolver

import csv
from datetime import datetime

#Resolve Path
csv_file_path=path_resolver.reports_file_path

checking_link=check()

reponse_column=checking_link.response_code
latency_column=checking_link.latency


#Get Some Time
time_now=datetime.now().time().strftime("%H:%M")

class reporter():
    #Write to CSV File
    if not csv_file_path.exists():
        if(reponse_column==200):
            with open(csv_file_path,"w",newline="") as csv_file:
                writer=csv.writer(csv_file)

                #Data
                csv_header=["Time","API","Response","Latency"]
                csv_line=time_now,config_load.api_link, reponse_column , latency_column

                #write now
                writer.writerow(csv_header)
                writer.writerow(csv_line)

        #Else Log the Fail Ones
        else:
            logger.create_logger.error("Error Happened")

    else:
        if(reponse_column==200):
            with open(csv_file_path,"a",newline="") as csv_file:
                writer=csv.writer(csv_file)
                csv_line=time_now,config_load.api_link,reponse_column,latency_column
                
                #write data only
                writer.writerow(csv_line)
        else:
            #Log Failed Entry
            logger.create_logger.error("Error Happened")


    
