from utility.node import Node

my = Node()

while (True):
    cmd = input('Vui lòng nhập lệnh:')
    if cmd == 'quit':
        break;
    if cmd == 'transfer':
        if my.transfer():
            print('Chuyển tiền thành công')
        else:
            print('Chuyển tiền thất bại')
        continue
    if cmd == 'mine':
        my.blockchain.mine()
        continue
    if cmd == 'check':
        print([block.__dict__ for block in my.blockchain.get_data()])
    if cmd == 'balance':
        print(my.check_balance())