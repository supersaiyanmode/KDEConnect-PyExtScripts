# KDEConnect-PyExtScripts

Sample scripts for PyExt plugin of KDEConnect.

All the files and folders need to go the location: `~/.kde/share/apps/kdeconnect/pyext/`. `kdeconnectd` will look 
into this folder and load all sub directories as independent python based plugins. Each plugin can listen for 
various events -- look into `metadata.json`.

----

##Metadata.json file.

If `Metadata.json` file is not present within the folder, PyExt will not load it. Explanation for various fields
in the JSON follows:

 - "name"
    - Type: String
    - Explanation: The value against this key appears in the Android ListView.
    - Eg: "Remote KDE Unlock"
 - "description"
    - Type: String
    - Explanation: The text that appears beneath the name in the list view.
    - Eg: "Unlock desktop from phone"
	- "entry_points"
	  - Type: JSON Object
	  - Child elements are string => string maps.
	  - Explanation: Each key represents the event that the script wants to listen for. Each value is of type String,
	    and represents name of the function within the script that will be invoked when this event occurs.
	  - Currently only one type of event is supported: "on_device_unlock".
