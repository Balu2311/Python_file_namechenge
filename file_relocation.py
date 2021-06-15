import os
import shutil

base_dir = 'G:\dev\projects\GolldenCarat\docs\datas'
os.chdir(base_dir)

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_company, f_interval, f_date = f_name.split('_')
    interval = 1
    if f_interval.lower() == 'minute':
        interval = 1
    elif f_interval.lower() == '2minute':
        interval = 2
    elif f_interval.lower() == '3minute':
        interval = 3
    elif f_interval.lower() == '4minute':
        interval = 4
    elif f_interval.lower() == '5minute':
        interval = 5
    dest = os.path.join(f_company, str(interval))
    os.makedirs(dest, exist_ok=True)
#     shutil.move(f, os.path.join(dest, f'{f_date}.csv'))
    shutil.copy(f, os.path.join(dest, f'{f_date}.csv'))