.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/sd.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/sd
    .. image:: https://readthedocs.org/projects/sd/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://sd.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/sd/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/sd
    .. image:: https://img.shields.io/pypi/v/sd.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/sd/
    .. image:: https://img.shields.io/conda/vn/conda-forge/sd.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/sd
    .. image:: https://pepy.tech/badge/sd/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/sd
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/sd

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/


sd
==

CLI for Stable Diffusion tasks.

Installation
------------

.. code:: bash

   pip install sd
   activate-global-python-argcomplete
   echo 'eval "$(register-python-argcomplete sd)"' >> ~./zshrc

CLI
---

template
~~~~~~~~

.. code:: bash

   sd template -c type=Viking  -d data/hero.yaml "$(cat templates/hero.j2)"

prompt
~~~~~~

.. code:: bash

   sd prompt "Spawn in a battle" --time "ancient" --type "Comic Book" --background_color "#000000" --art_style "Concept art" --realism "Photorealistic" --rendering_engine "Octane render" --lightning_style "Cinematic" --camera_position "Ultra-Wide-Angle Shot" --resolution "8k" 

image
~~~~~

.. code:: bash

   sd image "Comic Book of Spawn in a battle, Concept art, Photorealistic, Octane render, Cinematic, Ultra-Wide-Angle Shot, 8k" --output $HOME/Desktop/ --name spawn

or e.g.

.. code:: bash

   sd image "$(sd prompt "Spawn in a battle" --time "ancient" --type "Comic Book" --background_color "#000000" --art_style "Concept art" --realism "Photorealistic" --rendering_engine "Octane render" --lightning_style "Cinematic" --camera_position "Ultra-Wide-Angle Shot" --resolution "8k")" --output $HOME/Desktop/ --name spawn

.. code:: bash

   prompt="a wall with graffiti on it, with text Seen, in the art of Seen, located in New York City"
   echo "$prompt" | sd image --output $(pwd)/out/batch --name graffiti --input $(pwd)/assets/img/sketch.png --controlnet_model "lllyasviel/sd-controlnet-hed"
   echo "$prompt" | sd image --output $(pwd)/out/batch --name graffiti --input $(pwd)/assets/img/sketch.png
   echo "$prompt" | sd image --output $(pwd)/out/batch --name graffiti

roop
~~~~

.. code:: bash

   sd roop --source face.jpg --input target.png --output output.png