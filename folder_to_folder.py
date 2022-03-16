import os
import shutil

PATH1 = 'C:/Users/Desktop/bag_data_set/bag_thoufic/images'
PATH2 = 'C:/Users/Desktop/bag_data_set/bag_thoufic/labels'
folder1 = os.listdir(PATH1) # folder containing your files
folder2 = os.listdir(PATH2) # the other folder
#for item1,item2 in folder1,folder2:
for item1 in folder1:
     for item2 in folder2:
          f_name, f_ext = os.path.splitext(item1)
          l_name, l_ext = os.path.splitext(item2)
          if f_name==l_name:
               os.chdir(PATH1)
               img_dset = os.path.join('img_data')
               os.makedirs(img_dset, exist_ok=True)
               shutil.move(item1, os.path.join(img_dset, item1))
               # shutil.copy(item1, os.path.join(img_dset, f'{f_name}.jpg'))
               os.chdir(PATH2)
               lab_dset = os.path.join(str('labm_data'))
               os.makedirs(lab_dset, exist_ok=True)
               shutil.move(item2, os.path.join(lab_dset, item2))
          # else:
          #      os.chdir(PATH1)
          #      img_dset = os.path.join('img_data_wrong')
          #      # lab_dset = os.path.join(str('labm_data'))
          #      os.makedirs(img_dset, exist_ok=True)
          #      # os.makedirs(lab_dset, exist_ok=True)
          #      # shutil.copy(item1, (img_dset, item1))
          #      shutil.copy(item1, os.path.join(img_dset, item1))
          #      # shutil.move(item1, os.path.join(img_dset, f'{f_name}.jpg'))
          #      os.chdir(PATH2)
          #      lab_dset = os.path.join(str('labm_data_wrong'))
          #      os.makedirs(lab_dset, exist_ok=True)
          #      shutil.copy(item2, os.path.join(lab_dset, item2))
print('completed')
