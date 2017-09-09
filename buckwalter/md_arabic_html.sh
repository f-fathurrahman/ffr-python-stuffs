#!/bin/bash

TEMP_MD="pre.md"

pushd `dirname $0` > /dev/null
SCRIPTPATH=`pwd -P`
popd > /dev/null

python3 $SCRIPTPATH/preproc_buckwalter.py "$1" > $TEMP_MD

python -m markdown $TEMP_MD > tmp

cat << EOF
<!DOCTYPE html>
<html lang="en">

<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ffr&#39;s pages</title>
<meta name="description" content="Some description">
<style>
  body {
    font-size: 23pt;
  }
  .arabic {
    font-family: me_quran;
    font-size: 32pt;
  }
  .arabicPar {
    font-family: me_quran;
    font-size: 32pt;
    text-align: right;
  }
  .new-style {
    font-style: italic;
    text-decoration: overline;
    color: gray;
  }
</style>
</head>

<body>
EOF

# or use the following link:
# https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML

cat tmp
echo "</body>"
echo "</html>"

rm $TEMP_MD
rm tmp
