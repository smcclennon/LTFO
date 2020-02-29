# Log TF Out
# github.com/smcclennon/LTFO
ver = '5.0.4'
proj = 'LTFO'


# ----------------------------------------------------------------------------------------------

# Bypass LTFO's default message: used when the user skips the custom message creator
# You can customise ('''the area between the triple quotes''')
# Variables: {computer}, {username}, {time}, {date}, $gui, $path/to/file
configureMessage = '''You forgot to logout of {computer}!
This is a friendly reminder that you should probably do that next time.'''

# ----------------------------------------------------------------------------------------------





# LTFO logo
asciiRaw = f'''██╗  ████████╗███████╗ ██████╗
██║  ╚══██╔══╝██╔════╝██╔═══██╗
██║     ██║   █████╗  ██║   ██║  v{ver}
██║     ██║   ██╔══╝  ██║   ██║
███████╗██║   ██║     ╚██████╔╝
╚══════╝╚═╝   ╚═╝      ╚═════╝'''
# Run a specific command
def cmd(x):
    os.system(str(x))
# Pause the program for a specified amount of time
def sleep(x):
    time.sleep(x)
# Clear the display
def display():
    cmd('cls')
    print(asciiRaw)



# -==========[ Update code ]==========-
# Updater: Used to check for new releases on GitHub
# github.com/smcclennon/Updater
import os  # detecting OS type (nt, posix, java), clearing console window, restart the script
from distutils.version import LooseVersion as semver  # as semver for readability
import urllib.request, json  # load and parse the GitHub API
import platform  # Consistantly detect MacOS

# Disable SSL certificate verification for MacOS (very bad practice, I know)
# https://stackoverflow.com/a/55320961
if platform.system() == 'Darwin':  # If MacOS
    import ssl
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context
proj = proj
if os.name == 'nt':
    import ctypes  # set Windows console window title
    ctypes.windll.kernel32.SetConsoleTitleW(f'   == {proj} v{ver} ==   Checking for updates...')

updateAttempt = 0  # Keep track of failed attempts
display()
print('Checking for updates...', end='\r')
while updateAttempt < 3:  # Try to retry the update up to 3 times if an error occurs
    updateAttempt = updateAttempt+1
    try:
        with urllib.request.urlopen("https://smcclennon.github.io/update/api/1") as internalAPI:
            repo = []
            for line in internalAPI.readlines():
                repo.append(line.decode().strip())
            apiLatest = repo[0]  # Latest release details
            proj = repo[1]  # Project name
            ddl = repo[2]  # Direct download link
            apiReleases = repo[3]  # List of patch notes
        with urllib.request.urlopen(apiLatest) as githubAPILatest:
            data = json.loads(githubAPILatest.read().decode())
            latest = data['tag_name'][1:]  # remove 'v' from version number (v1.2.3 -> 1.2.3)
        del data  # Prevent overlapping variable data
        release = json.loads(urllib.request.urlopen(  # Get latest patch notes
            apiReleases).read().decode())
        releases = [  # Store latest patch notes in a list
            (data['tag_name'], data['body'])
            for data in release
            if semver(data['tag_name'][1:]) > semver(ver)]
        updateAttempt = 3
    except:  # If updating fails 3 times
        latest = '0'
if semver(latest) > semver(ver):
    if os.name == 'nt': ctypes.windll.kernel32.SetConsoleTitleW(f'   == {proj} v{ver} ==   Update available: {ver} -> {latest}')
    print('Update available!      ')
    print(f'Latest Version: v{latest}\n')
    for release in releases:
        print(f'{release[0]}:\n{release[1]}\n')
    confirm = input(str('Update now? [Y/n] ')).upper()
    if confirm != 'N':
        if os.name == 'nt': ctypes.windll.kernel32.SetConsoleTitleW(f'   == {proj} v{ver} ==   Installing updates...')
        print(f'Downloading {proj} v{latest}...')
        urllib.request.urlretrieve(ddl, os.path.basename(__file__))  # download the latest version to cwd
        import sys; sys.stdout.flush()  # flush any prints still in the buffer
        os.system('cls||clear')  # Clear console window
        os.system(f'"{__file__}"' if os.name == 'nt' else f'python3 "{__file__}"')
        import time; time.sleep(0.2)
        quit()
if os.name == 'nt': ctypes.windll.kernel32.SetConsoleTitleW(f'   == {proj} v{ver} ==')
# -==========[ Update code ]==========-


import os
if os.name != 'nt':
    print(f'{proj} currently only supports Windows, and we have no plans to expand support to Unix any time soon\ndue to our relyance on ctypes.windll')
    print('\nHowever, this script will continue to recieve updates,\nincluding the possibility for Unix support in the future :)')
    print('\nhttps://github.com/smcclennon/LTFO')
    print('\nPress enter to exit')
    input()
    quit()
print('Importing requirements...')
try:
    # Attempt to import requirements
    import time, string, socket, getpass
    from ctypes import windll
    from random import randint
    from pathlib import Path
    from shutil import copyfile
except:
    # Display error message on failure
    print('\nError: one or more libraries could not be imported!'
          f'\nVisit github.com/smcclennon/{proj} for support\n\nPress enter to exit...')
    input()
    exit()



# Set console window title
windll.kernel32.SetConsoleTitleW(f'{proj} - v{ver}')







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
    'proj': proj,
    'message': '',  # Store message for file creation
    'messageBackup': '''You forgot to logout of {computer}!
This is a friendly reminder that you should probably do that next time.'''.format(**variables),
    'messageType': '',
    'filename': '',
    'filePath': '',
    'drive': '',
    'start': 0,
    'filesProcessed': 0,
    'processDuration': 0,
    'status': 0
}





def setupMessage():
    display()
# \033[F moves cursor to the beginning of the previous line
    print('''\033[F
Computer: {computer}
Username: {username}
Time: {time}
Date: {date}'''.format(**variables))
    print('\nVariables: {computer}, {username}, {time}, {date}, \\n')
    print('File selection: $gui, $path/to/file')
    print('\nEnter your custom message. Leave blank to use the default message.')
    try:
        customMessage = input('\n> ').format(**variables).replace('\\n', '\n')
    except:
        print('Invalid variable. Please try again.')
        sleep(1)
        setupMessage()
    options['message'] = customMessage
    options['messageType'] = 'Custom'
    confirmMessage()


def confirmMessage():
    support = 1
    display()
    customMessage = options['message']
    messageBackup = options['messageBackup']
    if customMessage == '':
        try:
            options['message'] = configureMessage.format(**variables)
            if options['message'] == options['messageBackup']:
                options['messageType'] = 'Default'
            else:
                options['messageType'] = 'Config'
        except:
            options['message'] = options['messageBackup']
            options['messageType'] = 'Backup'
            print('''Error: Unable to parse variables used in "configureMessage".
To fix this, remove any invalid {variables} from "configureMessage" at the top of this script.
''')

    message = options['message']

    # Custom file GUI mode
    if message == '$gui':
        try:
            import win32gui, win32con
        except:
            print('\nError: unable to import "pypiwin32", this is needed for GUI mode')
            confirm=input(str('Attempt to install "pypiwin32"? [Y/n] ')).upper()
            if confirm != 'N':
                try:
                    os.system('pip install pypiwin32 --user')
                    os.system('cls')
                    os.system('"'+str(os.path.basename(__file__))+'"')
                    exit()
                except:
                    print('Failed to install "pypiwin32"\nPress enter to go back...')
                    input()
                    setupMessage()
        try:
            print('Please select a file from the File picker GUI')
            selectedFile, Filter, flags = win32gui.GetOpenFileNameW(
                InitialDir=os.environ['temp'],
                Flags=win32con.OFN_EXPLORER,
                Title=f'{proj} v{ver}: Select a file to use for flooding',
                Filter='All files\0*.*\0',
                FilterIndex=0)
            display()
            options['filePath'] = selectedFile
            options['messageType'] = '$File'
            options['filename'] = os.path.basename(options['filePath'])
            try:
                with open(options['filePath'], 'r') as fileContents:
                    options['message'] = fileContents.read()
            except:
                options['message'] = 'Preview unavailable: Unsupported filetype'
                options['messageType'] = '$Copy'
            # Attempt to load variables
            try:
                options['message'] = options['message'].format(**variables)
            except:
                pass
        except:
            # No file selected
            setupMessage()

    # Custom file console mode
    elif message[0] == '$':
        try:
            if os.path.exists(os.path.join(os.path.dirname(__file__), message[1:])):
                options['filePath'] = os.path.join(
                    os.path.dirname(__file__), message[1:])
                options['messageType'] = '$File'
                options['filename'] = os.path.basename(options['filePath'])
                try:
                    with open(options['filePath'], 'r') as fileContents:
                        options['message'] = fileContents.read()
                except:
                    options['message'] = 'Preview unavailable: Unsupported filetype'
                    options['messageType'] = '$Copy'
                #Attempt to load variables
                try:
                    options['message'] = options['message'].format(**variables)
                except:
                    pass
        except:
            setupMessage()
    message = options['message']
    messageType = options['messageType']
    filename = options['filename']
    print(f'Message Type: {messageType}')
    if messageType == '$File' or messageType == '$Copy':
        print(f'Filename: {filename}')
    print(f'\n______ Message ______\n\n{message}\n\n______ Message ______\n')
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
    message = options['message']
    messageType = options['messageType']
    selectedDrive = options['drive']

    print('Computer: {computer}'.format(**variables))
    print('Username: {username}'.format(**variables))

    print(f'Selected Drive: {options["drive"]}')

    print(f'Message Type: {messageType}')
    if messageType == '$File' or messageType == '$Copy':
        filename = options['filename']
        print(f'Filename: {filename}')
    print(f'\n______ Message ______\n\n{message}\n\n______ Message ______\n')

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
    messageType = options['messageType']

    print(f'\nSelected Drive: {selectedDrive}\nMessage Type: {messageType}\n\nTo begin flooding, please enter the confirmation code {rand}.')
    confirm = input('\n>>> ')
    try:
        confirm = int(confirm)
    except:
        confirmWrite()
    i = 0
    if confirm != rand:
        confirmWrite()

    filePath = options['filePath']

    if options['messageType'] == '$File' or options['messageType'] == '$Copy':
        floodFilename = options['filename']
        filenameEstimate = options['filename']
        removaltoolFilename = f'Removal Tool [{floodFilename}].py'
        scriptnameEstimate = f'Removal Tool [{floodFilename}'
    else:
        scriptnameEstimate = f'Removal Tool [{rand}'
        filenameEstimate = f'READ_ME [{rand}'
        removaltoolFilename = f'{scriptnameEstimate}].py'

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
filenameEstimate="{filenameEstimate}"
scriptnameEstimate="{scriptnameEstimate}"
i=0
for x in Path(selectedDrive+':/').glob('**'):
        try:
            i=i+1
            for y in glob.glob(str(x)+'\\\\*'+filenameEstimate+'*', recursive=True):
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

    messageType = options['messageType']
    print('\nCreating files...')

    options['start'] = time.time()  # Take note of the current time
    for x in Path(selectedDrive+':/').glob('**'):
        if options['messageType'] != '$File' and options['messageType'] != '$Copy':
            floodFilename = f'READ_ME [{rand}] [#{i}].txt'
        if i == 0:
            try:  # Create the removal script
                filename = removaltoolFilename
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
                options['processDuration'] = time.time() - options['start']
                options['filesProcessed'] = i
                try:
                    f.close()
                    os.remove(f'{x}\\{filename}')
                except:
                    pass
                confirm = input(str('Cancel the operation? [Y/n] ')).upper()
                if confirm != 'N':
                    stats()

        try:  # Create the READ_ME files
            filename = floodFilename
            if messageType != '$Copy':
                f = open(str(x)+'\\'+filename, 'w')
                msg = options['message']
                if messageType != '$File':
                    f.write(msg+removalMsg)
                elif messageType == '$File':
                    f.write(msg)
                f.close()
            if messageType == '$Copy':
                copyfile(f'{filePath}', f'{x}\\{filename}')
            i = i+1
            print(f'{i}. Created: {x}\\{filename}')
        except Exception as e:
            print(f'[FAILED]: {x}\\{filename}')
            print(e)
    options['processDuration'] = time.time() - options['start']
    options['filesProcessed'] = i
    stats()


def stats():
    filesProcessed = options['filesProcessed']
    processDuration = options['processDuration']
    print('\n')
    print(asciiRaw)
    print(f'''Created {filesProcessed} files in {(round(processDuration, 2))} seconds!
         Press any key to exit...''')
    cmd('pause>nul')
    options['status'] = 1

# Debug = 0: Display a message and exit when an uncaught exception occurs
# Debug = 1: Show error details & crash when an uncaught exception occurs
debug = 0


# Run the script
if debug == 0:
    try:
        setupMessage()  # Start at the setupMessage module
    except:
        if options['status'] == 0:
            # Uncaught exception:
            print(f'''\n\n\nAn error occured after {proj} successfully loaded.
        Visit github.com/smcclennon/{proj} for support''')
            windll.user32.MessageBoxW(0, f'''An error occured after {proj} successfully loaded.
        Visit github.com/smcclennon/{proj} for support.
        Press OK to exit.''', f'{proj} v{ver}', 1)
        exit()
elif debug == 1:
    setupMessage()