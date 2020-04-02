import cv2


video = cv2.VideoCapture("2020-02-27 22-57-05.avi")
fps = video.get(cv2.CAP_PROP_FPS)
Count = video.get(cv2.CAP_PROP_FRAME_COUNT)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('帧率=%.1f'%fps)
print('帧数=%.1f'%Count)
print('分辨率',size)
print('视频时间=%.2f秒'%(int(Count)/fps))