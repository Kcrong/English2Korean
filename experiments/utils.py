from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

def viz_model(model):
    SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))