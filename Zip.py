import zipfile

import os

# zipFile = r'test.zip'
#
# zipTask1 = zipfile.ZipFile(zipFile,'r')
#
# for name in zipTask1.namelist():
#     print(name)
#
# for info in zipTask1.infolist():
#     print(info)
#
# zipTask1.close()


# zipTask2 = zipfile.ZipFile(zipFile,'a',zipfile.ZIP_DEFLATED)
#
# fileTxt = os.path.join(r'./',r'readme.txt')
#
# zipTask2.write(fileTxt,r'readme.txt')
#
# zipTask2.close()




zzipFile = r'test.zip'

targetDir = r'test.zip'

zipTask3 = zipfile.ZipFile(zipFile,'r',zipfile.ZIP_DEFLATED)

zipTask3.extractall(targetDir)

zipTask3.close()




