import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib as mpl


def convert_RGB(image_path):
    """画像をRGBに変換"""
    image = cv2.imread(image_path)
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # RGBで読み込む
    return imageRGB
    
def extract_colors(imageRGB, num_colors=5):
    """主要な色に分け、その割合を計算"""
    # 画像を2次元配列に変換
    pixels = imageRGB.reshape(-1,3)
    ### reshape()において「-1」は3行に合わせて自動でってことらしい！！！
    
    # KMeansクラスタリングで色を抽出 （今回は5つのクラスに分けられている。）
    kmeans = KMeans(n_clusters=num_colors, random_state=0) # ここは設定
    kmeans.fit(pixels) # ここで分けてる。
    
    # 主要な色とラベルを取得
    colors = kmeans.cluster_centers_ ### colors=[[R,G,B], ...]のように5つのクラスに分けられた。
    labels = kmeans.labels_ ### その5つのクラスに画素(pixel)が0~4で番号分けされてる → [0,0,1,1,2,2,2,3,3,4, ...] （ピクセル数ある）
    
    # 色の比率を計算
    labels_counts = np.bincount(labels)
    proportions = labels_counts / len(labels) ### colorsたちの割合
    
    return colors, proportions


def plot_color_chart(colors, proportions):
    # フォントサイズをグローバルに設定
    mpl.rcParams['font.size'] = 16

    # 円グラフ作成
    fig = plt.figure(figsize=(8,8))
    plt.pie(
        proportions, 
        labels = [f"{p*100:.1f}%" for p in proportions], 
        colors = [tuple(c/255 for c in color) for color in colors], # 色の正規化
        startangle = 90, # グラフ上から
        counterclock = False 
    )
    
    plt.title("COLOR CHART", fontsize=24)
    #plt.legend(fontsize=14)
    #plt.show()
    
    return fig


if __name__ == "__main__":
    image_path = "./img/image1_.jpg"
    num_colors = 4
    
    # 関数呼び出し
    colors, proportions = extract_colors(image_path, num_colors)
    plot_color_chart(colors, proportions)
