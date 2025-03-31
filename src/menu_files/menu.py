from requests.models import Response
from util.login import login
import util.delete as delete
import util.create as create
import colorama as clr


def menu_list():
    clr.init(autoreset=True)
    __token_data__: Response = {}

    while True:
        __token_data__ = login()

        if "error" in __token_data__:
            print(clr.Back.RED + "LOGIN FAILED!")
            for key, val in __token_data__.items():
                print(f"{clr.Fore.RED}{key}: {val}")
        else:
            print(f"{clr.Back.GREEN}LOGIN SUCCESSFUL!")
            break

    print("'help' for help.")

    usr_cmd = input(">> ")
    usr_cmd = usr_cmd.lower() if (usr_cmd.isalpha()) else usr_cmd
    while usr_cmd != "exit":
        if usr_cmd == "login":
            temp = login()
            if "accessToken" in temp:
                __token_data__ = temp
                print(f"{clr.Back.GREEN}SUCCESS!")
            else:
                print(f"{clr.Back.RED}FAILED!")
                for key, val in __token_data__.items():
                    print(f"{clr.Fore.RED}{key}: {val}")
        elif usr_cmd == "delete receive":
            delete.receive(__token_data__["accessToken"])
        elif usr_cmd == "delete supship":
            delete.supship(__token_data__["accessToken"])
        elif usr_cmd == "create supship":
            create.supship(__token_data__["accessToken"])
        elif usr_cmd == "help":
            help = """# Commands:
        |    \'login\'              : To change current logged in user.
        |    \'delete <sub_cmd>\'   : To delete \'receive\' or \'supship\' CTEs.
        |    \'create supship\'     : To create supship CTE.
        |    \'help\'               : To show all the valid commands.
        |    \'exit\'               : To exit the program."""
            print(help)
        else:
            print("Command not found.")

        usr_cmd = input(">> ")
        usr_cmd = usr_cmd.lower() if (usr_cmd.isalpha()) else usr_cmd
    return 0
