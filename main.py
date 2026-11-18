import os
import shutil

# The submitted image is fixed, so every offline run produces identical bytes.
os.makedirs('/output', exist_ok=True)
shutil.copyfile(os.path.join(os.path.dirname(__file__), 'news.png'), '/output/entry.png')
