from search_tool import search_articles
from summarizer import summarize_text
from report_generator import generate_report

def main():

    query = input("Enter research topic: ")

    print("\nSearching articles...\n")

    articles = search_articles(query)

    # limit number of articles for speed
    articles = articles[:3]

    summaries = []

    for i, article in enumerate(articles):
        print(f"Reading and summarizing article {i+1}...\n")

        try:
            summary = summarize_text(article)
            summaries.append(summary)

        except Exception as e:
            print("Error summarizing article:", e)

    print("\nGenerating final research report...\n")

    report = generate_report(query, summaries)

    print("\n==============================")
    print("      FINAL RESEARCH REPORT")
    print("==============================\n")

    print(report)

    # Save output to file
    with open("research_report.txt", "w", encoding="utf-8") as f:
        f.write(report)


if __name__ == "__main__":
    main()