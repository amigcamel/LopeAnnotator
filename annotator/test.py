class FakeRequest:

    class FakeUser:
        pass

    def __init__(self):
        self.user = self.FakeUser()
        self.user.username = 'aji@test.com'


if __name__ == '__main__':
    request = FakeRequest()
