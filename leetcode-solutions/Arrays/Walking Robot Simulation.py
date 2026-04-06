"""Walking Robot Simulation
A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot receives an array of integers commands, which represents a sequence of moves that it needs to execute. There are only three possible types of instructions the robot can receive:

-2: Turn left 90 degrees.
-1: Turn right 90 degrees.
1 <= k <= 9: Move forward k units, one unit at a time.
Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, it will stay in its current location (on the block adjacent to the obstacle) and move onto the next command.

Return the maximum squared Euclidean distance that the robot reaches at any point in its path (i.e. if the distance is 5, return 25).

Note:

There can be an obstacle at (0, 0). If this happens, the robot will ignore the obstacle until it has moved off the origin. However, it will be unable to return to (0, 0) due to the obstacle.
North means +Y direction.
East means +X direction.
South means -Y direction.
West means -X direction.
Problem Link : https://leetcode.com/problems/walking-robot-simulation/?envType=daily-question&envId=2026-04-06"""

def robotSim(self, commands: list[int], obstacles: list[List[int]]) -> int:
        x,y=1,0
        n,e=0,0
        m=0
        obstacles = set((x[1],x[0]) for x in obstacles)
        for i in range(len(commands)):
            if i>0:
                if commands[i]==-1:
                    x,y= -1*y,x
                elif commands[i]== -2:
                    x,y=y,-1 *x
                else:
                    if x==0:
                        for j in range(commands[i]):
                            e+=(1 *y)
                            if (n,e) in obstacles:
                                e-=(1*y)
                                break
                    else:
                        for j in range(commands[i]):
                            n+=(1 *x)
                            if (n,e) in obstacles:
                                n-=(1 *x)
                                break
            else:
                if commands[i]==-1:
                    x,y= -1*y,x
                elif commands[i]== -2:
                    x,y=y,-1 *x
                else:
                    for j in range(1,commands[i]+1):
                        n+=(1 *x)
                        if (n,e) in obstacles:
                            n-=1
                            break
            dist = n**2 + e**2
            m= max(dist,m)
        
        return m