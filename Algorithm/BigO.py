
#使用大O表示法给出下述各种情形的运行时间。
Names = ['Alyx', 'Python', 'BigO', 'Lucy', 'Max', 'Martin', 'Arthur', 'Ciri', 'Jane', 'John', 'Mary', 'Michael', 'Davia', 'Thomas', 'Lisa', 'Seven', 'Anna', 'Jack', 'Alice', 'Rose', 'Fran', 'Leo', 'William', 'Maya', 'Victoria', 'Ailee', 'Alex', 'Gianna', 'Weston', 'Jose', 'August', 'Richard', 'Nico', 'Elian', 'Otto', 'Taylor', 'Tommy', 'Violet']
Phones = ['+8617382120012', '+14844731143', '+15853042442', '+16102458163', '+16102458163', '+15853042386', '+18777405932', '+18665445994', '+436703080042', '+436703080013', '+436703080051', '+447441429277', '+447520644202', '+447441429227', '+441245969018', '+442037699224', '+442038850794', '']
#1.3 在电话簿中根据名字查找电话号码。
def set_1():
    name = input('Please inpuut the name:')
    find = False
    for i in Names:
        if i == name:
            find = True
            print('Found! Total counts {} frequency.'.format(i))
            break
    if not find:
        print('Invalue Name.')
#1.4 在电话簿中根据电话号码找人。（提示：你必须查找整个电话簿。)
#1.5 阅读电话簿中每个人的电话号码。
#1.6 阅读电话簿中姓名以A打头的人的电话号码。这个问题比较棘手，它涉及第4章的概念。答案可能让你感到惊讶！


def main():
    pass

if __name__ == '__main__':
    main()