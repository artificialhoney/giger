# sd

CLI for Stable Diffusion tasks.

## Installation


```bash
pip install -r requirements.txt
pip install -e .
activate-global-python-argcomplete
echo 'eval "$(register-python-argcomplete sd)"' >> ~./zshrc
```

## CLI

### template

```bash
sd template -c type=Viking  -d data/hero.yaml "$(cat templates/hero.j2)"
```

### prompt

```bash
sd prompt "Spawn in a battle" --time "ancient" --type "Comic Book" --background_color "#000000" --art_style "Concept art" --realism "Photorealistic" --rendering_engine "Octane render" --lightning_style "Cinematic" --camera_position "Ultra-Wide-Angle Shot" --resolution "8k" 
```

### image

```bash
sd image "Comic Book of Spawn in a battle, Concept art, Photorealistic, Octane render, Cinematic, Ultra-Wide-Angle Shot, 8k" --output $HOME/Desktop/ --name spawn
```

or e.g.

```bash
sd image "$(sd prompt "Spawn in a battle" --time "ancient" --type "Comic Book" --background_color "#000000" --art_style "Concept art" --realism "Photorealistic" --rendering_engine "Octane render" --lightning_style "Cinematic" --camera_position "Ultra-Wide-Angle Shot" --resolution "8k")" --output $HOME/Desktop/ --name spawn
```

```bash
prompt="a wall with graffiti on it, with text Seen, in the art of Seen, located in New York City"
echo "$prompt" | sd image --output $(pwd)/out/batch --name graffiti --input $(pwd)/assets/img/sketch.png --controlnet_model "lllyasviel/sd-controlnet-hed"
echo "$prompt" | sd image --output $(pwd)/out/batch --name graffiti --input $(pwd)/assets/img/sketch.png
echo "$prompt" | sd image --output $(pwd)/out/batch --name graffiti
```

### roop

```bash
sd roop --source face.jpg --input target.png --output output.png
```

## Templates

### Hero

Take your favorite character with pose and input it to a ControlNet unit of type **SoftLine** with weight **0.75**.

**Model:** [Photon](https://civitai.com/models/84728/photon)

To generate prompts with settings for use in Webui try e.g.:

```bash
sd template -t templates/hero.j2 -d data/hero.yaml
```

### Graffiti

Use a text image of best 4 characters in black font on white background and input it to a ControlNet unit of type **Depth** with weight **0.5**.
Make sure to invert in preprocessor settings!

Also try to add **Aesthetic Gradients** with same prompt!

**Model:** [DreamShaper](https://civitai.com/models/4384/dreamshaper)

```bash
sd template -t templates/graffiti.j2 -d data/graffiti.yaml
```

## Docs

### [Prompts](/docs/prompts.md)

## Links

- Webui installation: https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon
- ControlNet installation: https://github.com/Mikubill/sd-webui-controlnet#installation
- Roop extension for face swap: https://github.com/s0md3v/sd-webui-roop
- Aesthetic Gradients extension for mood tweaking: https://github.com/AUTOMATIC1111/stable-diffusion-webui-aesthetic-gradients
- Civitai for models: https://civitai.com/
- Huggingface for models: https://huggingface.co/