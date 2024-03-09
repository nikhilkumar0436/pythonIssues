import os
import traceback
import zipfile


#solution, The issue is due to max limit of 260 characters path in windows system. so inorder to override.
#Windows Registry Editor Version 5.00
#[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem] "LongPathsEnabled"=dword:00000001
try:

    with zipfile.ZipFile(r'D:\Git\pythonIssues\Demo Zip to show how the issue happens and how to fix it.zip','r') as zip:
        zip.extractall()
    print('file has unzipped successfully')
except FileNotFoundError as err:
    print(str(err))
    print(traceback.format_exc())


