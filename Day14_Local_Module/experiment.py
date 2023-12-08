def get_read_lines(filepath="todo.txt") :
    with open(filepath,"r") as file:
        set_user_list = file.readlines()
    return set_user_list

 # non default parameter put first place and second place is default parameter this is right way
def get_write_lines(user_list_argument, filepath="todo.txt"):
    with open(filepath,'w') as file :
        file.writelines(user_list_argument)

# without condition its execute other class also where experiment.py is imported
# prevent of execution use condition like this
# when file is run directly we can control which function or output we want
# to show there

if __name__ == '__Modules__' :
    print("hello")
    print(get_write_lines())