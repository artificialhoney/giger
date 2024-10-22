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

   pip install giger git+https://github.com/ai-forever/Real-ESRGAN.git git+https://github.com/XPixelGroup/BasicSR@master

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

swap
----

Simply change the face in an input image and render the result to disc.

.. code:: bash

   giger swap --face face.jpg --input target.png --output output.png

upscale
-------

Simply upscale an image and render the result to disc.

.. code:: bash

   giger upscale --input image.png --output image@4x.png --scale 4
