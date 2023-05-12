class Worker:

    def __init__(self, name: str):
        self.name = name
        print("Has been inited!")

    def __call__(self, *args, **kwargs):
        self.age = args[0]
        print("has been called!")


if __name__ == "__main__":
    print("Let's start")
    worker = Worker("Karim")
    print("before call")
    worker(41)
    print("##############")
