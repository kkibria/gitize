def get_template_path():
    import os
    root = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(root, 'template')

def set_warnigs_hook():
    import sys
    import warnings
    def on_warn(message, category, filename, lineno, file=None, line=None):
        print(f'Warning: {message}', file=sys.stderr)
    warnings.showwarning = on_warn
