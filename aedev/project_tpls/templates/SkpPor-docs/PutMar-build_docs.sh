# build Sphinx documentation (run in docs/ folder)
rm -rf _autosummary
rm -rf _build
python -m sphinx -v -T -b html -d _build/doctrees -D language=en . _build/html
