# Principio aberto/fechado. Aberto para extensões mais fechada para modificações

class Programmer:
    def make(self):
        print('programmer creating code')
class Seller:
    def make(self):
        print('Seller sellings products')
class Rh:
    def make(self):
        print('Human Resorces hiring new devs')

class Company:
    def do_work(self, worker: any) -> None:
        worker.make()

programmer = Programmer()
seller = Seller()
rh = Rh()
company = Company()

company.do_work(programmer)
company.do_work(seller)
company.do_work(rh)