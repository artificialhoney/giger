=====
giger
=====

.. image:: https://img.shields.io/pypi/v/giger.svg
    :alt: PyPI-Server
    :target: https://pypi.org/project/giger/
.. image:: https://pepy.tech/badge/giger/month
    :alt: Monthly Downloads
    :target: https://pepy.tech/project/giger
.. image:: https://github.com/artificialhoney/giger/actions/workflows/test.yml/badge.svg
   :alt: Test
   :target: https://github.com/artificialhoney/giger/actions/workflows/test.yml
.. image:: https://img.shields.io/coveralls/github/artificialhoney/giger/main.svg
    :alt: Coveralls
    :target: https://coveralls.io/r/artificialhoney/giger
.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :alt: License MIT
    :target: https://opensource.org/licenses/MIT
.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

CLI for Stable Diffusion tasks.

------------
Installation
------------

.. code:: bash

   pip install giger
   activate-global-python-argcomplete
   echo 'eval "$(register-python-argcomplete giger)"' >> ~./zshrc


-----
Usage
-----

template
--------

.. code:: bash

   giger template -c type=Viking  -d data/hero.yaml "$(cat templates/hero.j2)"

prompt
------

.. code:: bash

   giger prompt "Spawn in a battle" --time "ancient" --type "Comic Book" --background_color "#000000" --art_style "Concept art" --realism "Photorealistic" --rendering_engine "Octane render" --lightning_style "Cinematic" --camera_position "Ultra-Wide-Angle Shot" --resolution "8k"

image
-----

.. code:: bash

   giger image "Comic Book of Spawn in a battle, Concept art, Photorealistic, Octane render, Cinematic, Ultra-Wide-Angle Shot, 8k" --output $HOME/Desktop/ --name spawn

or e.g.

.. code:: bash

   giger image "$(giger prompt "Spawn in a battle" --time "ancient" --type "Comic Book" --background_color "#000000" --art_style "Concept art" --realism "Photorealistic" --rendering_engine "Octane render" --lightning_style "Cinematic" --camera_position "Ultra-Wide-Angle Shot" --resolution "8k")" --output $HOME/Desktop/ --name spawn

.. code:: bash

   prompt="a wall with graffiti on it, with text Seen, in the art of Seen, located in New York City"
   echo "$prompt" | giger image --output $(pwd)/out/batch --name graffiti --input $(pwd)/assets/img/sketch.png --controlnet_model "lllyasviel/sd-controlnet-hed"
   echo "$prompt" | giger image --output $(pwd)/out/batch --name graffiti --input $(pwd)/assets/img/sketch.png
   echo "$prompt" | giger image --output $(pwd)/out/batch --name graffiti

roop
----

.. code:: bash

   giger roop --source face.jpg --input target.png --output output.png
