class Crew:
    def __init__(self, agents):
        self.agents = agents
        self.context = {}

    def run(self, initial_context):
        self.context.update(initial_context)

        for agent in self.agents:
            print(f"\n=== Executando agente: {agent.name} ===")
            try:
                output = agent.act(self.context)
                self.context.update(output)
            except Exception as e:
                print(f"Erro no agente {agent.name}: {e}")

        return self.context
