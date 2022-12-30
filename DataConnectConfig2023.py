#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Emmanuel Cano - Senior Security Consulting Engineer @ Cisco Systems. (ecanogut@cisco.com)
Purpose: Basic consumption of the Open API calls for Identity Services Engine (ISE) 
to enable and configure the parameters for DataConnect Feature. 
This scripts assumes OpenAPI/ERS is enabled and ERS Admin account has been created
"""
import urllib3
import requests
import json
import pyfiglet
import time
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

clbanner = pyfiglet.figlet_format("ISE Webinars Monitoring, and Custom Reporting Part 2!!")
print(clbanner)

#Variables to be used in functions

CredentialsEnable='Basic ERS_Admin_Cred_Based64' #Password in Based64 format
ISENODE='ISE_IPAddress:443' #Depending on API Gateway configuration, you can use Primary Administration Node (PAN) IP address. 

#SVNFV2ViaW5hcjpDaXNjbzEyMw==
def enable_data_connect():
  #This function enables dataconnect feature
  #Available options for isEnabled are: True or False
  
    url = "https://" + ISENODE+ "/api/v1/mnt/data-connect/settings/status"
    payload = json.dumps({"isEnabled": True})
    
    headers = {
   'Accept': 'application/json',
   'Content-Type': 'application/json',
   'Authorization': CredentialsEnable
   }

    response = requests.request("PUT", url, headers=headers, data=payload, verify=False)
    if response.status_code == 200:
     print(response.text)
    else:
      print(response.status_code)
      print(response.text)
     
def set_password():
  #This function configures the password to be used for dataconnect
  #The password is used when configure the third party software to consume the logs 
  #Password must meet this criteria: 12 to 30 characters: (A-Z), (a-z), (0-9) -(#$%&*+,-.:;=?^_~)
  
    url = "https://" + ISENODE+ "/api/v1/mnt/data-connect/settings/password"
    payload = json.dumps({"password": "ISEWebinar02062023#"})  
    
    headers = {
   'Accept': 'application/json',
   'Content-Type': 'application/json',
   'Authorization': CredentialsEnable
   }

    response = requests.request("PUT", url, headers=headers, data=payload, verify=False)
    if response.status_code == 200:
     print(response.text)
    else:
      print(response.status_code)
      print(response.text)
      
    

def set_password_expiration():
  #This function configures the password expiration date in days
  #The valid range is from 1 to 3650 days. The default value is 90 days

    url = "https://" + ISENODE+ "/api/v1/mnt/data-connect/settings/password/expiry"
    payload = json.dumps({"passwordExpiresInDays": 370}) 
    
    headers = {
   'Accept': 'application/json',
   'Content-Type': 'application/json',
   'Authorization': CredentialsEnable
   }

    response = requests.request("PUT", url, headers=headers, data=payload, verify=False)
    if response.status_code == 200:
     print(response.text)
    else:
      print(response.status_code)
      print(response.text)
     
     
def check_status():
  #This function shows of the status of dataconnect

    url = "https://" + ISENODE+ "/api/v1/mnt/data-connect/details"
    headers = {
   'Accept': 'application/json',
   'Content-Type': 'application/json',
   'Authorization': CredentialsEnable
   }

    response = requests.request("GET", url, headers=headers, verify=False)
    if response.status_code == 200:
     print(response.text)
    else:
      print(response.status_code)
      print(response.text)
     
def check_password_status():
  #This function shows the details of the password including status and expiration date (In days)

    url = "https://" + ISENODE+ "/api/v1/mnt/data-connect/settings"
    headers = {
   'Accept': 'application/json',
   'Content-Type': 'application/json',
   'Authorization': CredentialsEnable
   }

    response = requests.request("GET", url, headers=headers, verify=False)
    if response.status_code == 200:
     print(response.text)
    else:
      print(response.status_code)
      print(response.text)


if __name__ == '__main__':
  

 time.sleep(1)
 print ("\n-------------------------------")
 print ("  Enabling DataConnect           ")
 print ("-------------------------------")
 enable_data_connect()
 
 time.sleep(1)
 print ("\n-------------------------------")
 print ("  Setting Password...            ")
 print ("-------------------------------")
 set_password()
 
 
 time.sleep(1)
 print ("\n-------------------------------")
 print ("  Setting Password Expiration in Days ")
 print ("-------------------------------")
 set_password_expiration()
 
 time.sleep(1)
 print ("\n-------------------------------")
 print ("  Checking Data Connect Status   ")
 print ("-------------------------------")
 check_status()
 
 time.sleep(1)
 
 print ("\n----------------------------------------")
 print ("  Checking Data Connect Password Status   ")
 print ("----------------------------------------")
 check_password_status()
 
 print ("\n----------------------------------------")
 print ("Dataconnect enabled and configured successfully")
 print ("----------------------------------------")
 print("\n")

