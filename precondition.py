# -*- coding: utf-8 -*-
from send_cmd import *
from ssh_connect import *
from clearUP import *

def createPool(c):
    PDInfo = SendCmd(c, 'phydrv')
    PDId = []
    row = PDInfo.split('\r\n')
    if "Pool" not in PDInfo:
        for i in range(4, len(row)-2):
            if len(row[i].split()) >= 9 and "Unconfigured" in row[i]:
                PDId.append(row[i].split()[0])

        SendCmd(c, 'pool -a add -s "name=TestViewUserPP,raid=0" -p ' + PDId[0])

def createSpare(c):
    PDInfo = SendCmd(c, 'phydrv')
    PDId = []
    row = PDInfo.split('\r\n')
    if "Global Spare" not in PDInfo:
        for i in range(4, len(row)-2):
            if len(row[i].split()) >= 9 and "Unconfigured" in row[i]:
                PDId.append(row[i].split()[0])

        SendCmd(c, 'spare -a add -t g -r y -p ' + PDId[0])

def createReadCache(c):
    PDInfo = SendCmd(c, 'phydrv')
    PDId = []
    row = PDInfo.split('\r\n')
    if "ReadCache" not in PDInfo:
        for i in range(4, len(row)-2):
            if len(row[i].split()) >= 9 and "Unconfigured" in row[i]:
                PDId.append(row[i].split()[0])

        SendCmd(c, 'rcache -a add -p ' + PDId[0])

def createVolume(c):
    VMInfo = SendCmd(c, 'volume')
    if "No volume exists" in VMInfo:
        PLInfo = SendCmd(c, 'pool')
        PLId = []
        row = PLInfo.split('\r\n')
        PLId.append(row[4].split()[0])
        SendCmd(c, 'volume -a add -s "name=TestViewUserPV,capacity=10GB" -p ' + PLId[0])

def createSnapshot(c):
    SSInfo = SendCmd(c, 'snapshot')
    if "No snapshot exists" in SSInfo:
        VMInfo = SendCmd(c, 'volume')
        VMId = []
        row = VMInfo.split('\r\n')
        VMId.append(row[4].split()[0])
        SendCmd(c, 'snapshot -a add -t volume -s "name=TestViewUserPS" -d ' + VMId[0])

def createClone(c):
    CLInfo = SendCmd(c, "clone")
    if "No clone found" in CLInfo:
        SSInfo = SendCmd(c, 'snapshot')
        SSId = []
        row = SSInfo.split('\r\n')
        SSId.append(row[4].split()[0])
        SendCmd(c, 'clone -a add -s "name=TestViewUserPC" -d ' + SSId[0])

def createInitiator(c):
    InInfo = SendCmd(c, "initiator")
    if "No initiator entry available" in InInfo:
        SendCmd(c, "initiator -a add -t iscsi -n test.test.com")

def createISCSIPortal(c):
    IIInfo = SendCmd(c, "iscsi -t portal")
    if "No portal in the subsystem" in IIInfo:
        SendCmd(c, 'iscsi -a add -t portal -r 2 -p 1 -m phy -s "iptype=4,dhcp=enable"')

def createTrunk(c):
    TKInfo = SendCmd(c, "trunk")
    if "No iSCSI trunks are available" in TKInfo:
        ISInfo = SendCmd(c, 'iscsi -t portal')
        ISId = []
        if 'No portal in the subsystem' not in ISInfo:
            row = ISInfo.split('\r\n')
            for x in range(4, (len(row) - 2)):
                ISId.append(row[x].split()[0])
        for i in ISId:
            SendCmd(c, 'iscsi -a del -t portal -i ' + i)

        SendCmd(c, 'iscsi -a mod -t port -r 2 -p 1 -s "port=enable"')
        SendCmd(c, 'iscsi -a mod -t port -r 2 -p 2 -s "port=enable"')
        SendCmd(c, 'trunk -a add -s "ctrlid=2,masterport=1,slaveport=2"')

def createCHAP(c):
    CHInfo = SendCmd(c, 'chap')
    if "CHAP record not found" in CHInfo:
        SendCmdPassword(c,'chap -a add -s "name=testViewUser,type=local"','111122223333')

def createBgasched(c):
    BSInfo = SendCmd(c, "bgasched")
    if "Type" not in BSInfo:
        SendCmd(c, 'bgasched -a add -t sc -s "recurtype=weekly,dow= Mon Wed Fri,starttime=11:00,endon=1/1/2020"')


if __name__ == "__main__":
    start = time.clock()
    c, ssh = ssh_conn()
    createPool(c)
    createVolume(c)
    createSnapshot(c)
    createClone(c)
    # createInitiator(c)
    # createISCSIPortal(c)
    # createCHAP(c)
    # createBgasched(c)
    ssh.close()
    elasped = time.clock() - start
