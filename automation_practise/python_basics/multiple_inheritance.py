'''
inheritance allows a class to inherit all the attributes and methods from more than one parent class
Method Resolution Order(MRO) - Search is done first in the current class, then continues to the parent class in depth first,
left right order without seraching the same class twice
'''

class MoveCharacter:
    def mov_fwd(self):
        print("moved 1 step forward")
    def mov_bwd(self):
        print("moved 1 step backward")
class JumpCharacter:
    def jump_1step(self):
            print("jumped 1 step ahead")
    def jump_2step(self):
            print("jumped 1 step ahead")
class Pokemon(MoveCharacter,JumpCharacter):
     def mov_fwd(self):
          print("Pokemon moved forward")
p=Pokemon()
p.jump_1step()
p.mov_fwd()
print(Pokemon.mro())
