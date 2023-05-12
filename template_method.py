from abc import ABC, abstractmethod


class SalesReport:
    """
    The problem is about duplicate code
    """

    def __init__(self, company, sales):
        self.company = company
        self.sales = sales

    def make_report(self):
        print("** REPORT HEADING **")
        print("Company: ", self.company)
        print("********************")
        print("Sales: ", self.sales)


class CostsReport:
    def __init__(self, company, costs):
        self.company = company
        self.costs = costs

    def make_report(self):
        print("** REPORT HEADING **")
        print("Company: ", self.company)
        print("********************")
        print("Consts: ", self.costs)


def run_simple_idea():
    sales_report = SalesReport("Google", 2000)
    sales_report.make_report()

    costs_report = CostsReport("Amazon", 5000)
    costs_report.make_report()


class Report:
    def make_report(self):
        print("** REPORT HEADING **")
        print("Company: ", self.company)
        print("********************")


class SalesReportSuperCall(Report):
    def __init__(self, company, sales):
        self.company = company
        self.sales = sales

    def make_report(self):
        super().make_report()
        print("Sales: ", self.sales)


class CostsReportSuperCall(Report):
    def __init__(self, company, costs):
        self.company = company
        self.costs = costs

    def make_report(self):
        super().make_report()
        print("Consts: ", self.costs)


def test_supper_call_idea():
    """
    Call Super Anti-Pattern

    Call super is an anti-pattern in which a particular class stipulates that in a
    derived class, the programmer is required to override a method and call back
    the overriden method itself at a particular poit.
    Because derived class HAVE TO call a method of super class.

    There is nothing wrong with a derived class method using a base class method. But
    *requiring* is an anti-pattern, as it will not be enforced by a language feature.
    allowing mistakes to occur.
    """
    print()
    sales_report = SalesReportSuperCall("Google", 2000)
    sales_report.make_report()

    costs_report = CostsReportSuperCall("Amazon", 5000)
    costs_report.make_report()


class ReportTemplateMethod(ABC):
    @abstractmethod
    def make_report_body(self):
        pass

    def make_report(self):
        print("** REPORT HEADING **")
        print("Company: ", self.company)
        print("********************")
        self.make_report_body()


class SalesReportTemplateMethod(ReportTemplateMethod):
    def __init__(self, company, sales):
        self.company = company
        self.sales = sales

    def make_report_body(self):
        print("Sales: ", self.sales)


class CostsReportTemplateMethod(ReportTemplateMethod):
    def __init__(self, company, costs):
        self.company = company
        self.costs = costs

    def make_report_body(self):
        print("Consts: ", self.costs)


def test_template_method_idea():
    """
    Template Method Design Pattern

    A template method is defined in a base class and it implements an overarching 'template'
    for an algorithm made up of higher-level steps, in-part by using 'helper method' that
    will be implemented by derived classes to accomplish more specific functionalities.
    """
    print()
    sales_report = SalesReportTemplateMethod("Google", 2000)
    sales_report.make_report()

    costs_report = CostsReportTemplateMethod("Amazon", 5000)
    costs_report.make_report()
