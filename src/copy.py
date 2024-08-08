import os
import shutil

rootdir = "pan15_training_datasetEnglish"
foldername = "Texts/"
i = 0
for subdir, dirs, files in os.walk(rootdir):
    print dirs, files
    for xfile in files:
        source = os.path.join(subdir, xfile)
        if i < 10:
            dest =  foldername + "00" + str(i) + xfile
        elif i < 100:
            dest =  foldername + "0" + str(i) + xfile
        else:
            dest =  foldername + str(i) + xfile
        shutil.copyfile(source, dest)
    i+=1