class VacuumCleanerAgent:
    def __init__(self, state):
            self.state = state
            self.buffer = self.initialize_buffer()
            self.performanceA=0
            self.performanceB=0
            
    def initialize_buffer(self):
        return {
            ("A", 0, 0): "Both rooms are clean.",
            ("A", 0, 1): "Room A clean, Room B dirty.",
            ("A", 1, 0): "Room A dirty, Room B clean.",
            ("A", 1, 1): "Both rooms dirty.",
            ("B", 0, 0): "Both rooms are clean.",
            ("B", 0, 1): "Room A clean, Room B dirty.",
            ("B", 1, 0): "Room A dirty, Room B clean.",
            ("B", 1, 1): "Both rooms dirty.",
        }
    
            
    def suck(self):
        if self.state[0] == "A" and self.state[1] == 1:
            self.state = ("A", 0, self.state[2])
            print(f"Sucked dirt in Room A. New state: {self.state}")
            self.performanceA+=1
            
        elif self.state[0] == "B" and self.state[2] == 1:
            self.state = ("B", self.state[1], 0)
            print(f"Sucked dirt in Room B. New state: {self.state}")
            self.performanceB+=1

    def move_left(self):
        if self.state[0] == "B":
            self.state = ("A", self.state[1], self.state[2])
            print(f"Moved left to Room A. New state: {self.state}")

    def move_right(self):
        if self.state[0] == "A":
            self.state = ("B", self.state[1], self.state[2])
            print(f"Moved right to Room B. New state: {self.state}")
        
    def clean(self):
        while self.state[1] == 1 or self.state[2] == 1:
            print(f"Current state: {self.state} - {self.buffer[self.state]}")
            if self.state[0] == "A" and self.state[1] == 1:
                self.suck()
            elif self.state[0] == "B" and self.state[2] == 1:
                self.suck()
            elif self.state[0] == "A" and self.state[2] == 1:
                self.move_right()
            elif self.state[0] == "B" and self.state[1] == 1:
                self.move_left()
        print(f"Final state: {self.state} - {self.buffer[self.state]}")
        if self.state[1] == 0 and self.state[2] == 0:
            print("Both rooms are cleaned.\n")
            
        print(f"Performance measure:")
        print(f"Performance Measure of A: {self.performanceA}")
        print(f"Performance Measure of B: {self.performanceB}")

agent_position = input("Enter the position of agent (A or B): ").strip().upper()
room_a_status = int(input("Enter 1 if room A is dirty else 0: ").strip())
room_b_status = int(input("Enter 1 if room B is dirty else 0: ").strip())
initial_state = (agent_position, room_a_status, room_b_status)
print("INITIAL STATE", initial_state)

agent = VacuumCleanerAgent(initial_state)
agent.clean()
