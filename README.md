<!-- -*- gfm -*- -->

# CS7IS2: Artificial Intelligence Group Project

Homepage: https://github.com/ai-msceteers/assignment2

## Team Members

- Muhammad Talha Bin Ijaz
- Basil Contovounesios
- Fionntán Ó Suibhne
- William O'Sullivan

# Report

## Template

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

## Requirements

- This project prefers the more modern
  [`biblatex`](https://ctan.org/pkg/biblatex) and
  [`biber`](https://ctan.org/pkg/biber) bibliography tools and dialects over
  their still traditional [BibTeX](http://www.bibtex.org) counterparts.  The
  former include more and better-formatted styles OOTB, and have better Unicode
  support.  The main reason to prefer the latter is when submitting to a journal
  that requires it.

- The report is encoded in UTF-8, which requires a modern TeX engine such as
  [LuaTeX](https://ctan.org/pkg/luatex) (recommended) or
  [XeTeX](https://ctan.org/pkg/xetex) (untested), both of which are included in
  the standard [TeX Live](https://www.tug.org/texlive) distribution.

## Recommendations

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

  Then to compile the document `rubik.tex`, just run `latexmk rubik.tex`.

- The [`minted`](https://ctan.org/pkg/minted) package makes it easy to include
  beautifully syntax-highlighted code listings.

  When compiling documents that use `minted`, it is important to specify the
  LaTeX command-line option `--shell-escape`.  Using the `latexmk` example from
  above, the resulting command would be `latexmk --shell-escape rubik.tex`.

- The [`booktabs`](https://ctan.org/pkg/booktabs) package documentation includes
  a nice primer for typesetting beautiful tables, and the
  [`ctable`](https://ctan.org/pkg/ctable) package provides a flexible interface.
