import cv2


video = cv2.VideoCapture("/Volumes/EAGET忆捷/爱咲/082710-465-carib-whole2048.wmv")
fps = video.get(cv2.CAP_PROP_FPS)
Count = video.get(cv2.CAP_PROP_FRAME_COUNT)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('帧率=%.1f'%fps)
print('帧数=%.1f'%Count)
print('分辨率',size)
print('视频时间=%.2f秒'%(int(Count)/fps))