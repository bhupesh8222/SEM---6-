import subprocess as cmd
import datetime
message = str(datetime.datetime.now())
cmd.run("git add .", check=True, shell=True)
cmd.run('git commit -m'+ ' " ' + message + ' " ', check=True, shell=True)
cmd.run("git push origin master", check=True, shell=True)
