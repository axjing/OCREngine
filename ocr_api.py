import easyocr
import time
import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(
    page_title="Anders OCR System",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "https://www.extremelycoolapp.com/bug"
    }
)
st.title('Anders OCR System')
st.write("小应用：准确高效的完成OCR识别任务，支持中、英、日、韩...等语言")
st.text("手机访问请把该链接复制到手机浏览器使用")
def image_input():
    if st.sidebar.checkbox('Upload'):
        content_file = st.sidebar.file_uploader("Choose a Content  Image", type=["png", "jpg"])
    else:
        content_file = st.sidebar.file_uploader("Choose a Content  Image", type=["png", "jpg"])
    if content_file is not None:
        start=time.time()
        # To read file as bytes:
        bytes_data = content_file.getvalue()
        content = Image.open(content_file)
        st.image(content)
        hist=content.histogram()

        print(hist)
        st.line_chart(hist)
        reader = easyocr.Reader(['ch_sim','en'],gpu=False,download_enabled=True) # this needs to run only once to load the model into memory
        with st.spinner('Wait for it...'):
            result = reader.readtext(np.array(content),detail = 0)

           
        s=""
        if len(result)==0:
           
            st.exception('图片中没有文字内容!')
        else:    
   
            for i in result:
                st.write(i)
                s+=i+'\n'
           
            st.info(s)
            st.success('OCR is a success message!')

        st.write("Time:{:.2f}".format(time.time()-start))
    else:
        st.warning("Upload an Image OR Untick the Upload Button")
        st.stop()


if __name__=="__main__":
    image_input()
