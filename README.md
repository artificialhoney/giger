# stable-diffusion-templates

Collection of templates to create stable-diffusion artworks.

## Prerequistes

Make sure you have **stable-diffusion-webui** with the **control-net** extension installed.

## Installation

`pip install -r requirements.txt`
`pip install -e .`

## CLI

### template

```bash
python -m stable_diffusion_templates.skeleton template -c type=Viking  -d data/hero.yaml "$(cat templates/hero.j2)"
```

### prompt

```bash
python -m stable_diffusion_templates.skeleton prompt "Spawn in a battle" --time "ancient" --type "Comic Book" --background_color "#000000" --art_style "Concept art" --realism "Photorealistic" --rendering_engine "Octane render" --lightning_style "Cinematic" --camera_position "Ultra-Wide-Angle Shot" --resolution "8k" 
```

### txt2img

```bash
python -m stable_diffusion_templates.skeleton txt2img "Comic Book of Spawn in a battle, Concept art, Photorealistic, Octane render, Cinematic, Ultra-Wide-Angle Shot, 8k" --output $HOME/Desktop/ --name spawn
```

or e.g.

```bash
python -m stable_diffusion_templates.skeleton txt2img "$(python -m stable_diffusion_templates.skeleton prompt "Spawn in a battle" --time "ancient" --type "Comic Book" --background_color "#000000" --art_style "Concept art" --realism "Photorealistic" --rendering_engine "Octane render" --lightning_style "Cinematic" --camera_position "Ultra-Wide-Angle Shot" --resolution "8k")" --output $HOME/Desktop/ --name spawn
```

## Templates

### Hero

Take your favorite character with pose, e.g. [assets](./assets/hero/valkyrie.png) and input it to a ControlNet unit of type **SoftLine** with weight **0.75**.

**Model:** [Photon](https://civitai.com/models/84728/photon)

To generate prompts with settings for use in Webui try e.g.:

```bash
python -m stable_diffusion_templates.skeleton template -t templates/hero.j2 -d data/hero.yaml
```

### Graffiti

Use a text image of best 4 characters in black font on white background like [assets](./assets/parisienne/pali.png) and input it to a ControlNet unit of type **Depth** with weight **0.5**.
Make sure to invert in preprocessor settings!

Also try to add **Aesthetic Gradients** with same prompt!

**Model:** [DreamShaper](https://civitai.com/models/4384/dreamshaper)

```bash
python -m stable_diffusion_templates.skeleton template -t templates/graffiti.j2 -d data/graffiti.yaml
```

## Notebooks

Start jupyter lab with `jupyter lab` for editing.

### Graffiti

See [create_lora.ipynb](./notebooks/graffiti/create_lora.ipynb), which you can run in Google Colab.

## Docs

### [Prompts](/docs/prompts.md)

## Links

- Local Jupyter instance: http://localhost:8888/
- Webui installation: https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon
- ControlNet installation: https://github.com/Mikubill/sd-webui-controlnet#installation
- Roop extension for face swap: https://github.com/s0md3v/sd-webui-roop
- Aesthetic Gradients extension for mood tweaking: https://github.com/AUTOMATIC1111/stable-diffusion-webui-aesthetic-gradients
- Civitai for models: https://civitai.com/
- Huggingface for models: https://huggingface.co/