#nabulo shantal hilda m24b13/008
#muyobo arnold m24b13/024
# kyazze angella m24b13/041

#visitor class

class visitor:
    def __init__(self,name,id):
        self.name = name
        self.id = id

#resident class

class resident:
    def __init__(self,name,room):
        self.name = name
        self.room = room

#Hostel class

class Hostel:
    def __init__(self,name):
        self.name = name
        self.visits = []

    def record_visit(self, visitor, resident):
        self.visits.append((visitor, resident))
    def show_visits(self):
        for visitor, resident in self.visits:
        
         
         print(f"{visitor.name} (ID: {visitor.id}) visited {resident.name} in room {resident.room}")

visitor1 = visitor("Alice", "V123")
resident1 = resident("Bob", "12B")
hostel = Hostel("UCU Hostel")

hostel.record_visit(visitor1, resident1)
hostel.show_visits()

        
