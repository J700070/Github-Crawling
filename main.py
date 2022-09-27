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



def main():

    query= "python"
    required_words = ["book", "science"]
    words_to_avoid = []
    show_private = False
    sort = "Stars"
    ascending = False
    entries_per_page = 100
    page = 0
    max_pages = 20
    
    total_count = -1
    total_pages = 10

    table = pd.DataFrame(columns=["Name","Repository Name", "Created Date","Language", "Stars","Watchers","Forks Count","Score","Topics","Private","Owner Name", "URL", "Description","Size"])

    # Obtain the github query results
    while page <= total_pages and page != max_pages:
        table, metadata  = gdg.getData(table, query, page, entries_per_page)

        if total_count == -1:
            total_count = metadata["Total Count"]
            total_pages = total_count//entries_per_page
        page += 1

        print(f"Page {page} of {total_pages}")

    # Filter the results to find the relevant repositories based on custom criteria
    table = tproc.processTable(table, query,required_words, words_to_avoid, show_private, sort, ascending)

    # Save results in a csv file
    table.to_csv("results.csv", index=False) 


    print(table.loc[:,["Name","Repository Name","Stars","Watchers","Forks Count","Score","Private","Description"]])







if __name__ == "__main__":
    main()
