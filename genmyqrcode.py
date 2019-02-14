import os
from MyQR import myqr
version, level, qr_name = myqr.run(
	'https://jackluson.github.io/to-lover-demo/',
	# 'https://jackluson.github.io/to-lover/',
    version=1,
    level='H',
    picture='pic-icon.png',
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