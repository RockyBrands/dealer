# Author:        Rod Elliott
# Email:         me@rodelliott.com
# Date:          12/7/18
# Description:   Automates the process of transferring info from
#                the .xls store location template to an XML
#                file for upload to Demandware.

# May not need these modules, but tossing them in for starters.
import sys
import os
import shutil
from os import path
from PIL import Image
import fnmatch
