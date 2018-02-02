import sys
import struct

fh = open(sys.argv[1], 'rb')

fbytes = fh.read()

i = 0
needle = [ 0x00, 0x11, 0x02, 0xff, 0x0c, 0x00 ]
while i < len(fbytes):

	j = 0
	match = True
	while j < len(needle):
		if needle[j] != fbytes[i+j]:
			match = False
		j += 1

	i += len(needle)

	if match == True:
		g = i - 16
		size = struct.unpack('h', bytes(fbytes[g:1]))

		print(fbytes[g+size:g+size+1])

		#for jig in fbytes[g:g+42]:
		#	sys.stdout.write("{:02x}-".format(jig))
		sys.stdout.write("\n")
		sys.stdout.flush()

	i += 1
