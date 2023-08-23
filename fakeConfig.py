import os
import subprocess
from Settings.settings import * #get the name of firmware image


GUIDIR=os.environ.get('GUI_dir')
#print(GUIDIR)

#firmwareImage = firmware_image[self.module.getType()][os.environ.get('Ph2_ACF_VERSION')]

#FIX IT ! warning! : in the board class the module type should be like "SingleSCC" not RD53B/A
#RD53B/A is the board type

firmwareImage = firmware_image["SingleSCC"][os.environ.get('Ph2_ACF_VERSION')]


#FIX it later currently using the xml from Ph2_ACF submodule.

boardtype = 'RD53B'
#fwlist = subprocess.run(["fpgaconfig","-c",os.environ.get('GUI_dir')+'/Gui/CMSIT_{}.xml'.format(boardtype),"-l"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
fwlist = subprocess.run(["fpgaconfig","-c",os.environ.get('XMLlocation')+'/CMSIT_{}.xml'.format(boardtype),"-l"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#print the list of image but fail(nothing is print out) (fixed by copy&paste setting folder from submodule)
#warning: logger.conf is missing. what is this? - > a file from setting folder


print("firmwarelist is {0}".format(fwlist.stdout.decode('UTF-8'))) #nothing is printed out why?
print(fwlist.stderr.decode('UTF-8'))
print("firmwareImage is {0}".format(firmwareImage))

#choose image
fwload = subprocess.run(["fpgaconfig","-c", os.environ.get('XMLlocation')+"/CMSIT_{}.xml".format(boardtype),"-i", "{}".format(firmwareImage)],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print(fwload.stdout.decode('UTF-8'))
print(fwload.stderr.decode('UTF-8'))

#reset
fwreset = subprocess.run(["CMSITminiDAQ","-f", os.environ.get('XMLlocation')+"/CMSIT_{}.xml".format(boardtype),"-r"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print(fwreset.stdout.decode('UTF-8'))
print("fwreset err:"+fwreset.stderr.decode('UTF-8'))
"fwreset err:terminate called after throwing an instance of 'Exception' what():  [RD53::loadfRegMapd] The RD53 file settings does not exist"