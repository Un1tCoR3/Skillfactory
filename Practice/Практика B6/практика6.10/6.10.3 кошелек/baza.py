from wallet import Wallet

account = Wallet("Иван Иванов", 50)
print(*account.get_account_info())