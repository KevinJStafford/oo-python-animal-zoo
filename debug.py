from lib.animal import Animal
from lib.zoo import Zoo

# code here


# e.g.  

z1 = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )
z2= Zoo('Phoenix Zoe', 'Phoenix, AZ')
a1 = Animal( 'Lion', 75, 'Luke', z1 )
a2 = Animal('Tiger', 108, 'Jim', z2)
a3 = Animal('Bear', 12, 'BooBoo', z1)
a4 = Animal('Lion', 78, 'Leia', z1)






# ipdb allows us to stop our code & test stuff
import ipdb; ipdb.set_trace()
print( 'Thanks for visiting the zoo!' )