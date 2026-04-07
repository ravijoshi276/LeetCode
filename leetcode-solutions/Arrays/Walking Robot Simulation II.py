"""Walking Robot Simulation II
A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1). The grid is aligned with the four cardinal directions ("North", "East", "South", and "West"). A robot is initially at cell (0, 0) facing direction "East".

The robot can be instructed to move for a specific number of steps. For each step, it does the following.

Attempts to move forward one cell in the direction it is facing.
If the cell the robot is moving to is out of bounds, the robot instead turns 90 degrees counterclockwise and retries the step.
After the robot finishes moving the number of steps required, it stops and awaits the next instruction.

Implement the Robot class:

Robot(int width, int height) Initializes the width x height grid with the robot at (0, 0) facing "East".
void step(int num) Instructs the robot to move forward num steps.
int[] getPos() Returns the current cell the robot is at, as an array of length 2, [x, y].
String getDir() Returns the current direction of the robot, "North", "East", "South", or "West".

Problem Link : https://leetcode.com/problems/walking-robot-simulation-ii/?envType=daily-question&envId=2026-04-07"""


class Robot:

    def __init__(self, width: int, height: int):
        self.width = width-1
        self.height = height-1
        self.n = 0
        self.e=1
        self.x=0
        self.y=0

    def step(self, num: int) -> None:
        while(num>0):
            
            if  num>0 and self.n :
                next= self.x+(num * self.n)
                if 0<=next<=self.height: 
                    self.x=next
                    num=0
                    break
                else:
                    if self.n==1:
                        self.x=self.height
                        num = next-self.x
                    else:
                        self.x=0
                        num= abs(next)
            
            elif num>0 and self.e:
                next = self.y+(num*self.e)
                if 0<=next<=self.width:
                    self.y=next
                    num=0
                    break
                else:
                    if self.e==1:
                        self.y=self.width
                        num = next-self.y
                    else:
                        self.y=0
                        num=abs(next)
    
            if num:
                self.setDir()
            num = num %(2*(self.height+self.width))
            if num==0:
                self.n,self.e = -1 *self.e ,self.n

    def getPos(self) -> List[int]:
        return [self.y,self.x]

    def getDir(self) -> str:
        if self.n:
            if self.n==1:
                return "North"
            return "South"
        else:
            if self.e==1:
                return "East"
            return "West"
    
    def setDir(self):
        self.n,self.e= self.e,-1*self.n
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()