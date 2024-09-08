import os
import shutil

def copy_src_to_dst(src="", dst=""):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(f"./{dst}")
    files = os.listdir(src)
    for file in files:
        file_path = os.path.join(src, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, dst)
        else:
            newsrc = os.path.join(src, file)
            newdst = os.path.join(dst, file)
            copy_src_to_dst(newsrc, newdst)

    


src = "static"
dst = "public"
copy_src_to_dst(src,dst)