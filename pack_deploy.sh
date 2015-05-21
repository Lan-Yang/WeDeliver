#!/bin/bash
git archive HEAD --format=zip > archive.zip
zip archive.zip theApp/config.py
