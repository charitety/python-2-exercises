from dataclasses import dataclass


@dataclass(frozen=False, order=True)
class Invoice:
    invoice_id = str
    user_id = str
    amount = str
    paid = str

    def convert_data(self):
        return [self.__class__()]

