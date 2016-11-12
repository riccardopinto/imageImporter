import urllib


## importImages function
#  @param filename a string containing the name of the file in which the images are stored
#  @return 0 or -1 if the filename is invalid
#
#  Note: The funcion assumes the urls are written one per line and that they are all valid urls
#        since this is supposed to be part of a bigger project and since it wasn't in the requirements
#	 the validation step was skipped. The images are stored with the add of a jpg extension to avoid images saved in raw numbers (some OS can have a problem with this).
#	 This could not be optimal for any situation, but it satisfied the test scenario that was given by email.

def importImages(filename):
	# check if the file exists
	try:
		with open(filename,"r") as f:
			c=0
			for line in f:
				#check if EOF
				if(line!="\n"):
					imageName=str(c)+ ".jpg"
					print("Importing image from url %s naming it %s" % (line,imageName))
					#retrieve url and incremnet c for future images
					urllib.urlretrieve(line,str(c))
					c+=1
				else:
					print("Reached EOF")
		return 0;

	except:
		print("Error in filename %s does not exist" % (filename))
		return -1;
		
#test line
#importImages("file.txt")
