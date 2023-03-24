#DE FORMA INCORRECTA CON IF
#def call_cost_caulcuale(call):
#   cost = 0
#    if call.is_local():
#        cost = calculate_local_cost_of(call)
#    elif call.is_national():
#        cost = calculate_national_cost_of(call)
#    elif call.is_international():
#        costcalculate_international_cost_of(call)
#    return cost

#DE FORMA CORRECTA SIN IF
class CallCostCalculator(object):   #Superclase

    @classmethod
    def to_handle(klass,call):
        #codigo que busca el CostCallCalculator correspondiente.
        return
    
    def calculate(self):
        raise NotImplementedError("Subclass Rsponsability")

class LocalCallCostCalculator(CallCostCalculator): #Subclase
    def calculate(self):
        #codigo de calculate_local_cost_of 
        return 
    
class NationalCallCostCalculator(CallCostCalculator): #Subclase
    def calculate(self):
        #codigo de calculate_national_cost_of  
        return

class InternationalCallCostCalculator(CallCostCalculator): #Subclase
    def calculate(self):
        #codigo de calcultate_intenaitional_cost_of
        return

cost_calculator = CallCostCalculator.to_handle(call)
cost_calculator.calculate()