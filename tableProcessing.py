
def processTable(table, query, required_words, words_to_avoid, show_private, sort, ascending):
    """Process the table and return only relevant entries"""

    # Filter the results to find the relevant repositories based on custom criteria
    table = table.sort_values(by=sort, ascending=ascending)
    table = table.reset_index(drop=True)

    # Remove duplicates
    table = table.drop_duplicates(subset=["Name", "Repository Name", "Created Date", "Language", "Stars", "Watchers", "Forks Count", "Score", "Private", "Owner Name", "URL", "Description", "Size"], keep="first")
    table = table.reset_index(drop=True)

    # Remove private repositories
    if not show_private:
        table = table[table["Private"] == False]
    
    # Remove repositories that do not contain all of the required_words or have no description
    

    if len(required_words) > 0:
        table = table[table["Description"].notna()]

    for word in required_words:
        # Search for the word in the description, the name or the topics
        table = table[table["Description"].str.contains(word, case=False) | table["Name"].str.contains(word, case=False) | table["Topics"].str.contains(word, case=False)]


    # Remove repositories that contain words to avoid
    for word in words_to_avoid:
        # Search for the word in the description, the name or the topics
        table = table[~table["Description"].str.contains(word, case=False) & ~table["Name"].str.contains(word, case=False) & ~table["Topics"].str.contains(word, case=False)]

    return table

