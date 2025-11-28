from agents import ResearcherAgent, CuratorAgent, WriterAgent
from tasks import Crew
import json

def main():
    # Define o tema da crew
    topic = "Como a Inteligência Artificial está transformando o trabalho de desenvolvedores em 2025"

    agents = [
        ResearcherAgent(),
        CuratorAgent(),
        WriterAgent()
    ]

    crew = Crew(agents)

    result = crew.run({"topic": topic})

    article = result.get("article_output", "Nenhum artigo gerado")

    # Salva
    with open("generated_article.md", "w", encoding="utf-8") as f:
        f.write(article)

    with open("crew_context.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print("\nArquivo gerado: generated_article.md")
    print("Contexto salvo em: crew_context.json")


if __name__ == "__main__":
    main()
