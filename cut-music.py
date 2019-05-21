from pydub import AudioSegment
file_name = "./media/zui-mei-qing-lv.mp3"
sound = AudioSegment.from_mp3(file_name)
start_time = "0:08"
stop_time = "1:37"
print ("time:",start_time,"~",stop_time)
start_time = (int(start_time.split(':')[0])*60+int(start_time.split(':')[1]))*1000
stop_time = (int(stop_time.split(':')[0])*60+int(stop_time.split(':')[1]))*1000
print("ms:",start_time,"~",stop_time)
word = sound[start_time:stop_time]
# save_name = "xiaye-and-anlian.mp3-"+file_name[6:]
save_name = "./media/zui-mei-qing-lv-cut.mp3"
print (save_name)
word.export(save_name, format="mp3",tags={'artist': 'AppLeU0', 'album': save_name[:-4]})
