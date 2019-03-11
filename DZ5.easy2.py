import os
import pprint

dest_dir = input("Укажите директорию")
dir_path = os.path.join(dest_dir)

pprint.pprint(os.listdir(dir_path))
