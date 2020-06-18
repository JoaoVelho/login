inpt = input('Login [l] or Create account [c]?\n')

if inpt == 'l':
  success = False
  login = input('Type your username:\n')
  password = input('Type your password:\n')
  with open("data.txt") as file:
    for line in file:
      if login in line and password in line:
        success = True
        print('Login feito com sucesso!')
        break
  if success == False:
    print('Login ou senha incorretos!')
else:
  create_pass1, create_pass2 = 1, 2
  while create_pass1 != create_pass2:
    create_login = input('Create a username:\n')
    create_pass1 = input('Create a password:\n')
    create_pass2 = input('Type your password again:\n')
  with open('data.txt', 'a') as file:
    file.write(f'{create_login} {create_pass2}\n')
  print('Conta criada com sucesso!')
  
