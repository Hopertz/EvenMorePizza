class MainProgram:
    def __init__(self):
        pass

    @staticmethod
    def PizzaDelivery(evenmorepizza):
        delivaries = []
        output = OutPutFile()
        i = 0
        while i < evenmorepizza.available_pizza:
            pizzaindx = []
            if evenmorepizza.team_of_two != 0:
                try:
                  pizzaindx.append(evenmorepizza.pizzaIng[i].id)
                  pizzaindx.append(evenmorepizza.pizzaIng[i + 1].id)
                  delivaries.append(Delivery(2, pizzaindx))
                  output.Delivery = delivaries
                  evenmorepizza.team_of_two -= 1
                  i += 2
                  continue
                except IndexError:
                    pass
            elif evenmorepizza.team_of_three != 0:
                try:
                  pizzaindx.append(evenmorepizza.pizzaIng[i].id)
                  pizzaindx.append(evenmorepizza.pizzaIng[i + 1].id)
                  pizzaindx.append(evenmorepizza.pizzaIng[i + 2].id)
                  delivaries.append(Delivery(3, pizzaindx))
                  output.Delivery = delivaries
                  evenmorepizza.team_of_three -= 1
                  i += 3
                  continue
                except IndexError:
                    pass
            elif evenmorepizza.team_of_four != 0:
                try:
                   pizzaindx.append(evenmorepizza.pizzaIng[i].id)
                   pizzaindx.append(evenmorepizza.pizzaIng[i + 1].id)
                   pizzaindx.append(evenmorepizza.pizzaIng[i + 2].id)
                   pizzaindx.append(evenmorepizza.pizzaIng[i + 3].id)
                   delivaries.append(Delivery(4, pizzaindx))
                   output.Delivery = delivaries
                   evenmorepizza.team_of_four -= 1
                   i += 4
                   continue
                except IndexError:
                    pass
            i += 1
        output.DeliveredPizza = len(delivaries)
        return output

    @staticmethod
    def WriteOutputFile(output):
        createText = f"{output.DeliveredPizza}\n"
        for op in output.Delivery:
            createText += f"{op.TeamType} {' '.join(str(i) for i in op.Pizza)}\n"

        with open("_Output.txt", 'w') as out:
            out.write(createText)

    @staticmethod
    def ReadInputFile(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

        line = lines[0].rstrip()

        fline = line.split(' ')
        aPizza = int(fline[0])
        T2 = int(fline[1])
        T3 = int(fline[2])
        T4 = int(fline[3])
        pings = []
        for i in range(1, len(lines)):
            otherLines = lines[i].rstrip().split(' ')
            ping = PizzaIng(i - 1, otherLines[0], otherLines[1:])
            pings.append(ping)
        emp = EvenMorePizza(aPizza, T2, T3, T4, pings)
        return emp


class EvenMorePizza:
    def __init__(self, available_pizza, team_of_two, team_of_three, team_of_four, pizzaIng):
        self.available_pizza = available_pizza
        self.team_of_two = team_of_two
        self.team_of_three = team_of_three
        self.team_of_four = team_of_four
        self.pizzaIng = pizzaIng


class OutPutFile:
    def __init__(self, DeliveredPizza=0, Delivery=None):
        self.DeliveredPizza = DeliveredPizza
        self.Delivery = Delivery


class Delivery:
    def __init__(self, TeamType, Pizza):
        self.TeamType = TeamType
        self.Pizza = Pizza


class PizzaIng:
    def __init__(self, id, no_of_ingridents, list_of_ingridents):
        self.id = id
        self.no_of_ingridents = no_of_ingridents
        self.list_of_ingridents = list_of_ingridents


program = MainProgram()
output = program.ReadInputFile('e_many_teams.in')
new_output = program.PizzaDelivery(output)
program.WriteOutputFile(new_output)
