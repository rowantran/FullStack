import os

def rename_files(dirname):
    os.chdir(dirname)
    
    filenames = os.listdir(dirname)
    for f in filenames:
        replaced_name = f.translate(None, '0123456789')
        os.rename(f, replaced_name)

rename_files('/Users/RJ/Scripts/FullStack/prank/')
