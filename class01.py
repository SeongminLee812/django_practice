class Account:
	def __init__(self, name):
		print('[init start]객체가 생성됩니다.')
		self.name = name
		self.money = 10000
		print('[init end]객체가 생성되었습니다.')
	
	def deposit(self, money):
		print(f'[deposit start]돈을 입금합니다. {money}원')
		self.money = self.money + money
		print(f'[deposit end]돈을 입금했습니다.{money}원')

	def withdraw(self, money):
		print(f'[withdraw start]돈을 출금합니다.{money}원')
		self.money = self.money - money
		print(f'[withdraw end]돈을 출금했습니다.{money}원')
		return money
	
	def print_balance(self):
		print('[print_balance start]잔고를 출력합니다.')
		print('잔고 :', self.money)
		print('[print_balance end]잔고를 출력했습니다.')
	
	def print_owner(self):
		print('[print_owner start]소유자를 출력합니다.')
		print('소유자 :', self.name)
		print('[print_owner end]소유자를 출력했습니다.')

account = Account('홍길동')

account.deposit(200000)

withdrawed = account.withdraw(150000)
print('출금액', withdrawed)

account.print_balance()

account.print_owner()




