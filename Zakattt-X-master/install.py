# Tool Name :- Zakat-X
# Author :- Ongar Developer
# Date :- 19/1/2021

import os
import sys
from time import sleep
from modules.logo import *
from modules.system import *

class tool:
  @classmethod
  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input("\033[1;33m Do you want to install Zakat-X [Y/n]> \033[00m")
      if inp=="y" or inp=="Y":
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          #require root permission
          if os.path.exists(system.conf_dir+"/Zakat-X"):
            pass
          else:
            os.system(system.sudo+" mkdir "+system.conf_dir+"/Zakat-X")
          os.system(system.sudo+" cp -r modules core Zakat-X.py "+system.conf_dir+"/Zakat-X")
          os.system(system.sudo+" cp -r core/Zakat-X "+system.bin)
          os.system(system.sudo+" cp -r core/zakatx "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/Zakat-X")
          os.system(system.sudo+" chmod +x "+system.bin+"/zakatx")
          os.system("cd .. && "+system.sudo+" rm -rf Zakat-X")
          if os.path.exists(system.bin+"/Zakat-X") and os.path.exists(system.conf_dir+"/Zakat-X"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m ##> \033[00m")
            break
        else:
          if os.path.exists(system.conf_dir+"/Zakat-X"):
            pass
          else:
            os.system("mkdir "+system.conf_dir+"/Zakat-X")
          os.system("cp -r modules core Tool-X.py "+system.conf_dir+"/Zakat-X")
          os.system("cp -r core/Zakat-X "+system.bin)
          os.system("cp -r core/zakatx "+system.bin)
          os.system("chmod +x "+system.bin+"/Zakat-X")
          os.system("chmod +x "+system.bin+"/zakatx")
          os.system("cd .. && rm -rf Zakat-X")
          if os.path.exists(system.bin+"/Zakat-X") and os.path.exists(system.conf_dir+"/Zakat-X"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m ##> \033[00m")
            break
      else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
