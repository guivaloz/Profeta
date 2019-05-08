#!/bin/bash

# Ejecutar configuracion local
if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi

# VirtualEnv
. bin/activate
cd Profeta/

echo "+----------------------+"
echo "|  VirtualEnv Profeta  |"
echo "+----------------------+"
echo
profeta --help
echo

# Instrucciones
echo "Pruebe con su archivo CSV..."
echo "  $ cd ~/Descargas/Profeta/"
echo "  $ ls sesaec-direcciones-ip.csv"
echo "  $ profeta --entrada sesaec-direcciones-ip.csv equipos"
echo
