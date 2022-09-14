from utility.node import Node

me = Node()

while (True):
    cmd = input('Vui lòng nhập lệnh:')
    if cmd == 'quit':
        break;
    if cmd == 'transfer':
        if me.transfer():
            print('Chuyển tiền thành công')
        else:
            print('Chuyển tiền thất bại')
        continue
    if cmd == 'mine':
        me.blockchain.mine()
        continue
    if cmd == 'check':
        print([block.__dict__ for block in me.blockchain.get_data()])
    if cmd == 'balance':
        print(me.check_balance())
    if cmd == 'wallet':
        subcmd = input('Nhập lệnh: ')
        if (subcmd == 'create'):
            wallet = me.create_wallet()
        if (subcmd == 'load'):
            pass
        