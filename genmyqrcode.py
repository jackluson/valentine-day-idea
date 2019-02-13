import os
from MyQR import myqr
version, level, qr_name = myqr.run(
	'http://120.79.184.238/to-lover/',
	# 'https://jackluson.github.io/to-lover/',
    version=1,
    level='H',
    picture='cover.jpg',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name='ip_jackLu.png',
    save_dir=os.getcwd()
)
print('version',version)
print('level',level)
print('qr_name',qr_name)
# os.system('pause')