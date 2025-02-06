from dotenv import load_dotenv

from browser_agent.app.projects.xhandles.tasks.search_x_prospects import search_prospects
load_dotenv()

def main():
	task = search_prospects.delay()

	print(task)


if __name__ == "__main__":
    main()