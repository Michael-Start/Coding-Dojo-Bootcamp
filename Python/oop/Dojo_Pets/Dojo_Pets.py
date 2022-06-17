from ninjas import Ninja
from pets import Pet

pet_1 =Pet("Stompy Mcstomp", "T-rex", "stomping", "ROAR")
ninja_1 = Ninja("Mike", "Start", pet_1, "steaks", "a whole turkey") 

print(ninja_1.pet.name)

ninja_1.feed().walk().bathe()




