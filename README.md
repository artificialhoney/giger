# stable-diffusion-templates

Collection of templates to create stable-diffusion artworks.

## Prerequistes

Make sure you have **stable-diffusion-webui** with the **control-net** extension installed.

## Installation

`pip install -r requirements.txt`


## Usage

To generate prompts with settings for use in Webui try e.g.:

```bash
jinja2 ./templates/death-knights/default.j2 ./data/death-knights/default.yaml > ./out/death-knights.txt
```

or

```bash
jinja2 ./templates/parisienne/default.j2 ./data/parisienne/default.yaml > ./out/parisienne.txt
```

### Death Knights

Take your favorite character with pose, e.g. [assets](./assets/death-knights/valkyrie.png) and input it to a ControlNet unit of type **SoftLine** with weight **0.75**.

**Model:** [Photon](https://civitai.com/models/84728/photon)

### Parisienne

Use a text image of best 4 characters in black font on white background like [assets](./assets/parisienne/pali.png) and input it to a ControlNet unit of type **Depth** with weight **0.5**.
Make sure to invert in preprocessor settings!

Also try to add **Aesthetic Gradients** with same prompt!

**Model:** [DreamShaper](https://civitai.com/models/4384/dreamshaper)

## Docs

### [Prompts](/docs/prompts.md)

## Links

- Webui installation: https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon
- ControlNet installation: https://github.com/Mikubill/sd-webui-controlnet#installation
- Roop extension for face swap: https://github.com/s0md3v/sd-webui-roop
- Aesthetic Gradients extension for mood tweaking: https://github.com/AUTOMATIC1111/stable-diffusion-webui-aesthetic-gradients
- Civitai for models: https://civitai.com/
- Huggingface for models: https://huggingface.co/