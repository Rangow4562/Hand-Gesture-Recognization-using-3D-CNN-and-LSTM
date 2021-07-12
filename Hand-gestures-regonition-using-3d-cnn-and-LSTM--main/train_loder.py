import csv
import shutil

def copyDirectory(src , dest):
	try:
		shutil.copytree(src, dest)
		return 1
	# Directories are the same
	except shutil.Error as e:
		print('Directory not copied. Error: %s' % e)
		return 2
	#Any error saying that the directory doesn't exist
	except OSError as e:
		print('Directory not copied. Error: %s' % e)
		return 3
path_source = 'D:/3D-CNN/D/20bn-jester-v1/' # The folder that contains all the data (Jester 20bn)
csv_file = 'D:/3D-CNN/D/jester-v1-train.csv' # training csv file
file = open(csv_file, 'r')
reader = csv.reader(file, delimiter=';')

path_dest2 = 'D:/3D-CNN/D/final_train_set/'  # The folder where we will put all our training samples
class2 = ['Doing other things'] # The classes we want to use
rows2 = []
count2 = 0
simple2 = 200
for c in class2:
    for line in reader:
        target = line[1]
        ref = line[0]

        if target == c:
            dep  = copyDirectory(path_source+ref , path_dest2+ref)
            if dep == 1:
                count2 += 1
                rows2.append([ref, target])
            if count2 == simple2:
                break

path_dest10 = 'D:/3D-CNN/D/final_train_set/'  # The folder where we will put all our training samples
class10 = ['Swiping Right'] # The classes we want to use
rows10 = []
count10 = 0
simple10 = 1600
for c in class10:
    for line in reader:
        target = line[1]
        ref = line[0]

        if target == c:
            dep  = copyDirectory(path_source+ref , path_dest10+ref)
            if dep == 1:
                count10 += 1
                rows10.append([ref, target])
            if count10 == simple10:
                break

path_dest12 = 'D:/3D-CNN/D/final_train_set/'  # The folder where we will put all our training samples
class12 = ['Swiping Left'] # The classes we want to use
rows12 = []
count12 = 0
simple12 = 1600
for c in class12:
    for line in reader:
        target = line[1]
        ref = line[0]

        if target == c:
            dep  = copyDirectory(path_source+ref , path_dest12+ref)
            if dep == 1:
                count12 += 1
                rows12.append([ref, target])
            if count12 == simple12:
                break

path_dest5 = 'D:/3D-CNN/D/final_train_set/'  # The folder where we will put all our training samples

class5 = ['Zooming In With Two Fingers'] # The classes we want to use
rows5 = []
count5 = 0
simple5 = 1600
for c in class5:
    for line in reader:
        target = line[1]
        ref = line[0]

        if target == c:
            dep  = copyDirectory(path_source+ref , path_dest5+ref)
            if dep == 1:
                count5 += 1
                rows5.append([ref, target])
            if count5 == simple5:
                break

%%time
path_dest6 = 'D:/3D-CNN/D/final_train_set/'  # The folder where we will put all our training samples
class6 = ['Zooming Out With Two Fingers'] # The classes we want to use
rows6 = []
count6 = 0
simple6 = 1600
for c in class6:
    for line in reader:
        target = line[1]
        ref = line[0]

        if target == c:
            dep  = copyDirectory(path_source+ref , path_dest6+ref)
            if dep == 1:
                count6 += 1
                rows6.append([ref, target])
            if count6 == simple6:
                break