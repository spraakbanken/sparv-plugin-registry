# sparv-plugin-registry

This repository serves as a central registry for Sparv Pipeline plugins.

## Manifest files
A manifest file is a YAML file containing metadata about a Sparv plugin. Manifest files are validated agains a JSON
schema. Each manifest contains mandatory and optional main properties as described below and a list of versions (at
least one version must be specified).

Main properties:
- `name` (required): The name of the Sparv plugin
- `description` (required): A short description of the plugin
- `long_description`: An optional long description of the plugin
- `source` (required): A URL pointing to the source code of the plugin
- `author` (required): Name of the author of the plugin (may be an organisation)
- `author_email` (required): E-mail address of the author
- `license` (required): Name of the license for the plugin
- `python_requires` (required): Python version required for running the plugin
- `requires_additional_installs` (required): Boolean stating whether it is necessary to install additional software in
  order to run this plugin
- `platforms`: An optional list of platforms (operating systems) where this plugin and its tools can be run
- `languages`: An optional list of language codes defining what languages the plugin can be used for
- `versions` (required): A list of version objects (each containing version properties as described below) where each
  objects describes one version of the plugin.

Version properties:
- `version` (required): The version of the plugin
- `install_pointer` (required): Pointer installation with pip (name of the package on PyPI or a reference to a GitHub
  repository)
- `sparv_pipeline_requires` (required): Sparv Pipeline version required for running the plugin
- Any of the above listed main properties may be overridden by including them in a version object.


## Installation
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the validation
```
cd validation
python validate.py
```
