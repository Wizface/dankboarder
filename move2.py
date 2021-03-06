#!/usr/bin/python

import smbus
import math
import socket
import time
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.1.184', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c


def get_da_daet():
    t0 = time.time()
    print("content uwu")
    bus = smbus.SMBus(0) # or bus = smbus.SMBus(1) for Revision 2 boards
    address = 0x68       # This is the address value read via the i2cdetect command

    # Now wake the 6050 up as it starts in sleep mode
    bus.write_byte_data(address, power_mgmt_1, 0)

    
    def read_byte(adr):
        return bus.read_byte_data(address, adr)
    def read_word(adr):
        high = bus.read_byte_data(address, adr)
        low = bus.read_byte_data(address, adr+1)
        val = (high << 8) + low
        return val
    def read_word_2c(adr):
        val = read_word(adr)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val
    def dist(a,b):
        return math.sqrt((a*a)+(b*b))
    def get_y_rotation(x,y,z):
        radians = math.atan2(x, dist(y,z))
        return -math.degrees(radians)
    def get_x_rotation(x,y,z):
        radians = math.atan2(y, dist(x,z))
        return math.degrees(radians)

    gyro_xout = read_word_2c(0x43)
    gyro_yout = read_word_2c(0x45)
    gyro_zout = read_word_2c(0x47)

    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)

    accel_xout_scaled = accel_xout / 16384.0
    accel_yout_scaled = accel_yout / 16384.0
    accel_zout_scaled = accel_zout / 16384.0

    #print "accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled
    #print "accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled
    #print "accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled

    print "x rotation: " , get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
    print "y rotation: " , get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
    #end = time.time()
    t1 = time.time()
    total = t1-t0
    print("got data and sent in:")
    print(total)
    return get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled), get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)

while 1:
    rotx, roty = get_da_daet()
    
    print("check if connect")
    ####################################
    ####################################
    sock.setblocking(0)
    try:
        data, address = sock.recvfrom(4096)
        #data, address = sock.recvfrom(4096)
        #print(address)
        if data == "killer_ben":
            print("kill command received")
            exit()
            
        comx = 1
        comy = 1
        #print("connected")
        paylod = str({'right': comx, 'forward': comy, 'xrotation': rotx, 'yrotation': roty})
        #print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
        #print >>sys.stderr, data
        paylod = str.encode(paylod)
        #if data:
        #    sent = sock.sendto(data, address)
        #    print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
        sent = sock.sendto(paylod, address)
        print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
        
        
       
    except:
        #print("fail: none connect")
        
        pass