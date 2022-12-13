# Common Documentation

Helpful links

https://en.wikipedia.org/wiki/CCID_(protocol)

https://www.usb.org/document-library/smart-card-ccid-version-11

https://www.usb.org/sites/default/files/DWG_Smart-Card_CCID_Rev110.pdf

https://pcscworkgroup.com/specifications/

https://pcscworkgroup.com/specifications/download/

https://pcscworkgroup.com/Download/Specifications/pcsc1-10_v2.01.14.zip

https://github.com/LudovicRousseau/CCID

https://ccid.apdu.fr/

Helpful commands

`sudo apt install pcscd libccid`

`sudo systemctl stop pcscd.service`

`sudo /usr/sbin/pcscd --foreground --debug --apdu`

`sudo apt install pcsc-tools`

`pcsc_scan`

`sudo apt install opensc`

`opensc-tool -v -s 'ffca000000'`

`opensc-tool -v -s 'ffb0000004'`

