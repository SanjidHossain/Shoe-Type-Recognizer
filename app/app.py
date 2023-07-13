import gradio as gr
from fastai.vision.all import load_learner

# import pathlib
# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath

shoe_labels = (
   'Army boots',
   'Ballet flats', 
   'Basketball shoes',
   'Brogues',
   'Chelsea Boot',
   'Chuck Taylor',
   'Climbing shoes',
   'Cone heels',
   'Court shoes',
   'Cowboy boots',
   'Derby shoes',
   'Dress shoe',
   'Flip flop',
   'Golf shoes',
   'High heels',
   'High-tops shoes',
   'Hiking boots',
   'Ice-skates shoes',
   'Kitten heels',
   'Knee high boots', 
   'Laced booties',
   'Lita shoe',
   'Loafer',
   'Mary Jane platforms',
   'Moccasin',
   'Mule shoes',
   'Old skool',
   'Oxford shoe',
   'Platform heels',
   'Running shoes',
   'Sandal',
   'Sneakers ',
   'Soccer shoes',
   'Uggs',
   'Wedges shoe',
   'Wellington boots'
)

model = load_learner('shoes-recognizer-v4.pkl') 

def recognize_image(image):
  pred, idx, probs = model.predict(image)
  print(pred, probs)
  return dict(zip(shoe_labels, map(float, probs))) 

image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label(num_top_classes=5)
examples = [
    'image-01.jpg',
    'image-02.jpg',
    'image-03.jpg',
    'image-06.JPG',
    'image-07.jpg',
    'image-08.jpg',
    'image-09.jpg',
    'image-10.jpg'    
    ]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False)