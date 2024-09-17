"""
Background:
 A very small company called **KommatiPara** that deals with bitcoin 
 trading has two separate datasets dealing with clients that they want 
 to collate to starting interfacing more with their clients. 
 One dataset contains information about the clients and the 
 other one contains information about their financial details.

 The company now needs a dataset containing the emails of 
 the clients from the United Kingdom and the Netherlands and 
 some of their financial details to starting reaching out to 
 them for a new marketing push.
"""

from pyspark.sql import SparkSession
from utils_functions import write_csv_to_location, filter_data


spark = SparkSession.builder.appName("JoinDatasets").getOrCreate()

df1 = spark.read.option('header', True).csv('codc-interviews/version1/dataset_one.csv')
df2 = spark.read.option('header', True).csv('codc-interviews/version1/dataset_two.csv')

df_joined = df1.join(df2, on="id", how="inner")

df_drop=df_joined.drop("cc_n")\
                   .drop("first_name")\
                   .drop("last_name")

df_filtered = filter_data(df_drop)
df_filtered.show()

output_folder = "codc-interviews/version1/client_data"  
filename = "dataset_three.csv"  
write_csv_to_location(df_filtered,output_folder,filename)
