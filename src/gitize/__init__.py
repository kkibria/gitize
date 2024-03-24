import os

def get_template_path():
    root = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(root, 'template')
