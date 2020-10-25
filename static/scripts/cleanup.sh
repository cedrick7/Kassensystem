#!/bin/bash
echo "Backup wird bereinigt!"
rm ./static/backups/$1/sql.dumb
rmdir ./static/backups/$1

