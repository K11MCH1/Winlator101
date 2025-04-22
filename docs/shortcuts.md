# SHORTCUTS

All the shortcuts made within containers will appear on this list.  
Winlator and box settings applied to these shortcuts will override container settings.

![image](https://github.com/user-attachments/assets/306af586-ac5a-494a-9bd6-da7ae3225c7f)


## HOW TO CREATE SHORTCUTS

![image](https://github.com/user-attachments/assets/e26963cf-e160-4f8e-a5fd-00ee7192e338)  

Within a container, navigate to the application's executable directory.  
Perform a right click to open up the context menu:

**Touch**: Hover over the .exe and with 2 fingers tap on the screen.  
**Mouse & Keyboard**: Click on the .exe once to select it, aftwards CTRL + LEFT CLICK.  

Finally tap/click on 'Create Shortcut'.

In some cases, games may include an unsupported `.exe` file or rely on an alternative, unsupported launcher—such as a `.bat` file—preventing shortcuts from appearing.  
i.e: Steam launcher with `.bat` file.

![image](https://github.com/user-attachments/assets/0a68934d-a283-48e1-b9dc-6346083104b4)  

This can be worked around by editing an existing executable, changing its path and pointing it to the `.bat` file.  
In the above case, you would create a shortcut of Steam's `.exe` first, then navigate to Desktop:

![image](https://github.com/user-attachments/assets/578cff93-d595-4900-b388-faf6aa19e0a9)  

Right click and Edit the `steam.desktop` file:

![image](https://github.com/user-attachments/assets/dbc933ea-f1a5-463f-b18e-25c529ea464c)  

And edit the ending of the `exec=` line:

![image](https://github.com/user-attachments/assets/6a2b8d9b-e5bc-437f-9ba1-6fa4491acbed)  

To

![image](https://github.com/user-attachments/assets/1452c6b8-165d-499c-8790-7fc354f6100d) 



### SHORTCUT OPTIONS

![scrcpy_yUns7GEBwU](https://github.com/user-attachments/assets/d6b95e3d-d6c3-4a95-8da4-0770a5e29919)  


This menu provides several options to manage the shortcuts.  

### [Shortcut Settings](/docs/shortcut_settings.md)  


### Add to Home Screen  

Adds a shortcut to the Android Home Screen.

### Remove  

Removes the shortcut.

### Export for Frontend  

Exports shortcut to Frontends such as ES-DE, Daijisho etc...

### Clone to Another Container  

Clones and transfers the shortcut to another container.

### Properties  

Play statistics.  

![image](https://github.com/user-attachments/assets/3df97835-fc99-462f-bb33-519dd9e5c694)

