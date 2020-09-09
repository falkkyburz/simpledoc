from docutils.core import publish_string
from pathlib import Path
import webbrowser
import textwrap
import inspect


# https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html

class Simpledoc:
    
    def __init__(self, path=Path('doc.html')):
        self.text = ''
        self.path = path
        
    def publish_html(self):
        with self.path.open('w', encoding="utf-8") as f:
            print(publish_string(self.text, writer_name='html5',
                                 settings_overrides={'math_output':'mathjax https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js'}).decode("utf-8"), 
                  file=f)
       
    def put(self, text):
        self.text += textwrap.dedent(text)
        
    def open_html(self):
        webbrowser.open(self.path.resolve().as_uri())


    def get_code(self, function):
        return textwrap.indent(inspect.getsource(function), '    ')

