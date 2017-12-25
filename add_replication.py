# -*- coding: utf-8 -*-
# 2017.12.25

from gui_test import *
from find_unconfigured_pd_id import *
import json


def precondition():

    pdId = find_pd_id()
    # create pool
    server.webapi('post', 'pool', {"name": "T_replication_0", "pds": pdId[:3], "raid_level": "raid5"})

    server.webapi('post', 'pool', {"name": "T_replication_1", "pds": pdId[3:6], "raid_level": "raid5"})

    server.webapi('post', 'pool', {"name": "T_replication_2", "pds": [pdId[6]], "raid_level": "raid0"})

    # create source volume
    for i in range(6):

        if i < 2:
            server.webapi('post', 'volume', {
                'pool_id': 2,
                'name': 'T_replication_vol_' + str(i),
                'capacity': '4GB',
                'thin_prov': i
            })

        elif i > 2 & i < 4:
            server.webapi('post', 'volume', {
                'pool_id': 0,
                'name': 'T_replication_vol_' + str(i),
                'capacity': '4GB',

            })

        else:

            server.webapi('post', 'volume', {
                'pool_id': 1,
                'name': 'T_replication_vol_' + str(i),
                'capacity': '1GB',
                'thin_prov': 1
            })

    return


def clean_up_environment():

    for i in range(3):

        server.webapi('delete', 'pool/' + str(i) + '?force=1')

    return


def add_replication():
    # precondition
    # precondition()

    tool = GUITestTool()

    # test date
    test_data = {
        "pool_id": ['0', '0', '1', '1'],
        "name": ['1', 'T2', 't_1' * 10, '_' * 31],
        "sync_mode": ['1', '2', '3', '']
    }
    # check data
    check_data = {
        "mode": ['Active-passive', 'Active-active', 'Active-active', 'Active-active'],
        "sync_mode": ['Async', 'Semi-Sync', 'Sync'],
        "kind": ['Local', 'Local', 'Local', 'Local'],
        "source": ['Source', 'Destination', 'Source', 'Destination'],
        "status": ['TBD', '', '', ''],
        "src_name": ['T_replication_vol_2', 'T_replication_vol_3', 'T_replication_vol_4', 'T_replication_vol_5'],
        "src_pool_name": ['T_replication_0', 'T_replication_0', 'T_replication_1', 'T_replication_1'],
        "dst_id": [6, 7, 8, 9],
        "dst_name": ['1', 'T2', 't_1' * 10, '_' * 31],
        "dst_pool_name": ['T_replication_1', 'T_replication_1', 'T_replication_0', 'T_replication_0'],
        "total_capacity": [4000000000, 4000000000, 1000000000, 1000000000],
        "used_capacity": [4000000000, 4000000000, 1000000000, 1000000000]
    }

    # click "Volume" button
    tool.click_action('//div[2]/div[1]/ul/li[4]/a/span')

    # click "Replication" button
    tool.click_action('//div[3]/div/div/div/ul/li/ul/li[4]/span')

    # create 4 nas share
    for i in range(len(test_data["pool_id"])):

        # click "Add" button
        tool.click_action('//pr-button-bar/div/div/div/button[1]')

        # select target Pool
        if test_data["pool_id"] == "0":
            tool.click_action('//form/div[1]/div/select/option[1]')
        else:
            tool.click_action('//form/div[1]/div/select/option[2]')

        # filling Nas Share name
        tool.fill_action('//form/div[2]/div[1]/input', test_data["name"][i])

        if test_data["thin"][i] == 'Enabled':
            # Enable Thin Provision
            tool.click_action('//form/div[3]/div/label/span')

        # select capacity unit
        if test_data["unit"] == "GB":
            tool.click_action('//form/div[4]/div[1]/div/div[2]/select/option[1]')
        else:
            tool.click_action('//form/div[4]/div[1]/div/div[2]/select/option[2]')

        # filling capacity
        tool.fill_action('//form/div[4]/div[1]/div/div[2]/input', test_data["capacity"][i])

        # submit
        tool.click_action('//div/div[3]/div/div/div[2]/div[2]/button[1]')

        nas_info = server.webapi('get', 'nasshare/' + str(i))

        if isinstance(nas_info, dict):

            info = json.loads(nas_info["text"])[0]

            for key in check_data:

                if key in info.keys():

                    tolog(key + ' Expected: ' + str(check_data[key][i]) + '; ' + 'Actual: ' + str(info[key]) + '\r\n')

                    if check_data[key][i] != info[key]:
                        tool.FailFlag = True
                        tolog('Fail: please check out: ' + key + '\r\n')

    tool.mark_status()

    tool.finished()

    return tool.FailFlag


if __name__ == "__main__":

    add_replication()