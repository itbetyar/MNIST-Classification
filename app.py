###############################################
##   IT Betyar - A.I. Developer tanfolyam
##
##   https://itbetyar.hu/mesterseges-intelligencia-fejleszto-tanfolyam/
##
##   Gradio MNIST - Képpel - Mintákkal

import gradio as gr
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('mnist.keras') # a modell betoltese

def preprocess_image(img):     # Potenciális RGB 2 gray konverzió
    if len(img.shape) == 3 and img.shape[-1] == 3: # ha szines
        img = tf.image.rgb_to_grayscale(img).numpy().squeeze() 
        # hatekony gray conv. > np array lesz belőle

    img = tf.image.resize(img[None, ..., None], (28, 28)).numpy().squeeze() # resize
    # dimenziót is váltogatunk, a tf.image.resizenak kell ez

    if img.mean() > 127: # szin invert
        img = 255 - img

    img = img.astype('float32') / 255.0  # Normalizál
    img = img.reshape(784)  # Flatten the image

    return img

def predict_digit(img):      # Predict the digit in the image
    processed_img = preprocess_image(img)
    processed_img = np.expand_dims(processed_img, axis=0)  # Add batch dimension
    prediction = model.predict(processed_img)[0]
    return {str(i): float(prediction[i]) for i in range(10)} # Gradio comaptible kiiras

## Fonti a mukodteto funkcio kodok
## Alabb a Gradio interface resz

# HTML for the header
header_html = """
<div style="max-width: 900px; margin: 0 auto; text-align: center;">
    <div style="display: flex; justify-content: center; align-items: center;">
        <div style="flex: 1; text-align: center;">
            <img src="https://huggingface.co/spaces/itbetyar/MNISTClassifier/resolve/main/mnist_img.webp" alt="Header Image" style="max-width: 100%; height: auto; margin: 20px;">
        </div>
        <div style="flex: 1; padding-left: 30px; text-align: left;">
            <h1 style="color: #8397aa; font-size: 3em;">MNIST Digit Recognition</h1>
            <h3 style="color: #7CE0E1; font-size: 1.8em;">by itbetyar.hu</h3>
        </div>
    </div>
    <div style="text-align: center; background-color: #1b2428; border-radius: 10px;">
        <p style="color: #FFFFFF; padding: 5px; font-size: 1.2em; margin-top: 0px;">
        <a href="https://itbetyar.hu/mesterseges-intelligencia-fejleszto-tanfolyam/">A.I. Developer tanfolyam minta anyag</a><br>
            Tölts fel egy kézzel írott szám képet (0-9) vagy használd alábbi mintákat!<br>
            A modell megállapítja melyik szám az.
        </p>
    </div>
</div>
"""

footer_html = """
<div style="max-width: 900px; margin: 0 auto; text-align: center;">
<h3 style="color: #7CE0E1; font-size: 1.8em; margin-top: 70px;">Leírás:</h3>
<p style="font-size: 1.3em;">
Fenti anyagunk az <a href="https://itbetyar.hu/mesterseges-intelligencia-fejleszto-tanfolyam/">A.I. Developer tanfolyamunk</a> egy minta anyaga. Az MNIST Digit Classifikáció minden A.I. és Machine learining tanfolyam alap modellje, anyaga. Egy remek kezdő projekt.
</p>
<p style="padding: 5px; font-size: 1.3em; margin-top: 0px;">
A lényege -mint azt fent láthatod- hogy <b>60,000 kézzel írt számkarakter</b> alapján, a diákok feltanítanak egy A.I. modellt. Miután készen van, a modell képes kézzel írt számok felismerésére
</p>
</div>
"""

with open("styles.css", "r") as file:
    custom_css = file.read()  # Read the external CSS file

# Gradio interface with header and layout
with gr.Blocks(css=custom_css) as ablakom:
    with gr.Column(elem_id="main-container"):
      gr.HTML(header_html)  # Add the header HTML block

    
      with gr.Row():
            with gr.Column(scale=1):
                input_image = gr.Image(type="numpy", label="Tölts fel egy képet...", height=210, width=350, sources=["upload"])
                
    
                with gr.Row():
                    clear_btn = gr.Button("Reset")
                    classify_btn = gr.Button("Mehet", elem_classes="custom-button")
    
                examples = gr.Examples(
                examples=["imgs/itbtest1.jpg", "imgs/itbtest3.jpg", "imgs/itbtest4.jpg", "imgs/itbtest5.jpg", "imgs/itbtest6.jpg"],
                inputs=input_image,
                label="Minták"
                )
            
            with gr.Column(scale=1):
                output = gr.Label(num_top_classes=3, label="A feltöltött számjegy:")

    with gr.Column():
        gr.HTML(footer_html)

    # Button actions
    classify_btn.click(predict_digit, inputs=input_image, outputs=output)
    clear_btn.click(lambda: [None, None], inputs=None, outputs=[input_image, output])

ablakom.launch() # az interface inditasa


##   IT Betyar - A.I. Developer tanfolyam
##
##   https://itbetyar.hu/mesterseges-intelligencia-fejleszto-tanfolyam/
##
##   Gradio MNIST - Képpel - Mintákkal
########################################################################