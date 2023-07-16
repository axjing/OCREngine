import easyocr
import pandas as pd
import PIL
from PIL import ImageDraw
def easyocr_launch(im_path,download_enabled=True):
    reader = easyocr.Reader(['ch_sim','en'], download_enabled=download_enabled) # this needs to run only once to load the model into memory
    text = reader.readtext(im_path)
    print(text)
    return text
def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image
def eastocr_inference(im_path, lang=['ch_sim','en'],save_path=None):
    reader = easyocr.Reader(lang)
    bounds = reader.readtext(im_path)
    im = PIL.Image.open(im_path)
    draw_boxes(im, bounds)
    if not save_path:
        save_path="../data/save_exp.png"
    im.save(save_path)
    return im, pd.DataFrame(bounds).iloc[: , 1:]
if __name__=="__main__":
    
    im_file=r"../data/exp1.png"
    # easyocr_launch(im_file)
    
    eastocr_inference(im_file)