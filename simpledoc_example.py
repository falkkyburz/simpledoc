from simpledoc import Simpledoc
from pathlib import Path

doc = Simpledoc(Path('simpledoc_example.html'))

doc.put(
'''
Simpledoc
==========

:author: Falk Kyburz
:organization: MyCompany AG
:contact: email@email.com
:version: 0
:date: 2020-09-09
:copyright: Falk Kyburz
:abstract: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

.. sectnum::

.. contents:: Table of Contents

'''
)


doc.put(
'''
Fist Subsection
---------------



Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

.. math::

   \\frac{ \\sum_{t=0}^{N}f(t,k) }{N}

Fist Subsection
---------------

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

Math Test SubSubsection
"""""""""""""""""""""""


.. math::

    \\dot{x} & = \\sigma(y-x) \\\\
    \\dot{y} & = \\rho x - y - xz \\\\
    \\dot{z} & = -\\beta z + xy
    
.. math::

    \\left( \\sum_{k=1}^n a_k b_k \\right)^2 \\leq \\left( \\sum_{k=1}^n a_k^2 \\right) \\left( \\sum_{k=1}^n b_k^2 \\right)


.. math::

    \\mathbf{V}_1 \\times \\mathbf{V}_2 =  \\begin{vmatrix}
    \\mathbf{i} & \\mathbf{j} & \\mathbf{k} \\\\
    \\frac{\\partial X}{\\partial u} &  \\frac{\\partial Y}{\\partial u} & 0 \\\\
    \\frac{\\partial X}{\\partial v} &  \\frac{\\partial Y}{\\partial v} & 0
    \\end{vmatrix}


.. math::

    P(E)   = {n \\choose k} p^k (1-p)^{ n-k}
    
    
.. math::

    \\frac{1}{\\Bigl(\\sqrt{\\phi \\sqrt{5}}-\\phi\\Bigr) e^{\\frac25 \\pi}} =
    1+\\frac{e^{-2\\pi}} {1+\\frac{e^{-4\\pi}} {1+\\frac{e^{-6\\pi}}
    {1+\\frac{e^{-8\\pi}} {1+\\ldots} } } }

.. math::

    1 +  \\frac{q^2}{(1-q)}+\\frac{q^6}{(1-q)(1-q^2)}+\\cdots =
    \\prod_{j=0}^{\\infty}\\frac{1}{(1-q^{5j+2})(1-q^{5j+3})},
    \\quad\\quad \\text{for $|q|<1$}.

.. math::

    \\nabla \\times \\vec{\\mathbf{B}} -\\, \\frac1c\\, \\frac{\\partial\\vec{\\mathbf{E}}}{\\partial t} & = \\frac{4\\pi}{c}\\vec{\\mathbf{j}} \\\\   \\nabla \\cdot \\vec{\\mathbf{E}} & = 4 \\pi \\rho \\\\
    \\nabla \\times \\vec{\\mathbf{E}}\\, +\\, \\frac1c\\, \\frac{\\partial\\vec{\\mathbf{B}}}{\\partial t} & = \\vec{\\mathbf{0}} \\\\
    \\nabla \\cdot \\vec{\\mathbf{B}} & = 0


Code Segments
-------------

.. code:: 
   
    import numpy as np
   
    def foo(test)
        return test + 2
        
Optional if pygments package is installed: Add languager after the code role. For example .. code:: python

Table
-----

.. table:: Caption of the super result table.

    =============== =============== ===============
    Column1 heading Column2 heading Column3 heading
    =============== =============== ===============
    1               2               3
    1               2               3
    1               2               3
    =============== =============== ===============



Inline markup
-------------

The *quick* brown **fox** jumps ``over`` :superscript:`the` lazy
:subscript:`dog`. :title-reference:`Title reference.`

Lorem ipsum [Ref]_ dolor sit amet.

.. [Ref] Book or article reference, URL or whatever.

Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

.. rubric:: Footnotes

.. [#f1] Text of the first footnote.
.. [#f2] Text of the second footnote.

Lists and quote-like blocks
---------------------------

* Bulleted list
* with two items

#. Numbered list
#. with
#. three items

* Nested

  #. List

    * Hooray
    * Hooray
    * Hooray
    * Hooray

  #. List

    * Hooray
    * Hooray
    * Hooray
    * Hooray

* Nested

  #. List


term (up to a line of text)
   Definition of the term, which must be indented

   and can even consist of multiple paragraphs

next term
   Description.

Paragraph heading
"""""""""""""""""

.. contents:: Local table of contents
   :local:

(The above ToC triggers anchors around all page headings beyond what Sphinx
does.)

.. topic:: Topic

  A topic is like a block quote with a title, or a self-contained section with
  no subsections. Use the "topic" directive to indicate a self-contained idea
  that is separate from the flow of the document. Topics may occur anywhere a
  section or transition may occur. Body elements and topics may not contain
  nested topics.

.. parsed-literal::

  parsed-literal is a literal-looking block with **parsed** *text*

Epigraph
^^^^^^^^

.. epigraph::

  No matter where you go, there you are.

  -- Buckaroo Banzai

Compound paragraph
^^^^^^^^^^^^^^^^^^

.. compound::

   This is a compound paragraph. The 'rm' command is very dangerous.  If you
   are logged in as root and enter ::

       cd /
       rm -rf *

   you will erase the entire contents of your file system.

Raw HTML
^^^^^^^^

.. raw:: html

  <span style="color: red;">This is some raw HTML.</span>


Admonition blocks
-----------------

.. attention:: attention block block block block block block block block block
    block block

.. caution:: caution block

.. danger:: danger block

.. error:: error block

.. hint:: hint block

.. important:: important block

.. note:: note block

.. tip:: tip block

.. warning:: warning block

.. admonition:: custom admonition

  with content

'''
)


def docput_in_function():
    doc.put(
    '''
    
    Subsection From Inside A Function
    ---------------------------------
    
    This is a doc inside a function. This is inserted where the function is called!
    
    .. math::
    
        \\mathbf{V}_1 \\mathbf{V}_2 =  \\begin{vmatrix}
        \\mathbf{i} & \\mathbf{j} & \\mathbf{k} \\\\
        \\frac{\\partial X}{\\partial u} &  \\frac{\\partial Y}{\\partial u} & 0 \\\\
        \\frac{\\partial X}{\\partial v} &  \\frac{\\partial Y}{\\partial v} & 0
        \\end{vmatrix}
 
    
    ''')


myresult = 69.6969

doc.put(
f'''
Rsult
-----

The result of my calculation is {myresult}

'''
)


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
  

doc.put(
f'''
Code Test
---------

Inserting code is only possible after the function definition. This is not a manual copy of the code, it's the real deal.

.. code::

{doc.get_code(tri_recursion)}

'''
)  


docput_in_function()

doc.publish_html()

doc.open_html()


