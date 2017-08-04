# -*- coding: utf-8 -*-
from send_cmd import *
from ssh_connect import *

def clearUpPool(c):
    PLInfo = SendCmd(c, 'pool')
    PLId = []
    row = PLInfo.split('\r\n')
    for i in range(4, (len(row)-2)):
        if len(row[i].split()) >= 9 and 'TestViewUserPP' in row[i]:
            PLId.append(row[i].split()[0])

    if len(PLId) != 0:
        SendCmdconfirm(c, 'pool -a del -i ' + PLId[0] + ' -f')

def clearUpVolume(c):
    VMInfo = SendCmd(c, 'volume')
    VMId = []
    row = VMInfo.split('\r\n')
    for i in range(4, (len(row)-2)):
        if len(row[i].split()) >= 9 and 'TestViewUserPV' in row[i]:
            VMId.append(row[i].split()[0])

    if len(VMId) != 0:
        SendCmdconfirm(c, 'volume -a del -i ' + VMId[0] + ' -f')

def clearUpSnapshot(c):
    SSInfo = SendCmd(c, 'snapshot')
    SSId = []
    row = SSInfo.split('\r\n')
    for i in range(4, (len(row)-2)):
        if len(row[i].split()) >= 7 and 'TestViewUserPS' in row[i]:
            SSId.append(row[i].split()[0])

    if len(SSId) != 0:
        SendCmdconfirm(c, 'snapshot -a del -i ' + SSId[0] + " -f")

def clearUpClone(c):
    CLInfo = SendCmd(c, 'clone')
    CLId = []
    row = CLInfo.split('\r\n')
    for i in range(4, (len(row)-2)):
        if len(row[i].split()) >= 10 and 'TestViewUserPC' in row[i]:
            CLId.append(row[i].split()[0])

    if len(CLId) != 0:
        SendCmd(c, 'clone -a del -i ' + CLId[0])

def clearUpInitiator(c):
    InInfo = SendCmd(c, "initiator")
    InId = []
    row = InInfo.split('Id: ')
    for i in range(1, len(row)):
        if "test.test.com" in row[i]:
            InId.append(row[i].split()[0])

    if len(InId) != 0:
        SendCmd(c, "initiator -a del -i " + InId[0])

def clearUpISCSIPortal(c):
    IIInfo = SendCmd(c, "iscsi -t portal")
    IIId= []
    row = IIInfo.split('\r\n')
    for i in range(4,len(row)-2):
        if len(row[i].split()) >= 10:
            IIId.append(row[i].split()[0])

    for id in IIId:
        SendCmd(c, "iscsi -a del -t portal -i " + id)

def clearUpTrunk(c):
    SendCmd(c, 'trunk -a del -i 1')

def clearUpCHAP(c):
    SendCmd(c, 'chap -a del -i 0')

def clearUpBgasched(c):
    SendCmd(c, 'bgasched -a del -t sc -i 1')


if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    clearUpSnapshot(c)
    clearUpClone(c)
    clearUpVolume(c)
    clearUpPool(c)
    clearUpInitiator(c)
    clearUpTrunk(c)
    clearUpCHAP(c)
    clearUpBgasched(c)
    ssh.close()
    elasped = time.clock() - start
