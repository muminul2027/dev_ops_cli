#devOps_CLI
#HANDLE:    _MUMINUL__ISLAM___


#CODE->

from src.path_resolve import path_resolver

import logging


class logger():
    #Get File

    logger_path=path_resolver.logger_file_path

    #Config the Global Logger
    logging.basicConfig(
        filename=logger_path,
        level=logging.ERROR,
        format='%(asctime)s-%(levelname)s-%(message)s'
    )

    #Create Logger
    create_logger=logging.getLogger("devops")
