#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import subprocess as sp

#I want the ability to change the backup location
#backupLocation="/backups"


#Endless loop
while (1<2):
  vms = []
  vmList = "virsh list --all"

  #run virsh list -all to list VM options
  output = sp.getoutput(vmList)
  #print (output)

  #Split up the VM list output
  s_list = output.split(" ")

  i=0
  for x in s_list:
    #Filter out lines from the options
    if(len(x)> 3) and ('run' not in x) and ('off' not in x) and ('shut' not in x) and ('Name' not in x) and ('State' not in x) and ('--' not in x):
      vms.append(x)
      print(str(i) + ") " + x + " ")
      i=i+1

  print ("exit# Type exit to exit the program ")
  vmChoice = input("Enter your choice (number for VM):")

  if(vmChoice == "exit"):
    exit()
  if(vmChoice == ""):
    vmChoice=999
  if(int(vmChoice) < len(vms)):
    #Backup the selected VM
    output = sp.getoutput("virsh backup-begin " + vms[int(vmChoice)])
    print ()
    #print("virsh backup-begin " + vms[int(vmChoice)] + " --target " + backupLocation)
    #exit()
    #print ("Check if complete with virsh domjobinfo " + vms[int(vmChoice)] + " --completed")
    print ()

    #Endless loop
    while (1<2):
      #Check status and print output
      output = sp.getoutput("clear;virsh  domjobinfo " + vms[int(vmChoice)])
      print (output)
      if("None" in output):
        print ("Backup Complete")
        print ()
        break
      time.sleep(5)
    #If completed then show status of complete
    output = sp.getoutput("clear;virsh  domjobinfo " + vms[int(vmChoice)] + " --completed")
    print (output)
  else:
    output = sp.getoutput("clear")
    print (output)
    print ("Selection out of range")
    print ()


exit()
