#devOps_CLI
#HANDLE:    _MUMINUL__ISLAM___


#CODE->

from src.path_resolve import path_resolver

import pandas as pd
import matplotlib.pyplot as plt

class analyzer_plot():

    #Get the CSV
    csv_report_file=path_resolver.reports_file_path

    #Read the CSV
    dataframe_table=pd.read_csv(csv_report_file)

    #Plot the Graph
    dataframe_table.plot(kind='scatter',x="Time",y="Latency")

    #Title On Graph
    plt.title("devOps_CLI")
    plt.xlabel("Time")
    plt.ylabel("Latency")

    #Save Graph
    plt.savefig(path_resolver.graph_image_path)