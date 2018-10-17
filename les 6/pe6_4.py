def nieuw_password(oldpassword,newpassword):
    if newpassword != oldpassword and len(newpassword) >= 6:
        print('True')

    else:
        print('False')

print (nieuw_password('langebroek','heidelberglaan'))