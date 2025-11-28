from utils import llm_call

class BaseAgent:
    def __init__(self, name, role, goal, backstory):
        self.name = name
        self.role = role
        self.goal = goal
        self.backstory = backstory

    def act(self, context):
        raise NotImplementedError


class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Researcher",
            role="Research Specialist",
            goal="Pesquisar informações factuais e recentes sobre o tema.",
            backstory="Um analista experiente em coletar dados e organizar fatos."
        )

    def act(self, context):
        topic = context.get("topic", "Inteligência Artificial na Engenharia de Software")

        prompt = f"""
        Liste 5 pontos importantes, com explicações curtas, sobre o tema:
        "{topic}".

        Formato:
        - Título do ponto
        - 2 frases explicando
        """

        result = llm_call(prompt)
        return {"research_output": result}


class CuratorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Curator",
            role="Content Curator",
            goal="Transformar a pesquisa em uma estrutura organizada.",
            backstory="Um editor experiente em sintetizar e estruturar conteúdo técnico."
        )

    def act(self, context):
        research = context.get("research_output", "")

        prompt = f"""
        A partir da pesquisa abaixo, crie um OUTLINE (estrutura) de artigo técnico:

        Pesquisa:
        {research}

        Formato:
        # Título
        ## Introdução
        ## Seção 1
        ## Seção 2
        ## Seção 3
        ## Conclusão
        """

        result = llm_call(prompt)
        return {"outline_output": result}


class WriterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Writer",
            role="Content Writer",
            goal="Escrever artigo final em markdown.",
            backstory="Redator técnico especializado em IA."
        )

    def act(self, context):
        outline = context.get("outline_output", "")

        prompt = f"""
        Usando o outline abaixo, escreva um ARTIGO COMPLETO em markdown
        com ~900 palavras.

        Outline:
        {outline}
        """

        result = llm_call(prompt, max_tokens=1500)
        return {"article_output": result}
