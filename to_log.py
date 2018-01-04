import time


def tolog(str_info):

        if str_info != "'result': 'p'" or str_info != "'result': 'f'":

            with open("./gui_scripts.log", "r+") as f:
                content = f.read()
                f.seek(0, 0)
                f.write(time.strftime('%Y-%m-%d %H:%M:%S',
                                      time.localtime(time.time())) + ": " + str_info + '\n' + content)

                f.close()
            print(str_info)

        # for testlink steps populate
        fout = open("./testlink.notes", "a")
        fout.write(str_info + '\n')

        fout.close()