#i/usr/bin/env python3
#maximum algorithm
#by: juan.daniel.rangel.avila@gmail.com
#LICENSE GNU/GPL
import sys
data = [1.0, 3.14, 6.2, 8.1, 5.3]

maximum = -sys.float_info.max
for x in data:
	if x>maximum:
		maximum=x
    		#print(x)
print(maximum)
