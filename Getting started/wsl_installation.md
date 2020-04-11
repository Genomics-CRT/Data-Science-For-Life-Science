# Installing a Windows Subsystem for Linux

Many bioinformatics tools are built for Unix-like operating systems. If you're a mac or linux user, great: you can go straight to your terminal and skip this tutorial. If you're a Windows user, it's a good idea to install something to allow you to use the command line tools we'll talk about later in this workshop.

This is a step-by-step tutorial on how to install the windows subsystem for linux (https://docs.microsoft.com/en-us/windows/wsl/about). The linked page has pretty clear instructions on how to install WSL, but I've put together some step-by-step instructions here. You may not end up using this tool for the first bit of the workshop, but command line tools such as awk, sed and grep are incredibly useful, for example when preparing files to visualise data. 

## Installation instructions

1. Open powershell in windows: right-click and choose to run as admin.
   - If you forget to right-click, type `Start-Process powershell -Verb runAs` to run as administrator.
   You might see this error message if you forget to run as admin: don't worry, just type in the command above.
   ![run_as_admin_error_powershell](./images/error_bc_not_admin.png)
2. The prompt should read something like `PS C:\WINDOWS\system32>`; At this point, type in `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`
3. This then starts loading (it might take a few minutes). When prompted to restart your computer, type in Y.
4. The next steps depend on what build of windows you have. Type `systeminfo | Select-String "^OS Name","^OS Version" ` into powershell; OS Name and Version will be printed to the screen. 

![get_build_number](./images/how_to_get_buildno.png)

5. For Build 16215 **or later**: we're going to be installing Ubuntu 18.04 LTS. Click on this link: https://www.microsoft.com/store/apps/9N9TNGVNDL3Q and click "get", and it should start downloading.

## Initialisation

Once you've finished installing, you'll be prompted to launch ubuntu. At this point, you may want to pin it to your start menu, to make it easily accessible. 

A console window will open, and you will need to wait for the installation to complete- this may take a couple of minutes. 

Once this is finished, you'll be prompted to set up a new user account and set a password. You *don't* need to enter the password every time you're using the terminal, but if you need special permission to run a process (e.g. installing something), you'll need to know your password, so make sure it's something you remember!

Once you've done this; you should run sudo apt update and sudo apt upgrade to update and upgrade packages; 

`sudo apt update && sudo apt upgrade`

![initialise_ubuntu](./images/initialise_ubuntu.png)

This isn't done automatically, so you should do this on a semi-regular basis. 
(You'll need your password to do this- sudo is a special command that "elevates" a process to give it special permissions)

Then you're good to go!

## Accessing your files
This will become important later in this series of workshops!

If you were using a Linux machine, your *actual* home directory would be at '~'

However, this is not the case with WSL: you need to change directory to /mnt/c to access your Windows filesystem, using the 'cd' command: `cd /mnt/c/`

![getting_your_files](./images/wsl_ls_mnt_screenshot.png)

Then, to get your personal files, go into Users/username/ and from there to whereever you keep your files. For example: `cd /mnt/c/Users/user/Desktop`

Don't worry if you don't know any of these commands yet: we will be publishing a beginner's guide to command line tools for bioinformatics over the course of the workshop. 

Remember to log any issues if you have them, and we will help you as quickly as we can. 

