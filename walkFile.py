import zipfile, os
from os import path
from buildScore import buildFile

basedir = os.getcwd()
prior_entry = {}

for bracket in os.listdir('.'):
    if path.isdir(bracket):
        os.chdir(path.join(os.getcwd(), bracket))

        for user in os.listdir('.'):
            if path.isdir(user):
                os.chdir(path.join(os.getcwd(), user))

                pct = buildFile(user, bracket, basedir.split("/")[-1])
                if pct == None:
                    continue

                if not user in prior_entry:
                    prior_entry[user] = (bracket, pct)
                else:
                    max_bkt, max_pct = prior_entry[user]
                    to_rm = None

                    if pct > max_pct:
                        to_rm = max_bkt
                        prior_entry[user] = (bracket, pct)
                    else:
                        to_rm = bracket

                    rm_path = path.join(basedir,
                                        to_rm, 
                                        user,
                                        "score.txt")

                    with open(rm_path, 'w') as f:
                        f.write("Scored in {} level\n".format(
                            prior_entry[user][0])
                        )
                os.chdir('..')
        os.chdir('..')
