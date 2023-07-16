import gradio as gr
from src.ocr import easyocr_launch
from src.ocr import eastocr_inference
from src.utils import LanguageCodes
import gradio as gr
import torch


def download_image():
    torch.hub.download_url_to_file('https://github.com/JaidedAI/EasyOCR/raw/master/examples/english.png', './data/english.png')
    torch.hub.download_url_to_file('https://github.com/JaidedAI/EasyOCR/raw/master/examples/thai.jpg', './data/thai.jpg')
    torch.hub.download_url_to_file('https://github.com/JaidedAI/EasyOCR/raw/master/examples/french.jpg', './data/french.jpg')
    torch.hub.download_url_to_file('https://github.com/JaidedAI/EasyOCR/raw/master/examples/chinese.jpg', './data/chinese.jpg')
    torch.hub.download_url_to_file('https://github.com/JaidedAI/EasyOCR/raw/master/examples/japanese.jpg', './data/japanese.jpg')
    torch.hub.download_url_to_file('https://github.com/JaidedAI/EasyOCR/raw/master/examples/korean.png', './data/korean.png')
    torch.hub.download_url_to_file('https://i.imgur.com/mwQFd7G.jpeg', './data/Hindi.jpeg')


title = 'EasyOCR'
description = 'Gradio demo for EasyOCR. EasyOCR demo supports 80+ languages.To use it, simply upload your image and choose a language from the dropdown menu, or click one of the examples to load them. Read more at the links below.'
article = "<p style='text-align: center'><a href='https://www.jaided.ai/easyocr/'>Ready-to-use OCR with 80+ supported languages and all popular writing scripts including Latin, Chinese, Arabic, Devanagari, Cyrillic and etc.</a> | <a href='https://github.com/JaidedAI/EasyOCR'>Github Repo</a></p>"
examples = [['english.png',['en']],['thai.jpg',['th']],['french.jpg',['fr', 'en']],['chinese.jpg',['ch_sim', 'en']],['japanese.jpg',['ja', 'en']],['korean.png',['ko', 'en']],['Hindi.jpeg',['hi', 'en']]]
examples = [['english.png',['en']],['chinese.jpg',['ch_sim', 'en']],['japanese.jpg',['ja', 'en']]]

css = "footer, .output_image, .input_image {visibility: hidden;height: 40rem !important; width: 100% !important;}"
choices =LanguageCodes().get_code()
webapp=gr.Interface(
    eastocr_inference,
    inputs=[gr.inputs.Image(type='filepath', label='Input'),gr.inputs.CheckboxGroup(choices, type="value", default=['ch_sim','en'], label='language')],
    outputs=[gr.outputs.Image(type='pil', label='Output'), gr.outputs.Dataframe(type='pandas',headers=['text', 'confidence'])],
    title=title,
    description=description,
    article=article,
    examples=examples,
    css=css,
    enable_queue=True
    )

if __name__ == "__main__":
    webapp.launch(share=False,debug=True)