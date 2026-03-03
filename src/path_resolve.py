#devOps_CLI
#HANDLE:    _MUMINUL__ISLAM___



#CODE->
from pathlib import Path

#Resolve Path
class path_resolver():
    src_folder_path=Path(__file__)

    parent_folder_path=src_folder_path.parent.parent

    reports_file_path=parent_folder_path/'reports/reports.csv'

    logger_file_path=parent_folder_path/'reports/logger.log'

    config_file_path=parent_folder_path/'config.json'

    graph_image_path=parent_folder_path/'reports/report_graph.png'