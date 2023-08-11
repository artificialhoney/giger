.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/giger.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/giger
    .. image:: https://readthedocs.org/projects/giger/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://giger.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/giger/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/giger
    .. image:: https://img.shields.io/pypi/v/giger.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/giger/
    .. image:: https://img.shields.io/conda/vn/conda-forge/giger.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/giger
    .. image:: https://pepy.tech/badge/giger/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/giger
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/giger

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/


giger
==

CLI for Stable Diffusion tasks.

Installation
------------

.. code:: bash

   pip install giger
   activate-global-python-argcomplete
   echo 'eval "$(register-python-argcomplete giger)"' >> ~./zshrc

CLI
---

template
~~~~~~~~

.. code:: bash

   giger template -c type=Viking  -d data/hero.yaml "$(cat templates/hero.j2)"

prompt
~~~~~~

.. code:: bash

   giger prompt "Spawn in a battle" --time "ancient" --type "Comic Book" --background_color "#000000" --art_style "Concept art" --realism "Photorealistic" --rendering_engine "Octane render" --lightning_style "Cinematic" --camera_position "Ultra-Wide-Angle Shot" --resolution "8k" 

image
~~~~~

.. code:: bash

   giger image "Comic Book of Spawn in a battle, Concept art, Photorealistic, Octane render, Cinematic, Ultra-Wide-Angle Shot, 8k" --output $HOME/Desktop/ --name spawn

or e.g.

.. code:: bash

   giger image "$(giger prompt "Spawn in a battle" --time "ancient" --type "Comic Book" --background_color "#000000" --art_style "Concept art" --realism "Photorealistic" --rendering_engine "Octane render" --lightning_style "Cinematic" --camera_position "Ultra-Wide-Angle Shot" --resolution "8k")" --output $HOME/Desktop/ --name spawn

.. code:: bash

   prompt="a wall with graffiti on it, with text Seen, in the art of Seen, located in New York City"
   echo "$prompt" | giger image --output $(pwd)/out/batch --name graffiti --input $(pwd)/assets/img/sketch.png --controlnet_model "lllyasviel/giger-controlnet-hed"
   echo "$prompt" | giger image --output $(pwd)/out/batch --name graffiti --input $(pwd)/assets/img/sketch.png
   echo "$prompt" | giger image --output $(pwd)/out/batch --name graffiti

roop
~~~~

.. code:: bash

   giger roop --source face.jpg --input target.png --output output.png