#Log TF Out
#github.com/smcclennon/LTFO
ver='4.0.0'
proj='LTFO'

print('Importing requirements...')
try:
    # Attempt to import requirements
    import time,string,os,socket,getpass,urllib.request,json
    from ctypes import windll
    from random import randint
    from pathlib import Path
except:
    # Display error message on failure
    print('Error: one or more libraries could not be imported!')
    print('Visit github.com/smcclennon/LTFO for support\n\nPress enter to exit...')
    input()
    exit()

windll.kernel32.SetConsoleTitleW(f'{proj} - v {ver}') #Set console window title

# Run a specific command
def cmd(x):
    os.system(str(x))

# Pause the program for a specified amount of time
def sleep(x):
    time.sleep(x)

# Print the logo
def asciiRaw():
    print(f'''██╗  ████████╗███████╗ ██████╗
██║  ╚══██╔══╝██╔════╝██╔═══██╗
██║     ██║   █████╗  ██║   ██║  v{ver}
██║     ██║   ██╔══╝  ██║   ██║
███████╗██║   ██║     ╚██████╔╝
╚══════╝╚═╝   ╚═╝      ╚═════╝''')

# Clear the display
def display():
    cmd('cls')
    asciiRaw()

def confirmChoice():
    while True:
        choice = input('Confirm? [Y/n] ').upper()
        if choice == "" or choice == "Y":
            return True
        else:
            return False

#store variables for calling in custom messages
variables = {
    'computer': socket.gethostname(),
    'username': getpass.getuser(),
    'nl': '\n'
}
options = {
    'message': '', #store custom message if one is created
    'drive': ''
}


defaultMsg='You forgot to logout of {computer}!\nThis is a friendly reminder that you should probably do that next time.'.format(**variables)




def update():
    updateAttempt=0
    display()
    print('Checking for updates...')
    try: #remove previous version if just updated
        global proj
        with open(proj+'.tmp', 'r') as content_file:
            oldFile=str(content_file.read())
            if oldFile != os.path.basename(__file__): #if the old version has the current filename, don't delete
                os.remove(oldFile)
        os.remove(proj+'.tmp')
    except:
        pass
    while updateAttempt<3:
        updateAttempt=updateAttempt+1
        try:
            with urllib.request.urlopen("https://smcclennon.github.io/update/api/1") as url:
                repo=[]
                for line in url.readlines():
                    repo.append(line.decode().strip())
                api=repo[0] #latest release details
                proj=repo[1] #project name
                ddl=repo[2] #direct download
            with urllib.request.urlopen(api) as url:
                data = json.loads(url.read().decode())
                latest=data['tag_name'][1:]
                patchNotes=data['body']
            updateAttempt=3
        except:
            latest='0'
    if latest>ver:
        print('\nUpdate available!')
        print('Latest Version: v'+latest)
        print('\n'+str(patchNotes)+'\n')
        confirm=input(str('Update now? [Y/n] ')).upper()
        if confirm=='Y':
            latestFilename=proj+' v'+str(latest)+'.py'
            print(f'Downloading {latestFilename}...') #Download latest version to cwd
            urllib.request.urlretrieve(ddl, latestFilename)
            f=open(proj+'.tmp', 'w') #write the current filename to LTFO.tmp
            f.write(str(os.path.basename(__file__)))
            f.close()
            os.system('"'+latestFilename+'"') #open latest version
            exit()

def setupMessage():
    display()
    print('Computer: {computer}'.format(**variables))
    print('Username: {username}'.format(**variables))
    print('\nVariables: {computer}, {username}, {nl}')
    print('Enter your custom message. Leave blank to use the default message.')
    try:
        customMessage = input('\n> ').format(**variables)
    except:
        print('Invalid variable. Please try again.')
        sleep(1)
        setupMessage()
    options['message'] = customMessage
    confirmMessage()

def confirmMessage():
    display()
    customMsg = options['message']
    print(f'Custom Message: {"Disabled" if customMsg == "" else "Enabled"}')
    print(f'\n______ Message ______\n\n{defaultMsg if customMsg == "" else customMsg}\n\n______ Message ______\n')
    confirm = confirmChoice()
    if confirm:
        setupDrive()
    else:
        setupMessage()

def setupDrive():
    display()
    driveArray = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            driveArray.append(letter)
        bitmask >>= 1
    print('Available Drives:')
    for index, drive in enumerate(driveArray):
        print(f'{index + 1}. {drive}')
    print('\nPlease type the drive letter you wish to select. Leave blank to go back.')

    selectedDrive=input(str('> ')).upper()
    if selectedDrive=='':
        setupMessage()
    if not selectedDrive in driveArray:
        print('Specified drive not found. Please try again.')
        sleep(1)
        setupDrive()
    else:
        options['drive'] = selectedDrive
        confirmDrive()

def confirmDrive():
    display()
    selectedDrive = options['drive']
    print(f'Selected Drive: {selectedDrive}')
    time.sleep(0.5)
    confirm=  confirmChoice()
    if confirm:
        confirmWrite()
    else:
        setupDrive()

def confirmWrite():
    display()
    customMsg = options['message']
    selectedDrive = options['drive']

    print('Computer: {computer}'.format(**variables))
    print('Username: {username}'.format(**variables))

    print(f'Selected Drive: {options["drive"]}')

    print(f'Custom Message: {"Disabled" if customMsg is False else "Enabled"}')
    print(f'\n______ Message ______\n\n{defaultMsg if customMsg == "" else customMsg}\n\n______ Message ______\n')

    time.sleep(1)
    print(f'\nYou are about to flood all subdirectories in [{selectedDrive}:\\]!')
    time.sleep(0.5)
    confirm = confirmChoice()
    if confirm:
        commitWrite()
    else:
        setupDrive()

def commitWrite():
    display()

    rand=randint(10000,99999) #Create a random number for confirmation and filenames
    customMsg = options['message']
    selectedDrive = options['drive']

    print(f'\nSelected Drive: {selectedDrive}\n\nTo begin flooding, please enter the confirmation code {rand}.')
    confirm=input('\n>>> ')
    try:
        confirm=int(confirm)
    except:
        confirmWrite()
    if confirm!=rand:
        confirmWrite()

    removalMsg='\n\n\n\nInstructions to remove the files:\n\nAutomatic:\n1. Navigate to "'+selectedDrive+':\\"\n2. Run "Removal Tool ['+str(rand)+'].py"\n\nManual:\n1. Navigate to "'+selectedDrive+':\\"\n2. Search for "READ_ME ['+str(rand)+']"\n3. Select everything and delete'
    removalScript='#LTFO: Removal Tool\n#github.com/smcclennon/LTFO\nver="'+str(ver)+'"\nrand='+str(rand)+"\nselectedDrive='"+str(selectedDrive)+"'"+'''
import os,glob
from ctypes import windll
from pathlib import Path
windll.kernel32.SetConsoleTitleW('LTFO: Removal Tool - v'+str(ver))
filenameEstimate='READ_ME ['+str(rand)
scriptnameEstimate='Removal Tool ['+str(rand)
i=0
for x in Path(selectedDrive+':/').glob('**'):
        try:
            i=i+1
            for y in glob.glob(str(x)+'\\\\*'+filenameEstimate+'*.txt', recursive=True):
                    os.remove(y)
                    print(str(i)+'. Deleted: '+str(y))
        except:
            print('[FAILED]: '+str(x))
try:
    i=i+1
    for y in glob.glob(str(selectedDrive)+':\\\\'+scriptnameEstimate+'*.py', recursive=True):
            os.remove(y)
            print(str(i)+'. Deleted: '+str(y))
except:
    print('[FAILED]: '+str(x))
print('\\n\\nFile cleanup complete!')
os.system('timeout 3')'''

    i=0
    print('\nCreating files...')
    start=time.time() #take note of the current time
    for x in Path(selectedDrive+':/').glob('**'):
        if i==0:
            try: #Create the removal script
                filename=f'Removal Tool [{rand}].py'
                f=open(f'{x}\\{filename}', 'w')
                f.write(removalScript)
                f.close()
                i=i+1
                print(f'{i}. Created: {x}\\{filename}')
            except:
                print(f'[FAILED: REMOVAL SCRIPT]: {x}\\{filename}')
                print('***Failed to create removal script!***')

        try: #Create the READ_ME files
            filename= f'READ_ME [{rand}] [#{i}].txt'
            f=open(str(x)+'\\'+filename, 'w')
            msg = defaultMsg if customMsg == '' else customMsg
            f.write(msg+removalMsg)
            f.close()
            i=i+1
            print(f'{i}. Created: {x}\\{filename}')
        except Exception as e:
            print(f'[FAILED]: {x}\\{filename}')
            print(e)

    taken=time.time()-start #calculate how long the operation took
    print('\n')
    asciiRaw()
    print(f'Created {i} files in {(round(taken, 2))} seconds!\nPress any key to exit...')
    cmd('pause>nul')
    exit()

#Run the script
update() #check for updates
setupMessage() #Start at the setupMessage module
