import os
import sys
import subprocess
import json

def parse_stdout(stdout):
    start = 0
    count = 0
    check = 0
    output = ''
    for element in stdout:
        if element == '{':
            start = 1
            count = count + 1
        if start == 1:
            #new lines were causing problems and
            #not removable with replace
            if element == '\\':
                check = 1
                continue
            if element == 'n' and check == 1:
                check = 0
                continue
            output = output + element
        if element == '}':
            count = count - 1
            if count == 0:
                start = 0
    #output = output.strip('\n')
    return(json.loads(str(output)))


def run_workflow(inputs):
    if len(inputs) >= 4:
        path = inputs[3]
    else:
        path = ''
    wf_metadata =
    workflow = path + inputs[1]
    yaml = path + inputs[2]
    cmd = 'cwltool'
    out = subprocess.Popen([cmd,workflow,yaml],
               stdout=subprocess.PIPE,
               stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()

    if 'Final process status is success' in str(stdout):
        output = parse_stdout(str(stdout))
        print(output)
    else:
        print("Failure: " + stderr)


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        run_workflow(sys.argv)
    else:
        print("Not enough inputs given to run workflow")
