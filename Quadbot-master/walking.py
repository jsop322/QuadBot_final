import time
from adafruit_servokit import ServoKit

class Walking():

    def __init__(self):
        # initialise the PWM device using the default address
        self.kit1 = ServoKit(channels=16, address=64)
        self.kit2 = ServoKit(channels=16, address=65)
        # set the pulse width limits of the servos
        self.pwm_min = 500
        self.pwm_max = 2500
        # number of servos that need adjustments
        servo_num = 12
        # set the desired angle (deg) for each servo
        self.angle = 90
        #Right front leg servo horizontal zero position
        self.servo6zero = 90
        self.servo7zero = 90
        self.servo8zero = 90
        #Left front leg servo horizontal zero position
        self.servo0zero = 90
        self.servo1zero = 90
        self.servo2zero = 90
        #Right back leg servo horizontal zero position
        self.servo9zero = 90
        self.servo10zero = 90
        self.servo11zero = 90
        #Left back leg servo horizontal zero position
        self.servo3zero = 90
        self.servo4zero = 90
        self.servo5zero = 90
        #Array of all servo horizontal zero positions
        self.servoZeroes = [self.servo0zero, self.servo1zero, self.servo2zero, self.servo3zero, self.servo4zero, self.servo5zero, self.servo6zero, self.servo7zero, self.servo8zero, self.servo9zero, self.servo10zero, self.servo11zero]
        self.horizontalZeroing(self.servoZeroes, self.kit1, self.kit2, self.pwm_min, self.pwm_max)
        self.initialized = True
        
    def setServo(self, channel, kit, position, delay, pwm_min, pwm_max):
        # set the pwm range
        kit.servo[channel].set_pulse_width_range(pwm_min, pwm_max)
        # set the position
        kit.servo[channel].angle = position 
        time.sleep(delay)
        print("Servo in channel " + str(channel) + " set to " + str(position) + " deg")

    def horizontalZeroing(self, servoZeroes, kit1, kit2, pwm_min, pwm_max):
        i = 0
        while i < 6:
            self.setServo(i, kit1, servoZeroes[i], 0, pwm_min, pwm_max)
            i += 1
        while i > 5 and i < 12:
            self.setServo(i, kit2, servoZeroes[i], 0, pwm_min, pwm_max)
            i += 1

    def testStanding(self, servoZeroes, kit1, kit2, pwm_min, pwm_max, testikulma):
        #testikulma = 80
        
        setServo(1, kit1, servoZeroes[1]+testikulma, 0, pwm_min, pwm_max)
        setServo(4, kit1, servoZeroes[4]+testikulma, 0, pwm_min, pwm_max)
        setServo(7, kit2, servoZeroes[7]+testikulma, 0, pwm_min, pwm_max)
        setServo(10, kit2, servoZeroes[10]+testikulma, 0, pwm_min, pwm_max)
        
        setServo(2, kit1, servoZeroes[2]-testikulma, 0, pwm_min, pwm_max)
        setServo(5, kit1, servoZeroes[5]-testikulma, 0, pwm_min, pwm_max)
        setServo(8, kit2, servoZeroes[8]-testikulma, 0, pwm_min, pwm_max)
        setServo(11, kit2, servoZeroes[11]-testikulma, 1, pwm_min, pwm_max)
        
    def testWalking(self, servoZeroes, kit1, kit2, pwm_min, pwm_max):
        angleUp = 60
        angleDown = 50
        angleHorizontal = 20
            
        self.setServo(1, kit1, servoZeroes[1]+angleUp, 0, pwm_min, pwm_max)
        self.setServo(2, kit1, servoZeroes[2]-angleUp, 0, pwm_min, pwm_max)
        self.setServo(10, kit2, servoZeroes[10]+angleUp, 0, pwm_min, pwm_max)
        self.setServo(11, kit2, servoZeroes[11]-angleUp, 0.1, pwm_min, pwm_max)
        
        self.setServo(3, kit1, servoZeroes[3]+angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(6, kit2, servoZeroes[6]-angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(0, kit1, servoZeroes[0]-angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(9 , kit2, servoZeroes[9]+angleHorizontal, 0.1, pwm_min, pwm_max)
        
        self.setServo(1, kit1, servoZeroes[1]+angleDown, 0, pwm_min, pwm_max)
        self.setServo(2, kit1, servoZeroes[2]-angleDown, 0, pwm_min, pwm_max)
        self.setServo(10, kit2, servoZeroes[10]+angleDown, 0, pwm_min, pwm_max)
        self.setServo(11, kit2, servoZeroes[11]-angleDown, 0.1, pwm_min, pwm_max)
        
        self.setServo(4, kit1, servoZeroes[4]+angleUp, 0, pwm_min, pwm_max)
        self.setServo(5, kit1, servoZeroes[5]-angleUp, 0, pwm_min, pwm_max)
        self.setServo(7, kit2, servoZeroes[7]+angleUp, 0, pwm_min, pwm_max)
        self.setServo(8, kit2, servoZeroes[8]-angleUp, 0.1, pwm_min, pwm_max)
        
        self.setServo(0, kit1, servoZeroes[0]+angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(9, kit2, servoZeroes[9]-angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(3, kit1, servoZeroes[3]-angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(6, kit2, servoZeroes[6]+angleHorizontal, 0.1, pwm_min, pwm_max)
        
        self.setServo(4, kit1, servoZeroes[4]+angleDown, 0, pwm_min, pwm_max)
        self.setServo(5, kit1, servoZeroes[5]-angleDown, 0, pwm_min, pwm_max)
        self.setServo(7, kit2, servoZeroes[7]+angleDown, 0, pwm_min, pwm_max)
        self.setServo(8, kit2, servoZeroes[8]-angleDown, 0.1, pwm_min, pwm_max)
        
        
    def walkBack(self, servoZeroes, kit1, kit2, pwm_min, pwm_max):
        angleUp = 60
        angleDown = 50
        angleHorizontal = 20
            
        self.setServo(1, kit1, servoZeroes[1]+angleUp, 0, pwm_min, pwm_max)
        self.setServo(2, kit1, servoZeroes[2]-angleUp, 0, pwm_min, pwm_max)
        self.setServo(10, kit2, servoZeroes[10]+angleUp, 0, pwm_min, pwm_max)
        self.setServo(11, kit2, servoZeroes[11]-angleUp, 0.1, pwm_min, pwm_max)
        
        self.setServo(3, kit1, servoZeroes[3]-angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(6, kit2, servoZeroes[6]+angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(0, kit1, servoZeroes[0]+angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(9 , kit2, servoZeroes[9]-angleHorizontal, 0.1, pwm_min, pwm_max)
        
        self.setServo(1, kit1, servoZeroes[1]+angleDown, 0, pwm_min, pwm_max)
        self.setServo(2, kit1, servoZeroes[2]-angleDown, 0, pwm_min, pwm_max)
        self.setServo(10, kit2, servoZeroes[10]+angleDown, 0, pwm_min, pwm_max)
        self.setServo(11, kit2, servoZeroes[11]-angleDown, 0.1, pwm_min, pwm_max)
        
        self.setServo(4, kit1, servoZeroes[4]+angleUp, 0, pwm_min, pwm_max)
        self.setServo(5, kit1, servoZeroes[5]-angleUp, 0, pwm_min, pwm_max)
        self.setServo(7, kit2, servoZeroes[7]+angleUp, 0, pwm_min, pwm_max)
        self.setServo(8, kit2, servoZeroes[8]-angleUp, 0.1, pwm_min, pwm_max)
        
        self.setServo(0, kit1, servoZeroes[0]-angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(9, kit2, servoZeroes[9]+angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(3, kit1, servoZeroes[3]+angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(6, kit2, servoZeroes[6]-angleHorizontal, 0.1, pwm_min, pwm_max)
        
        self.setServo(4, kit1, servoZeroes[4]+angleDown, 0, pwm_min, pwm_max)
        self.setServo(5, kit1, servoZeroes[5]-angleDown, 0, pwm_min, pwm_max)
        self.setServo(7, kit2, servoZeroes[7]+angleDown, 0, pwm_min, pwm_max)
        self.setServo(8, kit2, servoZeroes[8]-angleDown, 0.1, pwm_min, pwm_max)
        
    def turnLeft(self, servoZeroes, kit1, kit2, pwm_min, pwm_max):
        angleUp = 60
        angleDown = 50
        angleHorizontal = 20
            
        self.setServo(1, kit1, servoZeroes[1]+angleUp, 0, pwm_min, pwm_max)
        self.setServo(2, kit1, servoZeroes[2]-angleUp, 0, pwm_min, pwm_max)
        self.setServo(10, kit2, servoZeroes[10]+angleUp, 0, pwm_min, pwm_max)
        self.setServo(11, kit2, servoZeroes[11]-angleUp, 0.1, pwm_min, pwm_max)
        
        self.setServo(3, kit1, servoZeroes[3]-angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(6, kit2, servoZeroes[6]-angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(0, kit1, servoZeroes[0]+angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(9 , kit2, servoZeroes[9]+angleHorizontal, 0.1, pwm_min, pwm_max)
        
        self.setServo(1, kit1, servoZeroes[1]+angleDown, 0, pwm_min, pwm_max)
        self.setServo(2, kit1, servoZeroes[2]-angleDown, 0, pwm_min, pwm_max)
        self.setServo(10, kit2, servoZeroes[10]+angleDown, 0, pwm_min, pwm_max)
        self.setServo(11, kit2, servoZeroes[11]-angleDown, 0.1, pwm_min, pwm_max)
        
        self.setServo(4, kit1, servoZeroes[4]+angleUp, 0, pwm_min, pwm_max)
        self.setServo(5, kit1, servoZeroes[5]-angleUp, 0, pwm_min, pwm_max)
        self.setServo(7, kit2, servoZeroes[7]+angleUp, 0, pwm_min, pwm_max)
        self.setServo(8, kit2, servoZeroes[8]-angleUp, 0.1, pwm_min, pwm_max)
        
        self.setServo(0, kit1, servoZeroes[0]-angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(9, kit2, servoZeroes[9]-angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(3, kit1, servoZeroes[3]+angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(6, kit2, servoZeroes[6]+angleHorizontal, 0.1, pwm_min, pwm_max)
        
        self.setServo(4, kit1, servoZeroes[4]+angleDown, 0, pwm_min, pwm_max)
        self.setServo(5, kit1, servoZeroes[5]-angleDown, 0, pwm_min, pwm_max)
        self.setServo(7, kit2, servoZeroes[7]+angleDown, 0, pwm_min, pwm_max)
        self.setServo(8, kit2, servoZeroes[8]-angleDown, 0.1, pwm_min, pwm_max)
        
    def turnRight(self, servoZeroes, kit1, kit2, pwm_min, pwm_max):
        angleUp = 60
        angleDown = 50
        angleHorizontal = 20
            
        self.setServo(1, kit1, servoZeroes[1]+angleUp, 0, pwm_min, pwm_max)
        self.setServo(2, kit1, servoZeroes[2]-angleUp, 0, pwm_min, pwm_max)
        self.setServo(10, kit2, servoZeroes[10]+angleUp, 0, pwm_min, pwm_max)
        self.setServo(11, kit2, servoZeroes[11]-angleUp, 0.1, pwm_min, pwm_max)
        
        self.setServo(3, kit1, servoZeroes[3]+angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(6, kit2, servoZeroes[6]+angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(0, kit1, servoZeroes[0]-angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(9 , kit2, servoZeroes[9]-angleHorizontal, 0.1, pwm_min, pwm_max)
        
        self.setServo(1, kit1, servoZeroes[1]+angleDown, 0, pwm_min, pwm_max)
        self.setServo(2, kit1, servoZeroes[2]-angleDown, 0, pwm_min, pwm_max)
        self.setServo(10, kit2, servoZeroes[10]+angleDown, 0, pwm_min, pwm_max)
        self.setServo(11, kit2, servoZeroes[11]-angleDown, 0.1, pwm_min, pwm_max)
        
        self.setServo(4, kit1, servoZeroes[4]+angleUp, 0, pwm_min, pwm_max)
        self.setServo(5, kit1, servoZeroes[5]-angleUp, 0, pwm_min, pwm_max)
        self.setServo(7, kit2, servoZeroes[7]+angleUp, 0, pwm_min, pwm_max)
        self.setServo(8, kit2, servoZeroes[8]-angleUp, 0.1, pwm_min, pwm_max)
        
        self.setServo(0, kit1, servoZeroes[0]+angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(9, kit2, servoZeroes[9]+angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(3, kit1, servoZeroes[3]-angleHorizontal, 0, pwm_min, pwm_max)
        self.setServo(6, kit2, servoZeroes[6]-angleHorizontal, 0.1, pwm_min, pwm_max)
        
        self.setServo(4, kit1, servoZeroes[4]+angleDown, 0, pwm_min, pwm_max)
        self.setServo(5, kit1, servoZeroes[5]-angleDown, 0, pwm_min, pwm_max)
        self.setServo(7, kit2, servoZeroes[7]+angleDown, 0, pwm_min, pwm_max)
        self.setServo(8, kit2, servoZeroes[8]-angleDown, 0.1, pwm_min, pwm_max)

    def getKit1(self):
        return self.kit1
    def getKit2(self):
        return self.kit2
    def getServoZeroes(self):
        return self.servoZeroes
    def getPwmMin(self):
        return self.pwm_min
    def getPwmMax(self):
        return self.pwm_max
    
    def cameraLeft(self, kit1, pwm_min, pwm_max):
        self.setServo(15, kit1, 135, 0, pwm_min, pwm_max)
        
    def cameraRight(self, kit1, pwm_min, pwm_max):
        self.setServo(15, kit1, 45, 0, pwm_min, pwm_max)
        
    def cameraCenter(self, kit1, pwm_min, pwm_max):
        self.setServo(15, kit1, 90, 0, pwm_min, pwm_max)

