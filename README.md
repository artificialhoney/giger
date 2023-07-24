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

### Parisienne

Use a text image of best 4 characters in black font on white background like [assets](./assets/parisienne/pali.png) and input it to a ControlNet unit of type **Depth** with weight **0.5**.
Make sure to invert in preprocessor settings!