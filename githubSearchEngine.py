import getDataFromGitHub as gdg
import tableProcessing as tproc
import pandas as pd

# The focus of this proyect is to obtain relevant data related to a given topic.
# How do we know what repositories are relevant? We want to value the repositories based 
# on the value they provide to the community.
# We can use the following criteria:
# - Number of stars
# - Number of watchers
# - Number of forks
# - Topics
# - Size
# - Language
# - Description
# - File types



def githubSearchEngine(query, required_words, words_to_avoid, show_private, sort, ascending, entries_per_page, page, max_pages):

    # query= "summarizer"
    # required_words = []
    # words_to_avoid = []
    # show_private = False
    # sort = "Stars"
    # ascending = False
    # entries_per_page = 100
    # page = 0
    # max_pages = 5
    
    # total_count = -1
    # total_pages = 20

    current_datetime = pd.to_datetime("today").strftime("%Y-%m-%d_%H-%M-%S")

    document_name = f"{query}_{current_datetime}_rw_{required_words}_av_{words_to_avoid}_mp_{max_pages}"
    
    table = pd.DataFrame(columns=["Name","Repository Name", "Created Date","Language", "Stars","Watchers","Forks Count","Score","Topics","Private","Owner Name", "URL", "Description","Size"])

    # Obtain the github query results
    while page <= total_pages and page != max_pages:
        table, metadata  = gdg.getData(table, query, page, entries_per_page)

        if total_count == -1:
            total_count = metadata["Total Count"]
            if total_count > 1000:
                total_count = 1000
            total_pages = total_count // entries_per_page
  
        page += 1

        print(f"Page {page} of {total_pages}")

    # Filter the results to find the relevant repositories based on custom criteria
    table = tproc.processTable(table, query,required_words, words_to_avoid, show_private, sort, ascending)


    # Save results in an excel file
    table.to_excel(f"./Results/Excel/{document_name}.xlsx", index=False)

    table_show = table.loc[:,["Name","Description","Topics","URL","Stars","Watchers","Forks Count","Created Date","Language","Size"]]

    # Create html file with the results, add links to the "URL" column
    table_show.to_html(f"./Results/HTML/{document_name}.html", index=False, escape=False, formatters={"URL": lambda x: f'<a href="{x}">{x}</a>'})
    

    

    # open html file
    import webbrowser

    webbrowser.open(f"Results\HTML\{document_name}.html")





