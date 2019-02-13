import os
# import time
from glob import glob
from PIL import Image
import pyperclip
source_dir = 'origin_images'
target_dir = 'images'
threshold = 1.5*1024*1024
if not os.path.exists(target_dir):
    os.makedirs(target_dir)
filenames = glob('{}/*.[jp]*'.format(source_dir))
# print(','.join(filenames))
strFileNames = ''
for i,filename  in enumerate(filenames):
  # 拼接文件名字符串
  strFileNames = strFileNames +  '"' + filename +'",'
  filesize = os.path.getsize(filename)
  output_filename = filename.replace(source_dir, target_dir)
  # output_filename = time.strftime("%Y-%m-%d", time.localtime()) + '000' + str(i) + '.png';

  print('output_filename:',output_filename)
  if filesize >= threshold:
    print(filename)
    with Image.open(filename) as im:
      width, height = im.size
      new_width = width // 2
      new_height = int(new_width * height * 1.0 / width)
      print('adjusted size:', new_width, new_height)
      resized_im = im.resize((new_width, new_height))
      resized_im.save(output_filename)
  else:
    with Image.open(filename) as im:
      im.save(output_filename)

# 字符串复制到剪切板
strFileNames = strFileNames.replace(source_dir + '\\', './' + target_dir + '/')
print(strFileNames[0:-1]);
pyperclip.copy(strFileNames[0:-1]);
spam = pyperclip.paste()