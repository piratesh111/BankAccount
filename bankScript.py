from bankaccount import MinimumBalanceAccount


accountMin = MinimumBalanceAccount(1500)

result = accountMin.withdraw(400)

if result.is_ok:
    print(result.message, result.value)

