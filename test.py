# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:03:55 2021

@author: hajar
"""

import rospy
import unittest
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension
from listener import ULTRASONIC_SENSORS1, ULTRASONIC_SENSORS2, MOTOR_COMMANDS


"""
donner l'ordre d'avancer en ligne droite
1) envoyer trame ros avec floats inferieur a 10 pour chaque capteur avant 
2) envoyer trame ros avec floats inferieur a 10 pour chaque capteur arrière 
vérifier si la voiture s'arrete en verifiant speed_cmd=0 et drive_enabled = 0
"""
class Test_Hurdle1(unittest.TestCase):
    def test_hurdle1_1(self):
        global ULTRASONIC_SENSORS1
        global ULTRASONIC_SENSORS2
        global MOTOR_COMMANDS
        pubUltr1 = rospy.Publisher('/ultrasonic_sensors1', Float32MultiArray, queue_size=10)
        pubUltr2 = rospy.Publisher('/ultrasonic_sensors2', Float32MultiArray, queue_size=10)
        for i in range(10):
            
            #Ultrasonic1 publisher
            rateU = rospy.Rate(10) # 10hz
            vectU = Float32MultiArray()
            vectU.layout.dim.append(MultiArrayDimension())
            vectU.layout.dim[0].label = "height"
            vectU.layout.dim[0].size = 3
            vectU.layout.dim[0].stride = 3
    
            #Ultrasonic2 publisher
            rateU2 = rospy.Rate(10) # 10hz
            vectU2 = Float32MultiArray()
            vectU2.layout.dim.append(MultiArrayDimension())
            vectU2.layout.dim[0].label = "height"
            vectU2.layout.dim[0].size = 3
            vectU2.layout.dim[0].stride = 3           
            
            ULTRASONIC_SENSORS1.MUT.acquire()
            vectU.data = [5.0, 5.0, 50.0]    
            ULTRASONIC_SENSORS1.MUT.release()
            pubUltr1.publish(vectU)
            rateU.sleep()

            ULTRASONIC_SENSORS2.MUT.acquire()
            vectU2.data = [50.0, 50.0, 5.0]    
            ULTRASONIC_SENSORS2.MUT.release()
            pubUltr2.publish(vectU2)
            rateU2.sleep()
            
            self.assertEqual(MOTOR_COMMANDS.speed_cmd == 0)
            self.assertEqual(MOTOR_COMMANDS.drive_enabled == 0)
            fichier = open("log.txt", "a")
            fichier.write("\n Test_Hurdle1")
            fichier.write("\n speed_cmd = ", MOTOR_COMMANDS.speed_cmd)
            fichier.write("\n drive_enabled = ",MOTOR_COMMANDS.drive_enabled, "\n")
            fichier.close()
            
class Test_Hurdle2(unittest.TestCase):
    def test_hurdle1_2(self):
        global ULTRASONIC_SENSORS1
        global ULTRASONIC_SENSORS2 
        global MOTOR_COMMANDS
        pubUltr1 = rospy.Publisher('/ultrasonic_sensors1', Float32MultiArray, queue_size=10)
        pubUltr2 = rospy.Publisher('/ultrasonic_sensors2', Float32MultiArray, queue_size=10)
        for i in range(10):
            #Ultrasonic1 publisher
            rateU = rospy.Rate(10) # 10hz
            vectU = Float32MultiArray()
            vectU.layout.dim.append(MultiArrayDimension())
            vectU.layout.dim[0].label = "height"
            vectU.layout.dim[0].size = 3
            vectU.layout.dim[0].stride = 3
    
            #Ultrasonic2 publisher
            rateU2 = rospy.Rate(10) # 10hz
            vectU2 = Float32MultiArray()
            vectU2.layout.dim.append(MultiArrayDimension())
            vectU2.layout.dim[0].label = "height"
            vectU2.layout.dim[0].size = 3
            vectU2.layout.dim[0].stride = 3           
            
            ULTRASONIC_SENSORS1.MUT.acquire()
            vectU.data = [50.0, 50.0, 5.0]    
            ULTRASONIC_SENSORS1.MUT.release()
            pubUltr1.publish(vectU)
            rateU.sleep()

            ULTRASONIC_SENSORS2.MUT.acquire()
            vectU2.data = [5.0, 5.0, 50.0]    
            ULTRASONIC_SENSORS2.MUT.release()
            pubUltr2.publish(vectU2)
            rateU2.sleep()
            
            self.assertEqual(MOTOR_COMMANDS.speed_cmd == 0)
            self.assertEqual(MOTOR_COMMANDS.drive_enabled == 0)
            
            fichier = open("log.txt", "a")
            fichier.write("\n Test_Hurdle2")
            fichier.write("\n speed_cmd = ", MOTOR_COMMANDS.speed_cmd)
            fichier.write("\n drive_enabled = ",MOTOR_COMMANDS.drive_enabled, "\n")
            fichier.close()

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun("python_test", 'test_hurdle1_1', Test_Hurdle1)
    rosunit.unitrun("python_test", 'test_hurdle1_2', Test_Hurdle2)
