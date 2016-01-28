import os
import shutil
z = os.path.join('tempdata', 'matty.shakespeare.tar.gz')


shutil.unpack_archive(z, extract_dir='tempdata')


