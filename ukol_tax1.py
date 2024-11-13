from abc import ABC, abstractmethod
from enum import Enum
import math 

class EstateType(Enum):
    land = 0.85
    buildingsite = 9
    forrest = 0.35
    garden = 2

class Locality:
    def __init__ (self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property(ABC):
    def __init__ (self, locality):
        self.locality = locality

    @abstractmethod
    def calculate_tax(self):
        pass

class Estate(Property):
       
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
        EstateType.land,
        EstateType.buildingsite,
        EstateType.forrest,
        EstateType.garden,

    def calculate_tax(self):
        type_coefficient = self.estate_type.value

        tax = self.area * type_coefficient * self.locality.locality_coefficient

        return math.ceil(tax)
    
    def __str__(self):
        tax = self.calculate_tax()
        return f"Za pozemek {self.estate_type} zaplaťte daň {tax} Kč."
        
class Residence(Property):  
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        tax = self.area * self.locality.locality_coefficient * 15
        if self.commercial is True:
            tax *= 2
       
        return math.ceil(tax)
    
    def __str__(self):
        tax = self.calculate_tax()
        return f"Za nemovitost {self.commercial} zaplaťte daň {tax} Kč." 

class TaxReport:
    def __init__(self, name, property_list=None):
        self.name = name
        if property_list is None:
            property_list = []
        self.property_list = property_list
        
    def add_property(self, property):
        self.property_list.append(property)

    def calculate_tax(self):
        total_tax = 0
        for property in self.property_list:
            total_tax += property.calculate_tax()
        return total_tax
    
    def list_properties(self):
        for property in self.property_list:
            print(property)

    def __str__(self):
        total_tax = self.calculate_tax()
        return f"Celková daň činí {total_tax} Kč."
                          
lokalita1 = Locality("Manětín", 0.8)
lokalita2 = Locality("Brno", 3)

nemovitost1 = Estate(lokalita1, EstateType.land, 900)
nemovitost2 = Residence(lokalita2, 90, commercial=True)
nemovitost3 = Residence(lokalita1, 120, commercial=False)

tax_report = TaxReport("name")
tax_report.add_property(nemovitost1)
tax_report.add_property(nemovitost2)
tax_report.add_property(nemovitost3)

print(nemovitost1)
print(nemovitost2)
print(nemovitost3)
print(tax_report)
