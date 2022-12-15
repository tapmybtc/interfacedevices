# HID OMNIKEY 5022 CL

```
OMNIKEY Workbench Tool
Version: 2.2.0

Vendor Name: HID Global
Product Name: OMNIKEY 5022
Platform Name: AViatoR
Firmware Version: 01.01.00
Firmware Label: OK5022-1.1.0.315-20171123T093856-61611489D942-FLASH
Hardware Version: PCB-00044 REV2
```

Part No: R50220318-GR

REV: C

FCC ID: JQ6-OK5022CL

UPC: 639399027949

Helpful Links

https://www.hidglobal.com/products/5022

https://www.hidglobal.com/documents/omnikeyr-5022-usb-reader-datasheet

https://www.hidglobal.com/sites/default/files/documentlibrary/eat-omnikey-5022-usb-reader-ds-en_2.pdf

https://www.hidglobal.com/documents/omnikey-5022-software-developer-guide

https://www.hidglobal.com/sites/default/files/documentlibrary/plt-03092_omnikey_5022_sw_dev_guide.pdf

https://www.hidglobal.com/documents/omnikey-product-selection-guide

https://www.hidglobal.com/sites/default/files/documentlibrary/eat-omnikey-product-cc-en.pdf

https://www.hidglobal.com/documents/omnikey-user-guide

https://www.hidglobal.com/sites/default/files/documentlibrary/plt-02395-a.6-omnikey-smart-card-reader-installation-guide-en.pdf

https://www3.hidglobal.com/drivers

https://www3.hidglobal.com/drivers/37337

https://www.hidglobal.com/documents/omnikey-contact-smart-card-readers-software-developer-guide

https://www.hidglobal.com/sites/default/files/documentlibrary/plt-03099_a.5_-_omnikey_sw_dev_guide_0.pdf

https://www.hidglobal.com/documents/omnikey-contactless-developer-guide

https://www.hidglobal.com/sites/default/files/documentlibrary/5321-903_b.4_omnikey_contactless_developer_guide_en.pdf

https://github.com/hidglobal/HID-OMNIKEY-Sample-Codes

https://apps.fcc.gov/oetcf/eas/reports/ViewExhibitReport.cfm?mode=Exhibits&calledFromFrame=N&application_id=xIvaTBL8kP6Wy%2BNwzx5bxg%3D%3D&fcc_id=JQ6-OK5022CL

https://ccid.apdu.fr/ccid/shouldwork.html#0x076B0x5022

https://www.youtube.com/watch?v=M2ey-ZFiolg&list=PLXsEtURGV4pQHS4UymbgHa2FXCB6Zk50U

```
> lsusb -v -d '076b:5022'

Bus XXX Device XXX: ID 076b:5022 OmniKey AG OMNIKEY 5022 Smart Card Reader
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               2.00
  bDeviceClass            0 
  bDeviceSubClass         0 
  bDeviceProtocol         0 
  bMaxPacketSize0         8
  idVendor           0x076b OmniKey AG
  idProduct          0x5022 
  bcdDevice            1.01
  iManufacturer           1 HID Global
  iProduct                2 OMNIKEY 5022 Smart Card Reader
  iSerial                 3 XX-XXXXXXXX-XXXX-XXXXXX
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength       0x005d
    bNumInterfaces          1
    bConfigurationValue     1
    iConfiguration          0 
    bmAttributes         0xa0
      (Bus Powered)
      Remote Wakeup
    MaxPower              250mA
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           3
      bInterfaceClass        11 Chip/SmartCard
      bInterfaceSubClass      0 
      bInterfaceProtocol      0 
      iInterface              2 OMNIKEY 5022 Smart Card Reader
      ChipCard Interface Descriptor:
        bLength                54
        bDescriptorType        33
        bcdCCID              1.10  (Warning: Only accurate for version 1.0)
        nMaxSlotIndex           0
        bVoltageSupport         7  5.0V 3.0V 1.8V 
        dwProtocols             3  T=0 T=1
        dwDefaultClock       4800
        dwMaxiumumClock      4800
        bNumClockSupported      0
        dwDataRate          12903 bps
        dwMaxDataRate      825807 bps
        bNumDataRatesSupp.      0
        dwMaxIFSD             254
        dwSyncProtocols  00000000 
        dwMechanical     00000000 
        dwFeatures       000404BA
          Auto configuration based on ATR
          Auto voltage selection
          Auto clock change
          Auto baud rate change
          Auto PPS made by CCID
          Auto IFSD exchange
          Short and extended APDU level exchange
        dwMaxCCIDMsgLen       520
        bClassGetResponse    echo
        bClassEnvelope       echo
        wlcdLayout           none
        bPINSupport             0 
        bMaxCCIDBusySlots       1
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x02  EP 2 OUT
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0040  1x 64 bytes
        bInterval               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x83  EP 3 IN
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0040  1x 64 bytes
        bInterval               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x84  EP 4 IN
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0008  1x 8 bytes
        bInterval              24
Device Status:     0x0000
  (Bus Powered)
```
