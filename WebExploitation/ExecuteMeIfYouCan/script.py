import os, sys, subprocess
import requests

M_COOKIES = dict(PHPSESSID="1sv3nggb2isq3lse9cc4puim62")
BASE_URL = "https://ringzer0ctf.com/challenges/121"

def print_banner():
	rows, columns = os.popen('stty size', 'r').read().split()
	banner = "=" * int(((int(columns) - len("-naiame script-")) / 2))
	print(banner + "-naiame script-" + banner)	

def get_content():
	resp = None
	print("| Sending request to : {}".format(BASE_URL))
	r = requests.get(BASE_URL, cookies = M_COOKIES)
	if r.status_code == 200:
		print("| Successfully fetched data")
		raw = r.text
		start = raw.find("----- BEGIN SHELLCODE -----") + 33
		end = raw.find("----- END SHELLCODE -----") - 10
		resp = raw[start:end].strip()
		return resp
	else:
		print("| Error on request")
		sys.exit()

def generate_file(content):
	print("| Generating C file...")
	template = '''
	#include <stdio.h>
	unsigned char code[] = "{}";
	int main(int argc, char **argv){{
		int foo_value = 0;
		int (*foo)() = (int(*)())code;
		foo_value = foo();
	}}
	'''.format(content)
	with open("tmp.c", "w") as f:
		f.write(template)
	print("| Succesfully generated file as tmp.c")

def send_flag(ans):
	ans = ans.strip()
	print(ans)
	# print(BASE_URL + "/{0}".format(ans))
	# r = requests.get(BASE_URL + "/{}".format(ans))
	# raw = r.text
	# print(raw)

if "__main__" in __name__:
	print_banner()
	content = get_content()
	generate_file(content)
	# gcc -fno-stack-protector -z execstack tmp.c -o test
	cmd = ['gcc', '-fno-stack-protector', '-zexecstack', 'tmp.c', '-otest']
	subprocess.run(cmd, stdout = subprocess.PIPE)
	res = subprocess.Popen(["./test"], stdout = subprocess.PIPE)
	(output, error) = res.communicate()
	print("RESULT : {}".format(output))
	# send_flag(str(ans))