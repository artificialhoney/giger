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

Read more: `https://artificialhoney.github.io/giger <https://artificialhoney.github.io/giger>`_

------------
Installation
------------

.. code:: bash

   pip install giger git+https://github.com/ai-forever/Real-ESRGAN.git

-----
Usage
-----

Please check first of all the help function and the `examples <https://github.com/artificialhoney/giger/tree/main/examples/>`_.

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

Use an inline ``jinja2`` template file and supply data. Write out to file.

.. code:: bash

   giger template --config hero=viking "A {{hero}} with long hair and sword" --output viking.txt

You can also pipe from another command to the template task.

.. code:: bash

   echo "A {{hero}} with long hair and sword" | giger template --config hero=viking  --output viking.txt

prompt
------

Generate a prompt with multiple well-known input keywords to choose.

.. code:: bash

   giger prompt "A viking with long hair and sword" --time "Ancient" --type "Comic Book" --art_style "Concept art" --realism "Photorealistic" --rendering_engine "Octane render" --lightning_style "Cinematic" --camera_position "Ultra-Wide-Angle Shot" --resolution "8k"

You can also pipe from another command to the prompt task.

.. code:: bash

   echo "A viking with long hair and sword" | giger prompt --time "Ancient" --type "Comic Book" --art_style "Concept art" --realism "Photorealistic" --rendering_engine "Octane render" --lightning_style "Cinematic" --camera_position "Ultra-Wide-Angle Shot" --resolution "8k"

image
-----

The commands pull the chosen model from ``huggingface.co``. You choose one with the ``--model`` option. Also the batch and image sizes can be configured and one can pass the prompt via pipe.

Please see the help function for more information.

txt2img
^^^^^^^

.. code:: bash

   giger image "A viking with long hair and sword, Concept art, Photorealistic, Octane render, Cinematic, Ultra-Wide-Angle Shot, 8k" --output $HOME/Desktop/ --name viking

img2img
^^^^^^^

.. code:: bash

   giger image "A viking with long hair and sword, Concept art, Photorealistic, Octane render, Cinematic, Ultra-Wide-Angle Shot, 8k" --output $HOME/Desktop/ --name viking --input input.png

controlnet
^^^^^^^^^^

.. code:: bash

   giger image "A viking with long hair and sword, Concept art, Photorealistic, Octane render, Cinematic, Ultra-Wide-Angle Shot, 8k" --output $HOME/Desktop/ --name viking --input input.png --controlnet_model "lllyasviel/sd-controlnet-hed"

roop
----

Simply change the face in an input image and render the result to disc.

.. code:: bash

   giger roop --face face.jpg --input target.png --output output.png

upscale
-------

Simply upscale an image and render the result to disc.

.. code:: bash

   giger upscale --input image.png --output image@4x.png --scale 4
