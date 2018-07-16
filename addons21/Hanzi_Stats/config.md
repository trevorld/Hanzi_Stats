``fieldToUseForStats`` determines the field (or fields) to be used when finding characters to check against the HSK sets. When using "sortField" (default) it will use the 'Sort Field' field as defined in the deck browser.  Specifying "all" will use all fields.  Specifying a specific field with a number will match the field number found in Manage Note Types -> Fields.  

values: "sortField", "all", "1", "2", "3", ...

``hanziURL`` determines which website to look hanzi characters up at.  Currently the hanzi is appended to the end of the url.  Default is "http://hanzicraft.com/character/".  

values: "http://hanzicraft.com/character/", "http://dict.cn/", "http://characterpop.com/explode/", ...

``categoriesToShow`` determines which categories to show Hanzi statistics for.  Delete any categories you do not want shown.  Default is to show all categories:

    [
    "HSK Level 1", "HSK Level 2", "HSK Level 3",
    "HSK Level 4", "HSK Level 5", "HSK Level 6",
    "Simplified Top 500", "Simplified Top 1000", "Simplified Top 1500", 
    "Simplified Top 2000", "Simplified Top 2500", "Simplified Top 3000", 
    "Simplified Top 3500", "Simplified Top 4000", "Simplified Top 4500", 
    "Simplified Top 5000", "Simplified Top 5500", "Simplified Top 6000", 
    "Traditional Top 500", "Traditional Top 1000", "Traditional Top 1500", 
    "Traditional Top 2000", "Traditional Top 2500", "Traditional Top 3000", 
    "Traditional Top 3500", "Traditional Top 4000", "Traditional Top 4500", 
    "Traditional Top 5000", "Traditional Top 5500", "Traditional Top 6000",
    "Unlisted"
    ]

values: A list of category strings.
