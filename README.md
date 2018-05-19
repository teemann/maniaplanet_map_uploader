# Maniaplanet Map Uploader
Simplifies the process of uploading a map (local or MX) to your server.
* Adds an option to upload to the context-menu of .gbx files.
* Adds a button to MX map pages to directly upload the map from there.

## Installation
* Download python 3.6
* Install the package *paramiko* (`pip install paramiko`)
* Download this repository
* Modify `settings.json` (only private key authorization is available)
* Modify lines 10 and 17 of `install.reg` to point to the correct directories
* *(Optional)* Install the Tampermonkey browser plugin
* *(Optional)* Add `MX server upload.user.js` to Tampermonkey

## Usage
To upload a local .Map.Gbx, right-click on the file and select `Upload to server`.  
To upload a file from MX, execute the optional installation steps, then navigate to a map-page on MX and click on the
button `Upload to server`.