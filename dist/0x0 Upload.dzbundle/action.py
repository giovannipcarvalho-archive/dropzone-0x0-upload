# Dropzone Action Info
# Name: 0x0 Upload
# Description: Upload dragged file to 0x0.st
# Handles: Files
# Creator: Giovanni Paolo
# URL: @giovannipaolo_
# Events: Dragged
# RunsSandboxed: No
# Version: 1.0
# MinDropzoneVersion: 3.5

import time
import subprocess

def dragged():
    dz.begin("Uploading file...")

    dz.determinate(False)

    FILE = items[0]

    bash = "curl -F 'file=@"+FILE+"' https://0x0.st"
    
    process = subprocess.Popen(bash, shell=True, executable='/bin/bash', stdout=subprocess.PIPE)
    result = process.communicate()[0].rstrip()

    dz.finish("File uploaded. URL on clipboard.")

    dz.url(result)