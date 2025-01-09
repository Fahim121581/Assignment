
fahim = open("sample.txt","w")
fahim.write("My name is Fahim.")
fahim.write("I am learning Python.")
fahim.write("This is the last line.")
fahim.close()
fahim=open("sample.txt", "r")
print(fahim.read())
fahim.close()