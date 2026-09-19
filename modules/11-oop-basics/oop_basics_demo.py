# Module 11 — OOP Basics
# Run: python oop_basics_demo.py
#
# SCHOOL: A class is a blueprint. An object is one real thing built from that blueprint.
# WORK: Enterprise domain models (Order, User), HTTP clients, metric exporters,
#       FastAPI+Pydantic models, AI Pipeline stages — all use this idea.

class Dog:
    # SCHOOL: __init__ runs when you create Dog("Rex", 3) — setup time.
    # WORK: same as Client(base_url, timeout) or Exporter(endpoint, api_key).
    def __init__(self, name, age):
        # SCHOOL: self = THIS dog. Store name/age on it for later methods.
        self.name = name
        self.age = age

    def bark(self):
        # SCHOOL: a method = action this object can do, using its own data.
        # WORK: client.get(), exporter.flush(), session.refresh_token().
        return f"{self.name} says woof!"

    def birthday(self):
        # SCHOOL: objects can change over time.
        # WORK: breaker.open(); buffer.size += 1; cache.invalidate().
        self.age += 1


class BankAccount:
    """SCHOOL: money rules live WITH the balance — safer than loose variables.
    WORK: Same pattern as RateLimiter, TokenBucket, CircuitBreaker, ConnectionPool.
    """

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        # SCHOOL: _balance means "please use methods, don't poke raw value."
        # WORK: encapsulation — hide internals so API stays stable (enterprise).
        self._balance = float(balance)

    def deposit(self, amount):
        # SCHOOL: refuse nonsense amounts.
        # WORK: validate at the boundary — like FastAPI/Pydantic, or reject bad metric samples.
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount

    @property
    def balance(self):
        # SCHOOL: read as account.balance but still controlled.
        # WORK: read-only views of internal state (pool.size, breaker.state).
        return self._balance

    def __str__(self):
        # SCHOOL: controls print(account).
        # WORK: useful __str__/__repr__ for logs during incidents.
        return f"BankAccount({self.owner!r}, balance={self._balance:.2f})"


def main():
    # SCHOOL: build one dog from the blueprint and use it.
    rex = Dog("Rex", 3)
    print(rex.bark())
    rex.birthday()
    print(f"{rex.name} is now {rex.age}")

    # SCHOOL: bank demo = same OOP idea with stricter rules.
    # WORK: imagine ApiClient with get/post and guarded timeouts instead of money.
    acct = BankAccount("Ada", 100)
    acct.deposit(50)
    acct.withdraw(30)
    print(acct)
    print("Balance property:", acct.balance)


# SCHOOL: only auto-run demo when THIS file is executed.
# WORK: libraries import classes without side effects — required in enterprise packages.
if __name__ == "__main__":
    main()
