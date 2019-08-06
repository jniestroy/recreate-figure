#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python3", "data_cleaning.py"]

requirements:
- class: ShellCommandRequirement
- class: DockerRequirement
  dockerImageId: jniestroy/recreate-figure
  dockerPull: jniestroy/recreate-figure

inputs:
  file:
    type: File
    inputBinding:
      position: 1
outputs:
  answer:
    type: stdout
stdout: clean.csv
