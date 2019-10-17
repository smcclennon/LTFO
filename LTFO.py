#Log TF Out
#github.com/smcclennon/LTFO
ver='3.0.3'
proj='LTFO'


print('Importing requirements...')
try:
    import time,string,os,socket,getpass,urllib.request,json
    from ctypes import windll
    from random import randint
    from pathlib import Path
except:
    print('Error: one or more libraries could not be imported!')
    print('Visit github.com/smcclennon/LTFO for support\n\nPress enter to exit...')
    input()
    exit()

windll.kernel32.SetConsoleTitleW(proj+' - v'+str(ver)) #Set console window title


def cmd(x):
    os.system(str(x))
def sleep(x):
    time.sleep(x)
def asciiRaw():
    print('''██╗  ████████╗███████╗ ██████╗ 
██║  ╚══██╔══╝██╔════╝██╔═══██╗
██║     ██║   █████╗  ██║   ██║  v'''+str(ver)+'''
██║     ██║   ██╔══╝  ██║   ██║
███████╗██║   ██║     ╚██████╔╝
╚══════╝╚═╝   ╚═╝      ╚═════╝''')
def display():
    cmd('cls')
    asciiRaw()
global confirm
computer=str(socket.gethostname())
username=str(getpass.getuser())


#You can customise this!
defaultMsg='You forgot to logout of '+computer+'!\nThis is a friendly reminder that you should probably do that next time.'

def update():
    updateAttempt=0
    display()
    print('Checking for updates...')
    try: #remove previous version if just updated
        global proj
        with open(proj+'.tmp', 'r') as content_file:
            os.remove(str(content_file.read()))
        os.remove(proj+'.tmp')
    except:
        pass
    while updateAttempt<3:
        updateAttempt=updateAttempt+1
        try: #Get latest version number (2.0.0)
            with urllib.request.urlopen("https://smcclennon.github.io/update/api/1") as url:
                global repo
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
            print('Downloading '+latestFilename+'...') #Download latest version to cwd
            urllib.request.urlretrieve(ddl, latestFilename)
            f=open(proj+'.tmp', 'w') #write the current filename to LTFO.tmp
            f.write(str(os.path.basename(__file__)))
            f.close()
            os.system('"'+latestFilename+'"') #open latest version
            exit()

def setupMessage():
    display()
    print('Computer: '+computer)
    print('Username: '+username)
    print('\nEnter your custom message: (leave blank to skip)')
    global customMessage
    customMessage=input(str('> '))
    confirmMessage()

def confirmMessage():
    display()
    global msg
    if customMessage=='':
        print('Custom Message: Disabled')
        msg=defaultMsg
        print('\n______ Message ______\n\n'+msg+'\n\n______ Message ______\n')
    else:
        print('Custom Message: Enabled')
        msg=defaultMsg+'\n\nCustom Message:\n'+customMessage
        print('\n______ Message ______\n\n'+msg+'\n\n______ Message ______\n')
    confirm=input(str('\nConfirm? [Y/n] ')).upper()
    if confirm=='Y':
        setupDrive()
    else:
        setupMessage()

def setupDrive():
    display()
    driveArray = [] #Search for drives
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            driveArray.append(letter)
        bitmask >>= 1
    print('Available Drives:')
    i=0
    for x in driveArray:
        i=i+1
        print('{}. {}'.format(i,str(x))) #format what {} values are
    print('\nPlease type the drive letter you wish to select (leave blank to go back)')
    global selectedDrive
    selectedDrive=input(str('> ')).upper()
    if selectedDrive=='':
        setupMessage()
    if not selectedDrive in driveArray:
        print('Specified drive not found. Please try again.')
        sleep(1)
        setupDrive()
    else:
        confirmDrive()

def confirmDrive():
    display()
    print('Selected Drive: '+selectedDrive)
    time.sleep(0.5)
    confirm=input(str('Confirm? [Y/n] ')).upper()
    if confirm=='Y':
        confirmWrite()
    else:
        setupDrive()

def confirmWrite():
    display()
    print('Computer: '+computer)
    print('Username: '+username)
    if customMessage=='':
        print('Custom Message: Disabled')
    else:
        print('Custom Message: Enabled')
    print('Selected Drive: '+selectedDrive)
    print('\n______ Message ______\n'+msg+'\n______ Message ______\n')
    time.sleep(1)
    print('\nYou are about to flood all subdirectories in ['+selectedDrive+':\\]!')
    time.sleep(0.5)
    confirm=input(str('Are you sure? [Y/n] ')).upper()
    if confirm=='Y':
        commitWrite()
    else:
        setupDrive()

def commitWrite():
    global rand
    rand=randint(10000,99999) #Create a random number for confirmation and filenames
    display()
    print('\nSelected Drive: '+selectedDrive+'\n\nTo begin flooding, please type this confirmation code: '+str(rand))
    confirm=input('\n>>> ')
    try:
        confirm=int(confirm)
    except:
        confirmWrite()
    if confirm!=int(rand):
        del rand
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

    global i
    global start
    i=0
    print('\nCreating files...')
    start=time.time() #take note of the current time
    for x in Path(selectedDrive+':/').glob('**'):
        if i==0:
            try:
                filename='Removal Tool ['+str(rand)+'].py'
                f=open(str(x)+'\\'+filename, 'w')
                f.write(removalScript)
                f.close()
                i=i+1
                print(str(i)+'. Created: '+str(x)+'\\'+filename)
            except:
                print('[FAILED: REMOVAL SCRIPT]: '+str(x)+'\\'+filename)
                print('***Failed to create removal script!***')
        try:
            filename='READ_ME ['+str(rand)+'] [#'+str(i)+'].txt'
            f=open(str(x)+'\\'+filename, 'w')
            f.write(msg+removalMsg)
            f.close()
            i=i+1
            print(str(i)+'. Created: '+str(x)+'\\'+filename)
        except:
            print('[FAILED]: '+str(x)+'\\'+filename)
    global taken
    taken=time.time()-start #calculate how long the operation took
    print('\n')
    asciiRaw()
    print('Created '+str(i)+' files in '+str(round(taken, 2))+' seconds!\nPress any key to exit...')
    cmd('pause>nul')
    exit()

#Run the script
update() #check for updates
setupMessage() #Start at the setupMessage module

