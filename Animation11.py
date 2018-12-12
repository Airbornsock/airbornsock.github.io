import animationframework11 as afw #imports the framework file. "afw" can be used in replacement for "animationframework11" when written in the code
import matplotlib.pyplot #imports the plotting library to create 2D graphs and images.
import csv # imports the tool required to read and write csv files (tabular data)
import random #imports random integers
import matplotlib.animation  #allows the creation of animations

# Opens raster file and runs through each line using reader
environment = []
f = open('Ex6Raster.Py', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:				
    rowlist = []
    for value in row:				
        #print(value) 				
        rowlist.append(value)
    environment.append(rowlist)
f.close() #stops reading when the last line is read







#random_seed = 200
agents = []
num_of_agents=10
#num_of_iterations = 100
neighbourhood=200


#making an empty graph
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])






for i in range(num_of_agents):
    #random_seed += 1
    agents.append(afw.Agent(environment,neighbourhood,agents))
    print(agents[i])
    
    
    
carry_on = True	



def update(frame_number):
    global carry_on
    fig.clear()       
    
    
    
 #telling the agents what to do  
    
     #for j in range(num_of_iterations):
        #random.shuffle(agents)
    
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        #agents[i].share_with_neighbours()
        
        
        
        
        #setting the dimensions of the graph
    matplotlib.pyplot.ylim(300, -1)
    matplotlib.pyplot.xlim(-1, 300)
    #importing the environment into the graph
    matplotlib.pyplot.imshow(environment)
    #defining the carry on function - telling the code what criteria needs to be satisfied for carry_on to be true of false, and then stop the agents moving and eating.
    if random.random() < 0.00001:
        carry_on = False
        print("stopping condition")

    #plot agents
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
        matplotlib.pyplot.imshow(environment)
        
      
		
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 100) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


#plot location
#for i in range(num_of_agents):
   #matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
   #print(agents[i][0],agents[i][1])

#call animation
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show()


print("End")    
    