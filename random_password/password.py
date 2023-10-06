import random
pswd_data="ABCDEFGHIJKLMNOPQRSTUVWXYZ"\
			"abcdefghijklmnopqrstuvwxyz"\
			"0123456789"\
			"~!@#$%^&*()_-+={[|}]:;',.><?/"
pswd_len=int(input("Enter length of the pswd"))
pswd=""
for i in range(pswd_len):
	pswd+=random.choice(pswd_data)
print(pswd)