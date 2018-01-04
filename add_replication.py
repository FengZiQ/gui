# -*- coding: utf-8 -*-
# 2018.01.02

from gui_test import *
from find_unconfigured_pd_id import *
import json

tool = GUITestTool()


def precondition():
    # stop all replication
    replica_request = server.webapi('get', 'replica')

    if isinstance(replica_request, dict):

        try:

            for replica in json.loads(replica_request["text"]):
                server.webapi('post', 'replicaloc/' + str(replica["src_id"]) + '/stop')

                time.sleep(3)

        except (TypeError, KeyError):

            tolog('precondition is failed\r\n')

        else:

            pdId = find_pd_id()

            # create pool
            if len(pdId) > 0:

                server.webapi('post', 'pool', {"name": "T_replication_0", "pds": pdId[:3], "raid_level": "raid5"})

                server.webapi('post', 'pool', {"name": "T_replication_1", "pds": pdId[3:6], "raid_level": "raid5"})

                server.webapi('post', 'pool', {"name": "T_replication_2", "pds": [pdId[6]], "raid_level": "raid0"})

                server.webapi('post', 'pool', {"name": "T_replication_3", "pds": [15], "raid_level": "raid0"})

            else:

                tolog('precondition is failed\r\n')

            # create source volume
            for i in range(6):

                if i <= 1:
                    server.webapi('post', 'volume', {
                        'pool_id': 2,
                        'name': 'T_replication_vol_' + str(i),
                        'capacity': '900GB',
                        'thin_prov': i
                    })

                elif i == 2 or i == 3:
                    server.webapi('post', 'volume', {
                        'pool_id': 0,
                        'name': 'T_replication_vol_' + str(i),
                        'capacity': '4GB',
                        'block': '64kb',
                        'sector': '4kb',
                        'compress': 'gzip',
                        'sync': 'disabled',
                        'logbias': 'throughput'
                    })

                elif i == 4 or i == 5:

                    server.webapi('post', 'volume', {
                        'pool_id': 1,
                        'name': 'T_replication_vol_' + str(i),
                        'capacity': '1GB'
                    })

    return


def clean_up_environment():
    # stop all replication
    replica_request = server.webapi('get', 'replica')
    if isinstance(replica_request, dict):

        try:

            for replica in json.loads(replica_request["text"]):
                server.webapi('post', 'replicaloc/' + str(replica["src_id"]) + '/stop')

                time.sleep(3)

        except (TypeError, KeyError):

            tolog('to clean up environment is failed\r\n')

        else:

            for i in range(3):
                server.webapi('delete', 'pool/' + str(i) + '?force=1')

    # delete pool
    find_pd_id()

    # delete initiator
    init_request = server.webapi('get', 'initiator')
    if isinstance(init_request, dict):

        try:

            for init in json.loads(init_request["text"]):
                server.webapi('delete', 'initiator/' + str(init["id"]))

        except (TypeError, KeyError):

            tolog('to clean up environment is failed\r\n')

    return


def add_replication():
    # precondition
    # precondition()

    # test date
    test_data = {
        "src_pool_name": ['T_replication_0', 'T_replication_0', 'T_replication_1', 'T_replication_1'],
        "src_id": [2, 3, 4, 5],
        "dst_pool_name": ['T_replication_1', 'T_replication_1', 'T_replication_0', 'T_replication_0'],
        "dst_name": ['1', 'T2', 't_1' * 10, '_' * 31],
        "sync_mode": ['Async', 'Semi-Sync', 'Sync', '']
    }
    # check data
    replication_data = {
        "description": ['Ready.', 'Ready.', 'Ready.', 'Ready.'],
        "dst_id": [6, 7, 8, 9],
        "dst_name": ['1', 'T2', 't_1' * 10, '_' * 31],
        "dst_pool_name": ['T_replication_1', 'T_replication_1', 'T_replication_0', 'T_replication_0'],
        "kind": ['Local', 'Local', 'Local', 'Local'],
        "mode": ['Active-Passive', 'Active-Passive', 'Active-Passive', 'Active-Passive'],
        "src_id": [2, 3, 4, 5],
        "src_name": ['T_replication_vol_2', 'T_replication_vol_3', 'T_replication_vol_4', 'T_replication_vol_5'],
        "src_pool_name": ['T_replication_0', 'T_replication_0', 'T_replication_1', 'T_replication_1'],
        "status": ['OK', 'OK', 'OK', 'OK'],
        "sync_mode": ['Async', 'Semi-Sync', 'Sync', 'Sync'],
        "total_capacity": [3999989760, 3999989760, 999997440, 999997440]
    }
    volume_data = [
        'total_capacity', 'adv_kind', 'sector', 'compress', 'ratio', 'thin_prov',
        'adv_type', 'block', 'adv_mode', 'adv_status', 'adv_protocol', 'logbias'
    ]

    # click "Volume" button
    tool.click_action('//div[2]/div[1]/ul/li[4]/a/span', 'Volume button')

    # click "Replication" button
    tool.click_action('//div[3]/div/div/div/ul/li/ul/li[4]/a/span', 'Replication button')

    # create 4 replication
    for i in range(len(test_data["dst_name"])):

        # click "Add" button
        tool.click_action('//pr-button-bar/div/div/div/button[1]', 'Add button')

        # select source pool
        if test_data["src_pool_name"][i] == "T_replication_0":
            tool.click_action('//form/div[1]/div[1]/select/option[1]', 'source pool drop down box')
        elif test_data["src_pool_name"][i] == "T_replication_1":
            tool.click_action('//form/div[1]/div[1]/select/option[2]' 'source pool drop down box')

        # select source volume
        if test_data["src_id"][i] == 2 or test_data["src_id"][i] == 3 or test_data["src_id"][i] == 5:
            tool.click_action('//form/div[2]/div[1]/select/option[1]', 'source volume drop down box')
        elif test_data["src_id"][i] == 4:
            tool.click_action('//form/div[2]/div[1]/select/option[2]', 'source volume drop down box')

        # select destination pool
        tool.click_action('//form/div[3]/div[1]/select/option[3]', 'destination pool drop down box')

        # filling destination volume name
        tool.fill_action('//form/div[4]/div[1]/input', test_data["dst_name"][i], 'dst volume name test box')

        # select Sync mode
        if test_data["sync_mode"][i] == 'Async':
            tool.click_action('//form/div[5]/div[1]/select/option[1]', 'sync mode drop down box')
        elif test_data["sync_mode"][i] == 'Semi-Sync':
            tool.click_action('//form/div[5]/div[1]/select/option[2]', 'sync mode drop down box')
        elif test_data["sync_mode"][i] == 'Sync':
            tool.click_action('//form/div[5]/div[1]/select/option[3]', 'sync mode drop down box')

        # submit
        tool.click_action('//div[3]/div/div/div[2]/div[2]/button[1]', 'submit button')

        # confirm
        tool.click_action('/html/body/div[1]/div/div/div/form/div[3]/button[1]', 'confirm button')

        time.sleep(5)

    # check replication list information
    tolog('check replication list information\r\n')

    try:
        replica_request = server.webapi('get', 'replica')

        if isinstance(replica_request, dict):

            replica_info = json.loads(replica_request["text"])

            for replica in replica_info:

                if replica["src_id"] == 2:

                    for key in replication_data.keys():

                        if replication_data[key][0] != replica[key]:

                            tolog(key + ': ' + str(replication_data[key][0]) + ' != ' + str(replica[key]) + '\r\n')
                            tool.FailFlag = True

                elif replica["src_id"] == 4:

                    for key in replication_data.keys():

                        if replication_data[key][2] != replica[key]:

                            tolog(key + ': ' + str(replication_data[key][2]) + ' != ' + str(replica[key]) + '\r\n')
                            tool.FailFlag = True

    except Exception as e:
        tolog(e.message)

    # check source volume and destination volume info
    tolog('check source volume and destination volume info\r\n')

    try:
        # source volume info
        vol2_request = server.webapi('get', 'volume/2')
        vol2_info = json.loads(vol2_request["text"])[0]

        # destination volume info
        vol6_request = server.webapi('get', 'volume/6')
        vol6_info = json.loads(vol6_request["text"])[0]

    except Exception as e:

        tolog(e.message)

    else:

        for k in volume_data:

            if vol2_info[k] != vol6_info[k]:

                tolog(k + vol2_info[k] + ' != ' + vol6_info[k] + '\r\n')
                tool.FailFlag = True

    tool.mark_status()

    return tool.FailFlag


def pause_resume_replication():

    # select the one replication
    tool.click_action('//table/tbody/tr[2]/td[1]/span/span')

    # click Pause button
    tool.click_action('//pr-button-bar/div/div/div/button[2]')

    checkpoint = tool.driver.find_element_by_xpath()

    if 'Failed to pause replication' in checkpoint:

        tool.FailFlag = True


def stop_replication():
    pass


if __name__ == "__main__":

    add_replication()
    # pause_resume_replication()
    # stop_replication()