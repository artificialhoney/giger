=====
giger
=====

.. image:: https://img.shields.io/pypi/v/giger.svg
    :alt: PyPI-Server
    :target: https://pypi.org/project/giger/
.. image:: https://static.pepy.tech/badge/giger/month
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

-----
Usage
-----

Please check first of all the help function.

.. code-block:: bash

    giger --help

Also make sure to always obtain the latest version.

.. code-block:: bash

    giger --version

Increase verbosity to also output the ``diffusers`` logging.

.. code-block:: bash

    giger -vv


template
--------

Use a ``jinja2`` template file and supply data from file. Overwrite variables and print out to console.

.. code:: bash

   giger template --config hero=viking --data hero.yml "$(cat hero.txt.j2)"

Use an inline ``jinja2`` template file and supply data. Write out to file

.. code:: bash

   giger template --config hero=viking "A {{hero}} with long hair and sword" --output viking.txt


prompt
------

Generate a prompt with multiple well-known input keywords to choose.

.. code:: bash

   giger prompt "Spawn in a battle" --time "Ancient" --type "Comic Book" --art_style "Concept art" --realism "Photorealistic" --rendering_engine "Octane render" --lightning_style "Cinematic" --camera_position "Ultra-Wide-Angle Shot" --resolution "8k"

image
-----

.. code:: bash

   giger image "Comic Book of Spawn in a battle, Concept art, Photorealistic, Octane render, Cinematic, Ultra-Wide-Angle Shot, 8k" --output $HOME/Desktop/ --name spawn

or e.g.

.. code:: bash

   giger image "$(giger prompt "Spawn in a battle" --time "ancient" --type "Comic Book" --art_style "Concept art" --realism "Photorealistic" --rendering_engine "Octane render" --lightning_style "Cinematic" --camera_position "Ultra-Wide-Angle Shot" --resolution "8k")" --output $HOME/Desktop/ --name spawn

.. code:: bash

   prompt="a wall with graffiti on it, with text Seen, in the art of Seen, located in New York City"
   echo "$prompt" | giger image --output $(pwd)/out/batch --name graffiti --input $(pwd)/assets/img/sketch.png --controlnet_model "lllyasviel/sd-controlnet-hed"
   echo "$prompt" | giger image --output $(pwd)/out/batch --name graffiti --input $(pwd)/assets/img/sketch.png
   echo "$prompt" | giger image --output $(pwd)/out/batch --name graffiti

roop
----

Simply change the face in an input image and render the result to disc.

.. code:: bash

   giger roop --face face.jpg --input target.png --output output.png
