# Sphynx project template

[Sphynx](https://www.sphinx-doc.org/en/master/) project template using [vscode dev containers](https://code.visualstudio.com/docs/remote/containers)

![dev containers](_static/arq.svg)

## REQUIREMENTS
Visual Studio Code Dev Containers: <https://code.visualstudio.com/docs/devcontainers/containers#_system-requirements>

## DEVELOPMENT

VScode -> Terminal -> Run Task... -> "Start sphinx autobuild"

http://127.0.0.1:8000/

### BUILD

set SPHINXOPTS=-D language=de
set SPHINXOPTS=-D language=en

make html
make rinoh
make latexpdf

make gettext
sphinx-intl update -p build/gettext -l en -l de