# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - Jie Lin
# Python 3

#coding=utf-8
"""
@version: 1.0
@author: Jie Lin
@Mail: jlin246@emory.edu
@file: solution.py
@time: 09/21/2018 9:29 PM
@purpose: for practicing API
@code environment: ubuntu 18.01
"""

import requests

# check if distros.py is running
def checkConnection():
	try:
		requests.get('http://localhost:8888');
		return True;
	except Exception:
		return False;


# a function gets user input and check if it matches the server ends data
def getUsrInput():
	name = input("Please enter a name of system that you want to request: ")
	type(name)
	parameter = {'oid':name}
	response = requests.get('http://localhost:8888',params = parameter);

	return response;

def printAvgTime(response_data,response):
	total_exec_time = 0.0;
	numberOfData=0;
	distribution_id = "";

	#get total_exec_time
	for value in response_data.values():
		total_exec_time=total_exec_time+float(value.get("ExecTime"));
		numberOfData=numberOfData + 1;
		distribution_id = value.get("Name");

	#calculate the avg_exec_time
	avg_exec_time = total_exec_time/numberOfData;
	#store result as a dictionary
	result = dict([("distribution_id",distribution_id),("avg_exec_time",avg_exec_time)])

	command = "curl "+response.url;
	print();
	print(command);
	print(result);


#this is the main method
if __name__ == '__main__':

	if(checkConnection()):
		response = getUsrInput();
		response_data = response.json();
		while(len(response_data)==0):
			print("\nYour input does not match the data in distros.json.\n"+
				"Please enter again or Ctrl+C to abort the program\n");
			response = getUsrInput();
			response_data = response.json();

		printAvgTime(response_data,response);

		
	else:
		print("Please check distros.py is running");