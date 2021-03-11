import os
import sys
import pygame
import sim

class Quadcopter:
    resolutionX = 640               # Camera resolution: 640*480
    resolutionY = 480

    def __init__(self):
        try:
            sim.simxFinish(-1) #close all opened connections
            clientID = sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
            if clientID != -1:
                print ('connect successfully')
            else:
                sys.exit("connect error")
        except:
                print ('Check if CoppeliaSim is open')

        _, Quadcopter_target = sim.simxGetObjectHandle(clientID, 'Quadricopter_target', sim.simx_opmode_blocking)
        _, targetPosition = sim.simxGetObjectPosition(clientID, Quadcopter_target, -1, sim.simx_opmode_buffer)
        print (targetPosition)

        ArrayPosition = [-0.18570, 0.99366, 0.615]
        sim.simxSetObjectPosition(clientID, Quadcopter_target, -1, ArrayPosition, sim.simx_opmode_oneshot)

        self.clientID = clientID
        self.Quadcopter_target = Quadcopter_target
        self.targetPosition = targetPosition



    # axis x
    def move_x(self, length):
        clientID = self.clientID
        Quadcopter_target = self.Quadcopter_target
        targetPosition = self.targetPosition

        sim.simxSetObjectPosition(clientID, Quadcopter_target, -1, targetPosition, sim.simx_opmode_oneshot)

        targetPosition[0] = targetPosition[0] + length

    def move_xx(self, length):
        clientID = self.clientID
        Quadcopter_target = self.Quadcopter_target
        targetPosition = self.targetPosition

        sim.simxSetObjectPosition(clientID, Quadcopter_target, -1, targetPosition, sim.simx_opmode_oneshot)

        targetPosition[0] = targetPosition[0] - length

    ##axis y
    def move_y(self, length):
        clientID = self.clientID
        Quadcopter_target = self.Quadcopter_target
        targetPosition = self.targetPosition

        sim.simxSetObjectPosition(clientID, Quadcopter_target, -1, targetPosition, sim.simx_opmode_oneshot)

        targetPosition[1] = targetPosition[1] + length

    def move_yy(self, length):
        clientID = self.clientID
        Quadcopter_target = self.Quadcopter_target
        targetPosition = self.targetPosition

        sim.simxSetObjectPosition(clientID, Quadcopter_target, -1,targetPosition, sim.simx_opmode_oneshot)

        targetPosition[1] = targetPosition[1] - length

    #axis z
    def move_z(self, length):
        clientID = self.clientID
        Quadcopter_target = self.Quadcopter_target
        targetPosition = self.targetPosition

        sim.simxSetObjectPosition(clientID, Quadcopter_target, -1, targetPosition, sim.simx_opmode_oneshot)

        targetPosition[2] = targetPosition[2] + length

    def move_zz(self, length):
        clientID = self.clientID
        Quadcopter_target = self.Quadcopter_target
        targetPosition = self.targetPosition

        sim.simxSetObjectPosition(clientID, Quadcopter_target, -1, targetPosition, sim.simx_opmode_oneshot)

        targetPosition[2] = targetPosition[2] - length


def main():
    robot = Quadcopter()
    resolutionX = robot.resolutionX
    resolutionY = robot.resolutionY

    length = 0.01

    pygame.init()
    screen = pygame.display.set_mode((resolutionX, resolutionY))
    screen.fill((255,255,255))
    pygame.display.set_caption("Vrep ")
    # 循环事件，按住一个键可以持续移动
    pygame.key.set_repeat(200, 50)

    while True:

        pygame.display.update()
        key_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    robot.move_x(length)

                elif event.key == pygame.K_s:
                    robot.move_xx(length)

                elif event.key == pygame.K_a:
                    robot.move_y(length)

                elif event.key == pygame.K_d:
                    robot.move_yy(length)

                elif event.key == pygame.K_UP:
                    robot.move_z(length)

                elif event.key == pygame.K_DOWN:
                    robot.move_zz(length)

                else:
                    print ("Invalid input")


if __name__ == '__main__':
    main()
