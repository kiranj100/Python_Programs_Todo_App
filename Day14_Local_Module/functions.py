def get_read_lines(filepath="todo.txt") :
    with open(filepath,"r") as file:
        set_user_list = file.readlines()
    return set_user_list

 # non default parameter put first place and second place is default parameter this is right way
def get_write_lines(user_list_argument, filepath="todo.txt"):
    with open(filepath,'w') as file :
        file.writelines(user_list_argument)

