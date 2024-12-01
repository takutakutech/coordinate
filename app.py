import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import cv2

import ColorChart as CC

### streamlit run app.py で起動 ###

# タイトルとか
st.title("COLOR CHART APP !")
st.write("コーディネート写真のカラーチャートを出力するよ！")
#st.caption("どーも")


"""
### 画像をアップロードしてね
"""
# マジックコマンド？Markdown


# ファイルアップロード
upload_file = st.file_uploader("画像を選んでね！", type=["jpg", "png", "jpeg"])


# 画面を分割
col1, col2 = st.columns(2)

if upload_file is not None:
    # PIL.Image で画像を取得
    image = Image.open(upload_file)
    with col1:
        st.image(image, caption="アップロード完了！", use_container_width=True)
    
    # PIL から NumPy 配列に変換
    image_np = np.array(image)
    
    # RGB チャンネルが正しいか確認（もし違うならRGBに変換）
    if image.mode != "RGB":
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGBA2RGB)
    
    
    ### 関数を呼び出す
    # 主要な色と割合を取得して
    colors, proportions = CC.extract_colors(imageRGB = image_np)
    # カラーチャートに
    chart = CC.plot_color_chart(colors, proportions)
    
    # 出力
    with col2:
        st.pyplot(chart)


