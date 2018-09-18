#odd_even
val = int(input(""))
mod = val % 2
#for_odd
if mod > 0:
	print("odd")
#for_even
elif mod < 0:
	print("even")
else:
	print("invalid")
