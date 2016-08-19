#!/bin/sh

rm -rf ~/.kde/share/apps/kdeconnect/pyext/plugins/*
cp -R * ~/.kde/share/apps/kdeconnect/pyext/plugins

echo "Plugins installed."
