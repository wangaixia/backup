import os
import tarfile

os.chdir('/tmp')
for file in os.walk("/tmp"):
    tar = tarfile.open("file.tar.gz", "w:gz")
    tar.add("catalina-2016-04-10.out")
tar.close()
