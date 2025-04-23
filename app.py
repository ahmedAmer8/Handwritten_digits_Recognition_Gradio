import tensorflow as tf
import gradio as gr
import numpy as np
from PIL import Image, ImageOps

model = tf.keras.models.load_model('mnist_model.h5')

def sketchToNumpy(image):
    if image is None or "composite" not in image:
        return "No image provided"

    im_array = image["composite"]

    pil_img = Image.fromarray(im_array).convert("L")
    pil_img = ImageOps.invert(pil_img)
    pil_img = pil_img.resize((28, 28))

    img_resized = np.array(pil_img).astype("float32") / 255.0

    img_input = img_resized.reshape(1, 28, 28, 1)

    prediction = model.predict(img_input)

    return {str(i): float(prediction[0][i]) for i in range(10)}

demo = gr.Interface(
    fn=sketchToNumpy,
    inputs=gr.Sketchpad(crop_size=(256, 256), type='numpy', image_mode='L'),
    outputs=gr.Label(num_top_classes=10, label="Prediction"),
)

demo.launch(debug=True)
