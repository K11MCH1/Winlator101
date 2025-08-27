# COLLECTION OF GAME FIXES AND MORE

This page provides a comprehensive collection of Fixes, workarounds, and patches designed to resolve issues affecting certain games and Winlator functionalities.

## AUDIO

### Fixing Red Dead Redemption in-game audio/music.  

&nbsp;

Download: [xaudio2_9_RDR_fix.zip](https://github.com/user-attachments/files/19792268/xaudio2_9_RDR_fix.zip)  
<sub>credits: Luis Gaming</sub>

### **Installation**  

1- Extract in a directory you can access through your container.  
2- Copy/paste the 2 folders into `C:\windows`  
3- Double click the .reg file included.  

&nbsp;

## CONTROLLER

### Assassin's Creed 1 & 2 controller fix.

&nbsp;

**Assassin's Creed 1**  
Download: [AC1_fix_eaglePatch.zip](https://github.com/user-attachments/files/19792453/AC1_fix_eaglePatch.zip)  
<sub>credits: Sergeanur</sub>

### **Installation**  

1- Extract in a directory you can access through your container.  
2- Copy/paste files into AC1's main folder (where the .exe is).  
3- In the game shortcut's Environment Variable list add `WINEDLLOVERRIDES` = `dinput8=n,b`  

**Assassin's Creed 1** (soon - or check https://github.com/Sergeanur/EaglePatch)

&nbsp;

## OFFLINE MONO & GECKO INSTALLERS

If for some reason Winlator won't download them.

Download: http://www.mediafire.com/file/ct51nlnpvly2qn2/offline-wine-mono-gecko.zip - Thanks Generic CPU

1- Extract.
2- Install.

## RED DEAD REDEMPTION PERFORMANCE MOD

A bundle of DDLs that drastically increases performance for this game.

1- Extract.  
2- Place DLLs in main game folder next to the .exe.

Download: [RDR_performance_mod.zip](https://github.com/user-attachments/files/21782292/RDR_performance_mod.zip)  

## WRAPPER FIX FOR WINLATOR CMOD V13

This fixes some dx12 compatibility and other things. Tested on Winlator Cmod v13 and v13.1.1.

1- Unpack and place the .so file in Z:/lib within a container.

Note: This might break some games. Make sure to back up the original or you will need to Reinstall ImageFS in the Winlator main settings.

Download: [libvulkan_wrapper.zip](https://github.com/user-attachments/files/21919963/libvulkan_wrapper.zip)  

## MEDIAFOUNDATION FOR ARM64EC PROTON 9 & 10

A bundle of libraries that handle video playback in games. Used to fix, or partially fix, missing video playback or playback crashes.  

1- Unpack and run the install bat file in the 64bit folder.

Download: [mediafoundation.zip](https://github.com/user-attachments/files/22006182/mediafoundation.zip)


Note: This replaces the original files in the ImageFS which may break games that don't need this. To revert this you will have to delete containers and reinstall ImageFS in the Winlator main settings.  
Credits: JeezDisReez
