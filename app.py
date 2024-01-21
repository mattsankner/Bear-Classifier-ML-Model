# Import the necessary libraries and modules
import os
from fastbook import *
from fastai.vision.widgets import *
import gradio as gr

# Setup fastbook
from fastbook import setup_book
setup_book()

# Set the key for Bing Image Search API
key = os.environ.get('AZURE_SEARCH_KEY', 'ENTER_YOUR_API_KEY')

# Download images of different types of bears
bear_types = 'polar','grizzly', 'black', 'teddy'
path = Path('bears')


# Create directories for each bear type and download images from Bing Image Search API into respective directories
path.mkdir(parents=True, exist_ok=True)
for o in bear_types:
    dest = (path/o)
    dest.mkdir(exist_ok = True)
    results = search_images_bing(key, f'{o} bear')
    download_images(dest, urls=results.attrgot('contentUrl'))

# Verify images
fns = get_image_files(path)
failed = verify_images(fns)
failed.map(Path.unlink)

# Create DataBlock
bears = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_items=get_image_files,
      splitter=RandomSplitter(valid_pct=0.2, seed=42),
      get_y=parent_label,
      item_tfms=Resize(128)
)

# Modify DataBlock
bears = bears.new(
    item_tfms=RandomResizedCrop(224, min_scale=0.5),
    batch_tfms=aug_transforms()
)

# Create DataLoaders
dls = bears.dataloaders(path)

# Create the Learner
learn = vision_learner(dls, resnet18, metrics=error_rate)

# Train the model
learn.fine_tune(4)

# Export the trained model
model_path = Path('bears')
learn.export(model_path/'export.pkl')
learn_inf = load_learner(model_path/'export.pkl')

# Define a function for the Gradio Interface to use
def classify_image(image):
    pred, pred_idx, probs = learn_inf.predict(image)
    return f'Prediction: {pred}; Probability: {probs[pred_idx]:.04f}'

# Create the Gradio Interface
iface = gr.Interface(
    fn=classify_image,
    inputs=gr.inputs.Image(shape=(224, 224)),
    outputs="text",
    live=True,
    capture_session=True,
)

# Launch the Gradio Interface
iface.launch()

