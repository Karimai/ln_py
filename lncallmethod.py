class Pay:
    def __init__(self, amount):
        self.pay = amount
        print("Initialized: ", amount)

    def __call__(self, *args, **kwargs):
        print("Called by: ", args[0])
        self.pay = args[0]


pay = Pay(10)  # __init__ will be called

pay(25)  # __call__ will be called


