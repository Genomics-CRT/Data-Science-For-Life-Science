# Cygwin installation

If you don't have Windows 10, Cygwin is an alternative to the Windows Subsystem for Linux:

1. Determine whether your computer is running a 32-bit or 64-bit version of Windows (so you know which version of cygwin to install):

   - Click **Start**, type **system** in the search box, and then click **System** in the **Control Panel** list. 
   - Under **System**, you should see a heading for **System type**: this should tell you if it is a 32 or 64-bit operating system
   - More instructions available [here](https://support.office.com/en-ie/article/determine-whether-your-computer-is-running-a-32-bit-version-or-64-bit-version-of-the-windows-operating-system-aac162a1-0cb3-46f2-888f-2f22897396ce)

   ![get_system_type](./images/system_type_w10.png)

2.  Download the appropriate setup.exe cygwin file (32 or 64 bit) from this [link](https://cygwin.com/install.html)

3. Open this once it has downloaded to run it.

   ![run_cygwin_setup](./images/run_setup_exe.png)

4. You'll be given different options for how to install: choose install from internet.

5. Choose which root directory to install to. Automatically it will be something along the lines of `C:\cygwin64` (or 32); just leave it like this. You'll also be asked which users should have access to cygwin and where to install packages. Leave this as the defaults (All Users and Downloads).

6. Next you'll be asked to select your internet connection: choose to use system proxy settings.

   ![select_internet](./images/select_internet.png)

7. Then you'll be asked to choose a mirror for your downloads: see [here](https://cygwin.com/mirrors.html ) for a mirror near you (e.g. a UK one for people in Ireland), and it will start to download.

8. Next, you'll be asked to choose packages to install. I do **not** recommend downloading all packages. Install the base packages. I also recommend the following list. Some of these may be installed with the base packages, but double check, and if they aren't, install them. 

   - bash
   - bash-completion
   - curl
   - gawk
   - git
   - grep
   - gzip
   - hostname
   - less
   - mintty
   - nano
   - openssh
   - openssh-debuginfo
   - openssl
   - sed
   - tar
   - tmux
   - unzip
   - vim
   - wget
   - which
   - zip

There is an arrow beside the "Skip" bit on these (see the red circle in the screenshot below): click on it and choose the version to install. Feel free to add any packages you feel you might use: equally, don't worry too much if you end up missing something: you can add or update packages by running these installation steps again.

![select_package_cygwin](./images/select_pckg_version.png)

9. Once you continue here, the selected packages will be downloaded, checked for corruption and installed. This will take a while: on my old laptop (which is admittedly pretty slow), it took about two hours... go and make a cup of tea and do something else at this point! If something fails, click "try again" rather than quitting the installer. Network congestion may be an issue if you have trouble downloading packages: try a different mirror if this occurs.
10. You will be given the option to install shortcuts on your Desktop/ Start Menu- I recommend doing this for ease of access; then click finish so it finishes installing.
11. If you notice something doesn't work, check the **setup.exe** log file: this is located in` /var/log/setup.log.full `. To read this, type `more /var/log/setup.log.full` into the cygwin terminal; make a copy of it and try running the **setup.exe** file again. You can also report problems to cygwin [here](https://cygwin.com/problems.html) and, of course log issues with us in the issues tab on the github. To access your Desktop from the cygwin terminal, go to `/cygdrive/c/Users/username/Desktop`, but you don't need to worry about this for a few weeks.
