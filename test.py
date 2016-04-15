#!/usr/bin/python3.4

import os
import shutil
import time
import datetime
import tarfile

if os.path.exists('/tmp/test'):
	pass
else:
	os.mkdir('/tmp/test')

if os.path.exists('/etc/passwd'):
	shutil.copyfile('/etc/passwd','/tmp/test/passwd')
	tar = tarfile


