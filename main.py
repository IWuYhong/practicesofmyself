import os
import zipfile

ruta = os.getcwd()

mi_zip = zipfile.ZipFile("proyecto", "r")
mi_zip.extractall()