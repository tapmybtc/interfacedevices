#!/usr/bin/env python3

# for more info see:
# https://ludovicrousseau.blogspot.com/2011/10/featureccidesccommand.html
# https://tech.springcard.com/tags/scard_ctl_code/
# pcsc10_v2.02.09.pdf and pcsc10_v2.02.02_sup.pdf from https://pcscworkgroup.com/Download/Specifications/pcsc1-10_v2.01.14.zip
# https://pyscard.sourceforge.io/
# OMNIKEY 5022 SOFTWARE DEVELOPER GUIDE PLT-03092 Version: A.1
# https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardconnecta
# apt install python3-pyscard

import smartcard
import sys
from smartcard.pcsc.PCSCPart10 import *

def get_user_selection(readers):
  print('===== Available Readers =====')
  for index, reader in enumerate(readers):
    print('{}) {}'.format(index, reader))
  print('=============================')
  while True:
    try:
      user_input = input('Which device do you want to reset to factory defaults (or q to quit)?: ').lower()
      if "q" == user_input:
        sys.exit(0)
      result = int(user_input, 10)
    except KeyboardInterrupt:
      sys.exit(0)
    except ValueError:
      result = -1
    if -1 < result < len(readers):
      return result
    else:
      print('Invalid selection')

def main(args):
  readers = smartcard.System.readers()
  reader_index = get_user_selection(readers)
  connection = readers[reader_index].createConnection()
  connection.connect(mode=SCARD_SHARE_DIRECT, disposition=SCARD_LEAVE_CARD)
  features = getFeatureRequest(connection)
  ccid_esc_command = hasFeature(features, FEATURE_CCID_ESC_COMMAND)
  if ccid_esc_command is None:
    # 1.3 Platform specific behaviors in OMNIKEY WORKBENCH TOOL 2 USER GUIDE PLT-04346, Rev. A.2
    # "On Linux, the application can communicate with a reader without a smart card present, if support for escape commands has been enabled in the Info.plist file."
    # Also, Appendix A in PLT-03092
    print('FEATURE_CCID_ESC_COMMAND not enabled, set bit 0 of ifdDriverOptions in the driver configuration to 1 and then restart pcscd.')
    # for example, you might do this:
    # sudo vim /usr/lib/pcsc/drivers/ifd-ccid.bundle/Contents/Info.plist
    # change the ifdDriverOptions string value to be 0x0001, save the change, and then run:
    # sudo systemctl restart pcscd
    return 1
  properties = getTlvProperties(connection, features)
  if properties['PCSCv2_PART10_PROPERTY_bPPDUSupport'] != 1:
    print('PPDU over SCardControl using FEATURE_CCID_ESC_COMMAND not supported')
    return 2
  response = connection.control(ccid_esc_command, list(bytes.fromhex('FF70076B08A206A104A902810000'))) # 7.6.2 restoreFactoryDefaults
  connection.disconnect()
  if list(bytes.fromhex('9D009000')) == response: # 7.6.2 restoreFactoryDefaults
    print('success')
    return 0
  else:
    print('restoreFactoryDefaults not successful')
    return 3

if __name__ == "__main__":
  sys.exit(main(sys.argv))

