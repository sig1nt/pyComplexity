from __future__ import print_function
from . import config
import zipfile, os, re, subprocess, glob, math

complexity = "/usr/local/bin/complexity"

def getRatio(scores):
    sorted_s = sorted(scores)
    quart_size = len(sorted_s)/4.0
    quart = None

    frac = quart_size - math.floor(quart_size)
    quart = float(sum(sorted_s[-int(quart_size):]))

    #TODO Add in the logic for non-4-divisible score lengths

    return quart/sum(scores)

def buildFile(user, bracket, asgn):

    # Filter out non-zip files
    zip_filename = list(filter(lambda z: re.search("^\w+\.zip", z),
                               os.listdir(os.getcwd())))

    if(len(zip_filename) != 1):
        print("Skipping {} in {}: Found {} zip files".format(user,
                                                             bracket,
                                                             len(zip_filename)))
        return
    else:
        zip_filename = os.path.join(os.getcwd(), zip_filename[0])

    # extract the project
    try:
        with zipfile.ZipFile(zip_filename, 'r') as handle:
            handle.extractall(os.getcwd())
    except:
        print("Skipping {} in {}: Extraction Failed".format(user, bracket))
        return

    # run complexity on the files
    args = [complexity, "-t0", "-s1"] + glob.glob("*.c")
    proc = subprocess.Popen(args,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE)
    proc.wait()
    out, err = proc.communicate()

    if err.decode('utf-8') != '':
        print("Skipping {} in {}: Complexity Failed".format(user, bracket))
        print(err)
        return

    # Break out scores and get calculations
    lines = out.decode('utf-8').split("\n")[2:-2] # Cut off the begining and end non-scores
    scores = [int(x.split()[0]) for x in lines]

    s_sum = sum(scores)
    s_avg = s_sum / len(scores)
    s_max = max(scores)
    s_ratio = getRatio(scores)

    # Build input for the template
    template = [user, asgn]
    user_data = [s_sum, s_avg, s_max, s_ratio]
    ref_data = [config.REF_SUM, config.REF_AVG, config.REF_MAX, config.REF_RAT]
    overall_score = 0

    for i in range(len(user_data)):
        template.append(user_data[i])
        template.append(ref_data[i])
        template.append(min(ref_data[i]/float(user_data[i]), 1) * 100)
        overall_score += template[-1]

    final_score = overall_score/len(user_data) * (float(bracket)/100)
    template.append(final_score)

    with open("score.txt", "w") as f:
        f.write(config.template(tuple(template)))

    return final_score
