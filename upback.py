#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import os
from shutil import make_archive
from datetime import date

currdate = date.today().strftime("%d_%m_%Y")

rootdir, archive_dir = list(
    map(lambda x: x.rstrip(), open("config.txt").readlines()))

modtime_file = open("dirs_last_modtime.txt", "r+")
modtime_lines = modtime_file.readlines()

# Архивирует все папки верхнего уровня(Работа, моделинг и т.д.),
# в которых были совершены изменения.
def archivate_changed_folders():
    for dirname in os.listdir(rootdir):
        dirpath = rootdir + dirname

        if dirname.startswith(".") or not os.path.isdir(dirpath):
            continue

        check_last_modtime(dirpath)


def archivate_dir(dirpath):
    dirname = dirpath.split("\\")[-1]
    archive_name = "{}_{}".format(dirname, currdate)
    archive_path = archive_dir + archive_name

    print("archivating " + dirname)

    make_archive(
        archive_path,       # Название файла
        'zip',              # Формат архива
        root_dir=dirpath)   # Директория сохранения архива


def check_last_modtime(dirpath):
    element_index = find_line_startswith(dirpath)

    if element_index == None:
        modtime_file.write("{} | {}\n".format(
            dirpath, os.path.getmtime(dirpath)))
        return

    old_modtime = modtime_lines[element_index].split()[-1]

    if old_modtime != str(os.path.getmtime(dirpath)):
        archivate_dir(dirpath)


def find_line_startswith(startswith_str):
    for line in modtime_lines:
        if line.startswith(startswith_str):
            return modtime_lines.index(line)


archivate_changed_folders()

modtime_file.close()
