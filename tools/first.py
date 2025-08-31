from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

ans = search.invoke('current big boss news')

print(ans)