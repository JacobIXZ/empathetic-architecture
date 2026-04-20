import random

class Agent:
    def __init__(self, agent_id: int):
        self.id = agent_id
        self.hunger = random.randint(20, 50)
        self.energy = 100
    
    def step(self) -> None:
        self.hunger += 5
        self.energy -= 1
        print(f"Agent {self.id} | Hunger: {self.hunger} | Energy: {self.energy}")

class Simulation:
    def __init__(self, num_agents: int):
        self.agents = [Agent(i) for i in range(num_agents)]
        self.step_count = 0

    def step(self) -> None:
        print(f"\n--- Step {self.step_count} ---")
        for agent in self.agents:
            agent.step()
        self.step_count += 1

def main() -> None:
    sim = Simulation(3)
    for _ in range(10):
        sim.step()

if __name__ == "__main__":
    main()