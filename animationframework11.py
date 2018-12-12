import random
class Agent():
    #create a list
    def __init__(self,environment,neighbourhood,agents):
       #define the agents and environment
        self.environment = environment
        self.store = 0
        self._x = random.randint(0,300)
        self._y = random.randint(0,300)
        self.neighbourhood = neighbourhood
        self.agents=agents
        
        #create a string
        def __str__(self):
            return"x"+str(self._x)+"y"+str(self._y)
    
    
    def getx(self):
       return self._x
   
    def gety(self):
        return self._y
        
        
        #defining how the agents move
    def move(self): 
        if random.random() < 0.5:
            self._y = (self._y + 1) % 299
        else:
            self._y = (self._y - 1) % 299

        if random.random() < 0.5:
            self._x = (self._x + 1) % 299
        else:
            self._x = (self._x - 1) % 299

     
        #telling the agents how to eat, and how much and when
    def eat(self):
            if self.environment[self._y][self._x] > 10:
                self.environment[self._y][self._x] -= 10
                self.store += 10
        
        #defining the share criteria, although is not used in the final code
    def share_with_neighbours(self):
        for Agent in self.agents:
            dist = self.distance_between(Agent) 
            if dist <= self.neighbourhood:
                sum = self.store + Agent.store
                ave = sum /2
                self.store = ave
                Agent.store = ave
                print("sharing " + str(dist) + " " + str(ave))
  #not used
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
