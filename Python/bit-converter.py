num_bits = int(input("How many bits are there? "))
num_bytes = num_bits/8
num_kilobytes = num_bytes/1024
num_megabytes = num_kilobytes/1024
num_gigabytes = num_megabytes/1024
num_terabytes = num_gigabytes/1024
print("bits: " + str(num_bits))
print("bytes: " + str(num_bytes))
print("Kilobytes: " + str(num_kilobytes))
print("Megabytes: " + str(num_megabytes))
print("Gigabytes: " + str(num_gigabytes))
print("Terabytes: " + str(num_terabytes))