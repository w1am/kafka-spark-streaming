#!/bin/sh

rm -rf dist package artifact.zip;
poetry install --only main --sync;
poetry build;
poetry run pip install --upgrade -t package dist/*.whl;
cd package;
zip -r ../artifact.zip . -x '*.pyc';

echo "\n\nDone! Your artifact is in artifact.zip\n\n"