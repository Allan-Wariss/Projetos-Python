user = input('Escreva seu usuario: ')
password = input('Escreva sua senha: ')

def register():
    global user, password
    with open('../Trabalho 2/users.txt', 'a')  as archiveUsers:
                archiveUsers.write(user + '\n')
    with open('../Trabalho 2/passwords.txt', 'a')  as archivePasswords:
                archivePasswords.write(password + '\n')

def login():
    global user, password
    with open('../Trabalho 2/users.txt', 'r') as archiveUsers:
        users = archiveUsers.readlines()
    with open('../Trabalho 2/passwords.txt', 'r') as archivePasswords:
        passwords = archivePasswords.readlines()

    users = list(map(lambda x: x.replace('\n', ''), users))
    passwords = list(map(lambda x: x.replace('\n', ''), passwords))

    logged = False

    for i in range(len(users)):
        if user == users[i] and password == passwords[i]:
            logged = True
            print('usuário logado')

    if not logged:
        print('usuário inválido')



