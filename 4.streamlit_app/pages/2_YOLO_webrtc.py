import streamlit as st 
from streamlit_webrtc import webrtc_streamer
import av
from prediction import YOLO_Pred

yolo = YOLO_Pred('./models/best.onnx',
                 './models/data.yaml')


def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    pred_img = yolo.predictions(img)

    return av.VideoFrame.from_ndarray(pred_img, format="bgr24")


webrtc_streamer(key="example", 
                video_frame_callback=video_frame_callback,
                media_stream_constraints={"video":True,"audio":False})