# Letter Generator
This script is used to generate cover letters efficiently.

## Installation
You need `pandoc` and `xelatex` installed on your machine. Also you need a basic `latex` installation that provides you with a `xelatex` engine.

## Usage
Run `python3 letter.py` to generate a new cover letter. A file named `brief.pdf` will appear in the base-directory -- this is the generated cover-letter. You can create new snippets by adding files to the `snippets/` folder. Recipients are stored in `recipients.csv`. If you want to change the way the letter looks, edit `letter.latex`.
