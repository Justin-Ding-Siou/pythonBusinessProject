import fnmatch
import os
from PIL import Image
path = "f:\\python"
matches = []
for root, dirs, files in os.walk(path):
    for file in fnmatch.filter(files, '*.jpg'):
        matches.append((root, file))
for (mdir, mfile) in matches:
    im = Image.open(mdir+'\\'+mfile)
    print(mdir+'\\'+mfile, im.format, im.size)
    im2 = im.resize((int(im.size[0]*0.5), int(im.size[1]*0.5)))
    outfile = mdir+'\\'+os.path.splitext(mfile)[0]+'.png'
    im2.save(outfile, 'PNG')
