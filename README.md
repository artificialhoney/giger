# stable-diffusion-templates

Collection of templates to create stable-diffusion artworks.

## Prerequistes

Make sure you have **stable-diffusion-webui** with the **control-net** extension installed.

## Installation

1. `brew install gomplate`
2. `git clone git@github.com:artificialhoney/stable-diffusion-templates.git`


## Usage

To generate prompts with settings for use in Webui try e.g.:

```bash
gomplate -d death-knights=./data/death-knights/default.yaml -d parisienne=./data/parisienne/default.yaml
```

### Death Knights

Take your favorite character with pose, e.g. [assets](./assets/death-knights/valkyrie.png) and input it to a ControlNet unit of type **SoftLine** with weight **0.75**.

**Model:** [Photon](https://civitai.com/models/84728/photon)

### Parisienne

Use a text image of best 4 characters in black font on white background like [assets](./assets/parisienne/pali.png) and input it to a ControlNet unit of type **Depth** with weight **0.5**.
Make sure to invert in preprocessor settings!

Also try to add **Aesthetic Gradients** with same prompt!

**Model:** [DreamShaper](https://civitai.com/models/4384/dreamshaper)

## Prompts

![Clipart of Flava Flav](./examples/prompts/Clipart%20of%20Flava%20Flav.png?raw=true)

`Clipart of Flava Flav`, **DreamShaper**, creates an vectorizable clipart.

![Wolpertinger](./examples/prompts/Wolpertinger.png?raw=true)

`Wolpertinger`, **Photon**, creates an photo realistic instance of the [bavarian legend](https://de.wikipedia.org/wiki/Wolpertinger#/media/Datei:Wolpertinger.jpg).

## Links

- Webui installation: https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon
- ControlNet installation: https://github.com/Mikubill/sd-webui-controlnet#installation
- Roop extension for face swap: https://github.com/s0md3v/sd-webui-roop
- Aesthetic Gradients extension for mood tweaking: https://github.com/AUTOMATIC1111/stable-diffusion-webui-aesthetic-gradients
- Civitai for models: https://civitai.com/
- Huggingface for models: https://huggingface.co/