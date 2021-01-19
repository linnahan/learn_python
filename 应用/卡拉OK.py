# python的pyaudio卡拉OK简要声纹改变
import pyaudio
import wave
import random
import numpy as np
import time
 
p = pyaudio.PyAudio()
 
stream_in = p.open(format=pyaudio.paInt16,#格式
    channels=2,#通道
    rate=44100,#采样率
    input=True,
    frames_per_buffer=1024)
 
stream_out = p.open(format = pyaudio.paInt16,
    channels = 2,
    rate = 44100,
    output = True)
 
print("recording")
 
frames=[]
k = 0
while True:
    data = stream_in.read(1024)
    data_array = np.fromstring(data,dtype = np.short)
    print(len(frames))
    # print frames
    if len(frames) > 2:
        max_value_now = max(frames[len(frames) - 1])
        max_value_late = max(frames[len(frames) - 2])
        print(max_value_now)
        print(max_value_late)
        # rate_v_l = max_value_late / max_value_now
        # if rate_v_l > 10:
            # k = 1
 
    for j in range(len(data_array)):
        # data_array[j] = data_array[j] + random.uniform(-5,5)
        # data_array[j] = max_value
        # print data_array[j]
        modulo = data_array[j] % 10
        if modulo > 5:
            data_array[j] = data_array[j] + (10 - modulo)
        else:
            data_array[j] = data_array[j] - modulo
    data = data_array.tostring()
    stream_out.write(data)
    frames.append(data)
    if k != 0:
        k = 0
        print("start")
        time.sleep(5)
        print("end")
    # k += 1
    
print("recording ok")
 
stream_in.stop_stream()
stream_in.close()
p.terminate()
  
wf=wave.open("recording.wav",'wb')
wf.setnchannels(2)
wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
wf.setframerate(44100)
wf.writeframes(b''.join(frames))
wf.close()