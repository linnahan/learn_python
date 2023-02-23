import wave
from pydub import AudioSegment
import struct

def wav_info():
    wave_file=wave.open(r"C:\Users\admin\Desktop\hhh.wav", 'r')
    channels=wave_file.getnchannels()#声道数
    samp_width=wave_file.getsampwidth()#采样大小
    frame_rate=wave_file.getframerate()#帧率
    numframes=wave_file.getnframes()#总帧数

    print("channel",channels)#声道数
    print('samp_width',samp_width)#采样大小2B 16bit
    print('frame_rate',frame_rate)#44100 帧率44100fps
    print('numframes',numframes)#总帧数=帧率*时间
    print('alltime',numframes/frame_rate)

    # for i in range(500):
    #     frame=wave_file.readframes(1)#读取1帧音频数据，可能包含多个声道信息
    #     print(frame,struct.unpack("h",frame[0:2])[0])#struct.unpack("h",frame[0:2])将二进制数据转化成10进制（16bit有符号整数）因为这里采样大小是16bit
    wave_file.close()

def cut_mp3(filepath):
    """
    # 程序流程
    1. 读取一个mp3文件,指定文件路径即可
    2. 根据用户选择设置截取片段，使用切片, 单位为ms
    3. 导出文件并保存, 指定导出文件名以及路径，最后指定导出的格式
    （其他编码格式，参考ffmpeg上的专业知识）

    :param filepath: 音乐文件路径, path
    :return: None
    """
    music = AudioSegment.from_mp3(file=filepath)
    sound_time = music.duration_seconds
    print(f"music duration time: {sound_time}")

    # 使用切片截取, 单位毫秒， 1s -> 1000ms
    out_music = music[15*1000+50: 15*1000+800]
    circle_out_musis = out_music * 20
    # 导出
    circle_out_musis.export(out_f=r"C:\Users\admin\Desktop\spleeter\cl.wav", format='wav')   # 可以指定bitrate为64k比特率 None为源文件

    print('done')


if __name__ == '__main__':
    src_path = r"C:\Users\admin\Desktop\spleeter\vo-hhh.wav"   # 要处理音频
    cut_mp3(filepath=src_path)




