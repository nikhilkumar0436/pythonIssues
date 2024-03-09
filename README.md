# pythonIssues
This repo is for the issue which software profession deals while working in corporate word
![img.png](screenshots\img.png)

To fix this we need to enable the longpathsenabled from registryeditor
Through Registory Editor

**[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem]"LongPathsEnabled"=dword:00000001**

Through powershell

**New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force**
![img_1.png](screenshots\img_1.png)

After implementing the above solution

![img_2.png](screenshots\img_2.png)