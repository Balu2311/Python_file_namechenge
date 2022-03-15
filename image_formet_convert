import os
import shutil

base_dir = 'G:/Perput/Python_API/api/images'
os.chdir(base_dir)
for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    #f_company, f_interval, f_date = f_name.split('_')
    #interval = 1
    f_ext1='.jpg'
    if f_ext.lower() == '.jpg':
        f_ext = '.jpg'
    elif f_ext.lower() == '.png':
        f_ext = '.png'
    elif f_ext.lower() == '.jfif':
        f_ext = '.jfif'
    else:
        f_ext.lower() == '.jpep'
        f_ext = '.jpep'
    dest = os.path.join(str(f_ext1))
    os.makedirs(dest, exist_ok=True)
#     shutil.move(f, os.path.join(dest, f'{f_date}.csv'))
    shutil.copy(f, os.path.join(dest, f'{f_name}.png'))
