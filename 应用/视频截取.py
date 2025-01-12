import cv2
from tqdm import tqdm

def cut_video(input_path, output_path, start_time_seconds):
    # 打开视频文件
    cap = cv2.VideoCapture(input_path)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    # 获取视频的帧率
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Video FPS: {fps}")
    
    # 计算要跳过的帧数
    frames_to_skip = int(start_time_seconds * fps)
    print(f"Frames to skip: {frames_to_skip}")
    
    # 跳过指定的帧数
    cap.set(cv2.CAP_PROP_POS_FRAMES, frames_to_skip)
    
    # 获取视频的总帧数
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - frames_to_skip
    print(f"Total frames to process: {total_frames}")
    
    # 获取视频的宽度和高度
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # 定义视频编码器并创建VideoWriter对象
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 使用XVID编码器
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    # 读取并写入剩余的帧
    for _ in tqdm(range(total_frames), desc="Processing frames"):
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
    
    # 释放资源
    cap.release()
    out.release()
    print(f"Video saved as {output_path}")

# 使用示例
input_video_path = '/Volumes/EAGET忆捷/爱咲/082710-465-carib-whole2048.wmv'
output_video_path = '/Volumes/EAGET忆捷/爱咲/2.wmv'
start_time_seconds = 4500  

cut_video(input_video_path, output_video_path, start_time_seconds)