class Printer:
    def print_text(self):
        pass

class OldPrinter:
    def print_old(self):
        return "Печать через старый принтер"

class PrinterAdapter(Printer):
    def _init(self, old_printer):
        self.old_printer = old_printer

    def print_text(self):
        return self.old_printer.print_old()

printer = PrinterAdapter(OldPrinter())
print(printer.print_text())
