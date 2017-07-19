"""
The python code to execute all files
"""

import os

for i in range(2002, 2015):
	os.system("cd "+str(i)+"01_"+"5min \n qsas algoproxy.sas \n qsas pca.sas \n qsas sample.sas \n cd .. \n")


	os.system("cd "+str(i)+"01_"+"5sec \n qsas algoproxy.sas \n qsas pca.sas \n qsas sample.sas \n cd .. \n")


	os.system("cd "+str(i)+"01_"+"15min \n qsas algoproxy.sas \n qsas pca.sas \n qsas sample.sas \n cd .. \n")

	
