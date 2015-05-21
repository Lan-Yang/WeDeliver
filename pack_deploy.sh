#!/bin/bash
rm archive.zip
git archive HEAD --format=zip > archive.zip
zip archive.zip theApp/config.py
