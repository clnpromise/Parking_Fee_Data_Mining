#change the city!!!
with open('Sydney_Street_Locations','r') as old:
	n=0
	output=""
	for line in old.readlines():
		n+=1
		output+=line
		if n % 1000==0:
			with open('download'+str(n/1000)+'.txt','w+') as out:
				out.write(output)
			output=""
		