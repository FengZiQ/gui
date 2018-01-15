# -*- coding: utf-8 -*-
# 2017.12.21

from gui_test import *
from find_unconfigured_pd_id import *
import json


def precondition():

    pd_id = find_pd_id()
    # create pool
    server.webapi('post', 'pool', {"name": "T_NAS_pool_0", "pds": pd_id[:3], "raid_level": "raid5"})

    server.webapi('post', 'pool', {"name": "T_NAS_pool_1", "pds": [pd_id[3]], "raid_level": "raid0"})

    return


def create_nas_share():
    # precondition
    precondition()

    tool = GUITestTool()

    # test date
    test_data = {
        "pool_id": ['0', '0', '1', '1'],
        "name": ['1', 'T2', 't_1'*10, '_'*31],
        "thin": ['Enabled', 'Disabled', 'Enabled', 'Disable'],
        "unit": ['GB', 'GB', 'TB', 'TB'],
        "capacity": ['1', '2', '1', '2']
    }
    # check data
    check_data = {
        "name": ['1', 'T2', 't_1'*10, '_'*31],
        "pool_name": ['T_NAS_pool_0', 'T_NAS_pool_0', 'T_NAS_pool_1', 'T_NAS_pool_1'],
        "pool_id": [0, 0, 1, 1],
        "thin_prov": ['Enabled', 'Disabled', 'Enabled', 'Disabled'],
        "total_capacity": [1000000000, 2000000000, 1000000000000, 2000000000000],
        "sync": ['standard', 'standard', 'standard', 'standard'],
        "recsize": ['128 KB', '128 KB', '128 KB', '128 KB'],
        "compress": ['off', 'off', 'off', 'off'],
        "logbias": ['latency', 'latency', 'latency', 'latency'],
        "status": ['Mounted', 'Mounted', 'Mounted', 'Mounted'],
        "operational_status": ['OK', 'OK', 'OK', 'OK']
    }

    # click "NAS Share" button
    tool.click_action(By.XPATH, '//div[2]/div[1]/ul/li[5]/a/span')

    # create 4 nas share
    for i in range(len(test_data["pool_id"])):

        # click "Create New NAS Share" button
        tool.click_action(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/div[2]/button')

        # select target Pool
        if test_data["pool_id"] == "0":
            tool.click_action(By.XPATH, '//form/div[1]/div/select/option[1]')
        else:
            tool.click_action(By.XPATH, '//form/div[1]/div/select/option[2]')

        # filling Nas Share name
        tool.fill_action(By.XPATH, '//form/div[2]/div[1]/input', test_data["name"][i])

        if test_data["thin"][i] == 'Enabled':
            # Enable Thin Provision
            tool.click_action(By.XPATH, '//form/div[3]/div/label/span')

        # select capacity unit
        if test_data["unit"] == "GB":
            tool.click_action(By.XPATH, '//form/div[4]/div[1]/div/div[2]/select/option[1]')
        else:
            tool.click_action(By.XPATH, '//form/div[4]/div[1]/div/div[2]/select/option[2]')

        # filling capacity
        tool.fill_action(By.XPATH, '//form/div[4]/div[1]/div/div[2]/input', test_data["capacity"][i])

        # submit
        tool.click_action(By.XPATH, '//div/div[3]/div/div/div[2]/div[2]/button[1]')

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

    create_nas_share()