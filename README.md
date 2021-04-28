<!-- -*- gfm -*- -->

# CS7IS2: Artificial Intelligence Group Project

Repositories:

* https://github.com/ai-msceteers/assignment2
* https://github.com/ai-msceteers/DeepCubeA

See [`readme.txt`](readme.txt) for more information on the group and the
project's repositories.

The minutes of each group meeting are kept in reverse chronological order in the
file [`minutes.md`](minutes.md).

Auxiliary notes for the project are kept in the file [`notes.md`](notes.md).

# Documentation

## Presentation

The slides for the presentation are in
[`doc/presentation.pdf`](doc/presentation.pdf), and their source in
[`doc/presentation.tex`](doc/presentation.tex).  A link to the video recording
of the presentation, accessible by TCD accounts, is included in the project
report.

## Report

The output of this project is the technical report
[`doc/report.pdf`](doc/report.pdf).  Its source can be found in the file
[`doc/report.tex`](doc/report.tex), which follows the given template in
[`resources/author.tex`](resources/author.tex).  The Biblatex bibliography
database for all documentation is in [`doc/rubik.bib`](doc/rubik.bib).

### Template

The [`resources/author.tex`](resources/author.tex) template is distributed with
the Springer-Verlag TeX bundle
[`resources/ProcSci_TeX.zip`](resources/ProcSci_TeX.zip).  It requires
installing the included `svproc.cls` document class in the standard TeX inputs
locations, or in the same directory as the TeX document using it.

### Requirements

- This project prefers the more modern
  [`biblatex`](https://ctan.org/pkg/biblatex) and
  [`biber`](https://ctan.org/pkg/biber) bibliography tools and dialects over
  their still traditional [BibTeX](http://www.bibtex.org) counterparts.  The
  former include more and better-formatted styles OOTB, and have better Unicode
  support.  The main reason to prefer the latter is when conforming to a style
  that requires it.

- The report is encoded in UTF-8, which requires a modern TeX engine such as
  [LuaTeX](https://ctan.org/pkg/luatex) (recommended) or
  [XeTeX](https://ctan.org/pkg/xetex) (untested), both of which are included in
  the standard [TeX Live](https://www.tug.org/texlive) distribution.

### Recommendations

- Automate your LaTeX compilations using a tool such as
  [`latexmk`](https://ctan.org/pkg/latexmk).  It is particularly helpful in
  later stages of the writeup when cross-references and bibliographies are
  involved.

  To configure `latexmk` to use LuaLaTeX, for example, add the following to your
  `~/.latexmkrc` file:

  ```perl
  # Use LuaLaTeX
  $pdf_mode = 4;
  ```

  Then to compile the document [`report.tex`](doc/report.tex), just run `latexmk
  report.tex`.

- The [`minted`](https://ctan.org/pkg/minted) package makes it easy to include
  beautifully syntax-highlighted code listings.

  When compiling documents that use `minted`, it is important to specify the
  LaTeX command-line option `--shell-escape`.  Using the `latexmk` example from
  above, the resulting command would be `latexmk --shell-escape report.tex`.

- The [`booktabs`](https://ctan.org/pkg/booktabs) package documentation includes
  a nice primer for typesetting beautiful tables, and the
  [`ctable`](https://ctan.org/pkg/ctable) package provides a flexible interface.
