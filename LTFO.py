# Log TF Out
# github.com/smcclennon/LTFO
ver = '4.2.0'
proj = 'LTFO'


# ----------------------------------------------------------------------------------------------

# Default message LTFO uses if the user presses [Enter] when asked to configure a custom message
# You can customise ('''the area between the triple quotes''')
# Variables: {computer}, {username}, {time}, {date}
Default_Message = '''You forgot to logout of {computer}!
This is a friendly reminder that you should probably do that next time.'''

# ----------------------------------------------------------------------------------------------



print('Importing requirements...')
try:
    # Attempt to import requirements
    import time, string, os, socket, getpass, urllib.request, json
    from ctypes import windll
    from random import randint
    from pathlib import Path
except:
    # Display error message on failure
    print('\nError: one or more libraries could not be imported!')
    print(f'Visit github.com/smcclennon/{proj} for support\n\nPress enter to exit...')
    input()
    exit()


# Set console window title
windll.kernel32.SetConsoleTitleW(f'{proj} - v{ver}')


# Run a specific command
def cmd(x):
    os.system(str(x))


# Pause the program for a specified amount of time
def sleep(x):
    time.sleep(x)


# LTFO logo
asciiRaw=f'''██╗  ████████╗███████╗ ██████╗
██║  ╚══██╔══╝██╔════╝██╔═══██╗
██║     ██║   █████╗  ██║   ██║  v{ver}
██║     ██║   ██╔══╝  ██║   ██║
███████╗██║   ██║     ╚██████╔╝
╚══════╝╚═╝   ╚═╝      ╚═════╝'''


# Clear the display
def display():
    cmd('cls')
    print(asciiRaw)


# Prompt the user to choose what to do
def confirmChoice():
    while True:
        choice = input('Confirm? [Y/n] ').upper()
        if choice == "" or choice == "Y":
            return True
        else:
            return False


# Store variables for calling in custom messages
variables = {
    'computer': socket.gethostname(),
    'username': getpass.getuser(),
    'time': time.strftime('%H:%M'),
    'date': time.strftime('%d.%m.%y')
}
options = {
    'message': '',  # Store custom message if one is created
    'drive': ''
}


def update():
    updateAttempt = 0
    display()
    print('Checking for updates...', end='\r')
    try:  # Remove previous version if just updated
        global proj
        with open(f'{proj}.tmp', 'r') as content_file:
            oldFile = str(content_file.read())
            # If the old version has the current filename, don't delete
            if oldFile != os.path.basename(__file__):
                os.remove(oldFile)
        os.remove(f'{proj}.tmp')
    except:
        pass
    while updateAttempt < 3:
        updateAttempt = updateAttempt+1
        try:
            with urllib.request.urlopen("https://smcclennon.github.io/update/api/1") as url:
                repo = []
                for line in url.readlines():
                    repo.append(line.decode().strip())
                apiLatest = repo[0]  # Latest release details
                proj = repo[1]  # Project name
                ddl = repo[2]  # Direct download
                apiReleases = repo[3] # List of patch notes
            with urllib.request.urlopen(apiLatest) as url:
                data = json.loads(url.read().decode())
                latest = data['tag_name'][1:]
            del data # Prevent overlapping variable data
            release = json.loads(urllib.request.urlopen(apiReleases).read().decode())
            releases = [
                (data['tag_name'],data['body'])
                for data in release
                if data['tag_name'] > ver][::-1]
            updateAttempt = 3
        except:
            latest = '0'
    if latest > ver:
        print('Update available!      ')
        print(f'Latest Version: v{latest}\n')
        for release in releases:
            print(f'{release[0]}:\n{release[1]}\n')
        confirm = input(str('Update now? [Y/n] ')).upper()
        if confirm == '' or confirm == 'Y':
            latestFilename = f'{proj} v{latest}.py'
            # Download latest version to cwd
            print(f'Downloading "{latestFilename}"...')
            urllib.request.urlretrieve(ddl, latestFilename)
            # Write the current filename to LTFO.tmp
            f = open(f'{proj}.tmp', 'w')
            f.write(str(os.path.basename(__file__)))
            f.close()
            os.system(f'"{latestFilename}"')  # Open latest version
            exit()


def setupMessage():
    display()
    try:
        #global defaultMsg
        defaultMsg = Default_Message.format(**variables)
    except:
        # Load the backup defaultMsg. It is reccomended that you do not touch this.
        defaultMsg = '''You forgot to logout of {computer}!
This is a friendly reminder that you should probably do that next time.'''.format(**variables)
        print('''Error: Unable to parse variables used in "Default_Message".
To fix this, remove any invalid {variables} from "Default_Message" at the top of this script.

Loaded backup message.
''')

    print('''\r
Computer: {computer}
Username: {username}
Time: {time}
Date: {date}'''.format(**variables))
    print('\nVariables: {computer}, {username}, \\n')
    print('Enter your custom message. Leave blank to use the default message.')
    try:
        customMessage = input('\n> ').format(**variables).replace('\\n', '\n')
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
    print(
        f'\n______ Message ______\n\n{defaultMsg if customMsg == "" else customMsg}\n\n______ Message ______\n')
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

    selectedDrive = input(str('> ')).upper()
    if selectedDrive == '':
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
    confirm = confirmChoice()
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

    # Create a random number for confirmation and filenames
    rand = randint(10000, 99999)
    customMsg = options['message']
    selectedDrive = options['drive']

    print(f'\nSelected Drive: {selectedDrive}\n\nTo begin flooding, please enter the confirmation code {rand}.')
    confirm = input('\n>>> ')
    try:
        confirm = int(confirm)
    except:
        confirmWrite()
    if confirm != rand:
        confirmWrite()

    # Removal instructions written to all READ_ME files
    removalMsg = f'''\n\n\n
Instructions to remove the files:

Automatic:
1. Navigate to "{selectedDrive}:\\"
2. Run "Removal Tool [{rand}].py"

Manual:
1. Navigate to "{selectedDrive}:\\"
2. Search for "READ_ME [{rand}]"
3. Select everything and delete'''

    # Removal script created at the root of the selected drive
    removalScript = f'''#{proj}: Removal Tool
#github.com/smcclennon/LTFO
ver="{ver}"
rand="{rand}"
selectedDrive="{selectedDrive}"
import os,glob
from ctypes import windll
from pathlib import Path
windll.kernel32.SetConsoleTitleW('{proj}: Removal Tool - v'+ver)
filenameEstimate='READ_ME ['+rand
scriptnameEstimate='Removal Tool ['+rand
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

    print('\nCreating files...')
    global cancel, i, start
    cancel=0
    i = 0
    start = time.time()  # Take note of the current time
    for x in Path(selectedDrive+':/').glob('**'):
        if i == 0:
            try:  # Create the removal script
                filename = f'Removal Tool [{rand}].py'
                f = open(f'{x}\\{filename}', 'w')
                f.write(removalScript)
                f.close()
                i = i+1
                print(f'{i}. Created: {x}\\{filename}')
            except:
                print(f'''
=====================================================
[FAILED: REMOVAL SCRIPT]: {x}\\{filename}
***Failed to create LTFO removal script!***

Removing generated files will have to be done
manually!

It is highly reccomended that you
cancel the operation!

No files have been generated yet.
=====================================================''')
                global taken
                taken = time.time()-start
                f.close()
                os.remove(f'{x}\\{filename}')
                confirm = input(str('Cancel the operation? [Y/n] ')).upper()
                if confirm != 'N':
                    cancel=1
                    stats()


        try:  # Create the READ_ME files
            filename = f'READ_ME [{rand}] [#{i}].txt'
            f = open(str(x)+'\\'+filename, 'w')
            msg = defaultMsg if customMsg == '' else customMsg
            f.write(msg+removalMsg)
            f.close()
            i = i+1
            print(f'{i}. Created: {x}\\{filename}')
        except Exception as e:
            print(f'[FAILED]: {x}\\{filename}')
            print(e)
    stats()
def stats():
    if cancel==0:
        global taken
        taken = time.time()-start  # Calculate how long the operation took
    print('\n')
    print(asciiRaw)
    print(f'''Created {i} files in {(round(taken, 2))} seconds!
         Press any key to exit...''')
    cmd('pause>nul')
    exit()


# Run the script
try:
    update()  # Check for updates
    setupMessage()  # Start at the setupMessage module
except:
    print(f'''\n\n\nAn error occured after {proj} successfully loaded.
Visit github.com/smcclennon/{proj} for support''')
    windll.user32.MessageBoxW(0, f'''An error occured after {proj} successfully loaded.
Visit github.com/smcclennon/{proj} for support.
Press OK to exit.''', f'{proj} v{ver}', 1)
    exit()