import streamlit as st
import numpy as np
import cv2
from PIL import Image

import ColorChart as CC

# ファイルアップロード
uploaded_file = st.file_uploader("画像をアップロードしてください", type=["jpg"])

if uploaded_file is not None:
    # PIL.Image で画像を開く
    image = Image.open(uploaded_file)
    st.image(image, caption="アップロードされた画像", use_container_width=True)

    # PIL から NumPy 配列に変換
    image_np = np.array(image)
    
    
    # RGB チャンネルが正しいか確認（もし違うならRGBに変換）
    if image.mode != "RGB":
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGBA2RGB)
    
    
    # rename
    imageRGB = image_np
    
    
    ### 関数を呼び出す
    # 主要な色と割合を取得して
    colors, proportions = CC.extract_colors(imageRGB)
    # カラーチャートに
    chart = CC.plot_color_chart(colors, proportions)
    
    # 出力
    st.pyplot(chart)



