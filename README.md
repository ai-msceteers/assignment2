<!-- -*- gfm -*- -->

# CS7IS2: Artificial Intelligence Group Project

Homepage: https://github.com/ai-msceteers/assignment2

## Team Members

- Basil Contovounesios
- William O'Sullivan
- Fionntán Ó Suibhne
- Muhammad Talha Bin Ijaz

# Report

To compile the [`resources/author.tex`](resources/author.tex) template, make
sure the `svproc.cls` document class it uses (included in
[`resources/ProcSci_TeX.zip`](resources/ProcSci_TeX.zip)) is in your local
`TEXMFHOME` directory.  For example, on GNU/Linux:

```console
$ D=~/texmf/tex/latex/svproc/
$ mkdir -p $D
$ unzip resources/ProcSci_TeX.zip -d /tmp/procsci
$ cp /tmp/procsci/styles/svproc.cls $D
```

A few recommendations:

- Automate your LaTeX compilations using a tool such as
  [`latexmk`](https://ctan.org/pkg/latexmk).  It is particularly helpful in
  later stages of the writeup when cross-references and bibliographies are
  involved.

- Prefer the more modern [`biblatex`](https://ctan.org/pkg/biblatex) and
  [`biber`](https://ctan.org/pkg/biber) bibliography tools and dialects over
  their still traditional [BibTeX](http://www.bibtex.org/) counterparts.  The
  former include more and better-formatted styles OOTB, and have better Unicode
  support.  The main reason to prefer the latter is when submitting to a journal
  that requires it.

- The [`minted`](https://ctan.org/pkg/minted) package makes it easy to include
  beautifully syntax-highlighted code listings.

- The [`booktabs`](https://ctan.org/pkg/booktabs) package documentation includes
  a nice primer for typesetting beautiful tables, and the
  [`ctable`](https://ctan.org/pkg/ctable) package provides a flexible interface.
