import os
import shutil

os.makedirs('/output', exist_ok=True)
shutil.copyfile(os.path.join(os.path.dirname(__file__), 'news.png'), '/output/entry.png')
