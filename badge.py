from typing import List
from collections import defaultdict

# Note
# get the count of a list: lst.count()
# sorted() will sort in place
# iterate through dictionary using items()
class Badge:
    def check_entry_exit(self, records: List[List[str]]):
        inside = {}
        enter_wo_exit = set()
        exit_wo_enter = set()

        for name, state in records:
            if state == "enter":
                if inside.get(name, False):
                    enter_wo_exit.add(name)
                inside[name] = True
            elif state == "exit":
                if not inside.get(name, False):
                    exit_wo_enter.add(name)

        for name, state in inside:
            if state:
                enter_wo_exit.add(name)

            
    # def check_entry_exit(self, records: List[List[str]]):
    #     enter_wo_exit = []
    #     exit_wo_enter = []
    #     mapping = {}
    #     for record in records:
    #         if record[0] not in mapping:
    #             mapping[record[0]] = [record[1]]
    #         else:
    #             mapping[record[0]].append(record[1])
        
    #     for key, val in mapping.items():
    #         if len(val) == 1:
    #             if val[0] == "enter":
    #                 enter_wo_exit.append(key)
    #             else:
    #                 exit_wo_enter.append(key)
    #         else:
    #             if val.count("enter") > val.count("exit"):
    #                 enter_wo_exit.append(key)
    #             elif val.count("enter") < val.count("exit"):
    #                 exit_wo_enter.append(key)
    #             else:
    #                 for i in range(len(val)):
    #                     if val[i] == val[i+1]:
    #                         enter_wo_exit.append(key)
    #                         exit_wo_enter.append(key)
    #                         break
        
    #     print("enter without exit, ", enter_wo_exit)
    #     print("exit without enter, ", exit_wo_enter)

if __name__ == "__main__":
    records1 = [
        ["Paul", "enter"],
        ["Pauline", "exit"],
        ["Paul", "enter"],
        ["Paul", "exit"],
        ["Martha", "exit"],
        ["Joe", "enter"],
        ["Martha", "enter"],
        ["Steve", "enter"],
        ["Martha", "exit"],
        ["Jennifer", "enter"],
        ["Joe", "enter"],
        ["Curtis", "exit"],
        ["Curtis", "enter"],
        ["Joe", "exit"],
        ["Martha", "enter"],
        ["Martha", "exit"],
        ["Jennifer", "exit"],
        ["Joe", "enter"],
        ["Joe", "enter"],
        ["Martha", "exit"],
        ["Joe", "exit"],
        ["Joe", "exit"]
    ]

    records2 = [
        ["Paul", "enter"],
        ["Paul", "exit"],
    ]

    records3 = [
        ["Paul", "enter"],
        ["Paul", "enter"],
        ["Paul", "exit"],
        ["Paul", "exit"],
    ]

    records4 = [
        ["Raj", "enter"],
        ["Paul", "enter"],
        ["Paul", "exit"],
        ["Paul", "exit"],
        ["Paul", "enter"],
        ["Raj", "enter"],
    ]

    badge = Badge()
    enter_wo_exit, exit_wo_enter = badge.check_entry_exit(records1)
    print(sorted(exit_wo_enter))
    # assert sorted(exit_wo_enter) == ["Curtis", "Joe", "Martha", "Pauline"]
    # assert sorted(enter_wo_exit) == ["Curtis", "Joe", "Paul", "Steve"]
