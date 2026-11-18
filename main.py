import os
import shutil

# Copy the reviewed newspaper image unchanged on every offline run.
os.makedirs('/output', exist_ok=True)
shutil.copyfile(os.path.join(os.path.dirname(__file__), 'world-news-2026-11-17.jpg'), '/output/entry.png')
