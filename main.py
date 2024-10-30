from datetime import date, timedelta
from random import randint
import sys
import subprocess
import os

def get_date_string(n, startdate):
	d = startdate - timedelta(days=n)
	rtn = d.strftime("%a %b %d %X %Y %z -0400")
	return rtn

def main(argv):
	if len(argv) < 1 or len(argv) > 2:
		print("Error: Bad input.")
		sys.exit(1)
	n = int(argv[0])
	if len(argv) == 1:
		startdate = date.today()
	if len(argv) == 2:
		startdate = date(int(argv[1][0:4]), int(argv[1][5:7]), int(argv[1][8:10]))
	i = 0
	while i <= n:
		curdate = get_date_string(i, startdate)
		num_commits = randint(1, 10)
		for commit in range(0, num_commits):
			with open("realwork.txt", "w") as f:
				f.write(curdate + str(randint(0, 1000000)))
			# windows
			subprocess.run("git add realwork.txt", shell=True)
			subprocess.run("set GIT_AUTHOR_DATE=" + curdate + " && set GIT_COMMITTER_DATE=" + curdate + " && git commit -m 'update'", shell=True)
			print("Commit " + str(commit) + " on " + curdate)
		i += 1

if __name__ == "__main__":
	main(sys.argv[1:])
