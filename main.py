#PROJECT_NAME:  devOps_CLI
#PROJECT_TYPE:  PERSONAL/PORTFOLIO

#OWNER/AUTHOR:  MUMINUL ISLAM
#HANDLE:    _MUMINUL_ISLAM___

#LICENSE:   PROPRIETARY
#PURPOSE:   JOB_APPLICATION_EVALUATION

#########################################################
##ADDITIONAL_INFORMATION

##PRODUCT_GOAL:    PRODUCTION_MVP_FOR_PORTFOLIO
##ALLOCATED_TIME:    2 [DAYS]

##STATUS:    ONGOING

##GitHub:
##########################################################

#CODE->
from src.report_module import reporter
from src.cli_module import parser_function
from src.analyzer import analyzer_plot

#Call Reporter
reporter_obj=reporter()
analyzer_plot_obj=analyzer_plot()

#Make CLI Work
if(parser_function()):
    print(reporter_obj.csv_line)
else:
    print("CLI Disabled Without Option --output")