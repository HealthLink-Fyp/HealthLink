#!/bin/bash
set -e

ng build
mkdir -p dist/health360-front/browser/browser

for item in dist/health360-front/browser/*; do
    if [ "$item" != "dist/health360-front/browser/browser" ]; then
        mv "$item" dist/health360-front/browser/browser/
    fi
done

cd dist/health360-front/browser/browser
touch .nojekyll
cp index.html 404.html
cd ../../../../
printf 'current directory is: ' && pwd
ng deploy --no-build