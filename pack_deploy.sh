#!/bin/bash

rm archive.zip
git archive HEAD --format=zip > archive.zip
zip -d archive.zip demo/\*
zip archive.zip theApp/config.py
