# -*- coding: utf-8 -*-

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

    # precondition()

    tool = GUITestTool()

    # test date
    test_data = {
        "pool": ['[1]', '[1]', '[2]', '[2]'],
        "name": ['1', 'T2', 't_1'*10, '_'*31],
        "thin": ['/span', '', '/span', ''],
        "unit": ['[1]', '[1]', '[2]', '[2]'],
        "capacity": ['1', '2', '1', '2']
    }
    # check data
    check_data = {
        "pool_name": ['T_NAS_pool_0', 'T_NAS_pool_0', 'T_NAS_pool_1', 'T_NAS_pool_1'],
        "thin_prov": ['Enabled', 'Disable', 'Enabled', 'Disable'],
        "capacity": ['1 GB', '2 GB', '1 TB', '2 TB']
    }

    # click "NAS Share" button
    tool.click_action('//div[2]/div[1]/ul/li[5]/a/span')

    for i in range(len(test_data["pool"])):

        # click "Create New NAS Share" button
        tool.click_action('/html/body/div[1]/div/div[3]/div[1]/div/div[2]/button')

        # select target Pool
        tool.click_action('//form/div[1]/div/select/option' + test_data["pool"][i])

        # filling Nas Share name
        tool.fill_action('//form/div[2]/div[1]/input', test_data["name"][i])

        if test_data["thin"][i] != '':
            # Enable Thin Provision
            tool.click_action('//form/div[3]/div/label' + test_data["thin"][i])

        # select capacity unit
        tool.click_action('//form/div[4]/div[1]/div/div[2]/select/option' + test_data["unit"][i])

        # filling capacity
        tool.fill_action('//form/div[4]/div[1]/div/div[2]/input', test_data["capacity"][i])

        # submit
        tool.click_action('//div/div[3]/div/div/div[2]/div[2]/button[1]')

        nas_info = server.webapi('get', 'nasshare/' + str(i))

        if isinstance(nas_info, dict):

            info = json.loads(nas_info["text"])[0]

            if info["name"] != test_data["name"][i]:

                tool.FailFlag = True
                tolog('Fail: please check out: ' + test_data["name"][i])

            elif info["pool_name"] != check_data["pool_name"][i]:

                tool.FailFlag = True
                tolog('Fail: please check out: ' + check_data["pool_name"][i])

            elif info["thin_prov"] != check_data["thin_prov"][i]:

                tool.FailFlag = True
                tolog('Fail: please check out: ' + check_data["thin_prov"][i])

            elif info["total_capacity"] != check_data["capacity"][i]:

                tool.FailFlag = True
                tolog('Fail: please check out: ' + check_data["capacity"][i])

        tool.mark_status()

    tool.finished()

    return tool.FailFlag


if __name__ == "__main__":

    create_nas_share()