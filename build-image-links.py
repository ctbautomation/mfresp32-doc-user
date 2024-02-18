#!/usr/bin/env python
from __future__ import print_function
import os,sys

path = os.path.dirname(os.path.abspath(__file__))

full_path = os.path.join(path, "source")
full_path = os.path.join(full_path, "images")

files = os.listdir(full_path)
for name in files:
    print(".. image:: /images/" + name)
