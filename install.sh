#!/bin/bash

cp cor-theming.py $(tutor plugins printroot)/.
cp -r theme-templates $(tutor plugins printroot)/.

tutor config save
tutor images build openedx
tutor local start -d
tutor local do settheme cor-theme