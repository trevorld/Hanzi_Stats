## fieldToUseForStats

* ``fieldToUseForStats`` determines the field (or fields) to be used when finding characters to check against the HSK sets. 
* When using "sortField" (default) it will use the 'Sort Field' field as defined in the deck browser.  
* Specifying "all" will use all fields.  
* Specifying a specific field with a number will match the field number found in Manage Note Types -> Fields.  
* values: "sortField", "all", "1", "2", "3", ...

## hanziURL

* ``hanziURL`` determines which website to look hanzi characters up at.  
* Currently the hanzi is appended to the end of the url.  
* Default is "http://hanzicraft.com/character/".  
* values: "http://hanzicraft.com/character/", "http://dict.cn/", "http://characterpop.com/explode/", ...

## categoriesToShow

* ``categoriesToShow`` determines which categories to show Hanzi statistics for.  
* Delete any categories you do not want shown.  
* Default is to show all categories.
* "HSK Level 1" is a reversi-compatible alias for "HSK (2012) Level 1" (similar alias available for Levels 2 through 6).
* values: A list of category strings:
  ```json
  [
  "HSK (2012) Level 1", "HSK (2012) Level 2", "HSK (2012) Level 3",
  "HSK (2012) Level 4", "HSK (2012) Level 5", "HSK (2012) Level 6",
  "HSK (2021) Band 1", "HSK (2021) Band 2", "HSK (2021) Band 3",
  "HSK (2021) Band 4", "HSK (2021) Band 5", "HSK (2021) Band 6",
  "HSK (2021) Bands 7-9",
  "Simplified Top 500", "Simplified Top 1000", "Simplified Top 1500", 
  "Simplified Top 2000", "Simplified Top 2500", "Simplified Top 3000", 
  "Simplified Top 3500", "Simplified Top 4000", "Simplified Top 4500", 
  "Simplified Top 5000", "Simplified Top 5500", "Simplified Top 6000", 
  "Traditional Top 500", "Traditional Top 1000", "Traditional Top 1500", 
  "Traditional Top 2000", "Traditional Top 2500", "Traditional Top 3000", 
  "Traditional Top 3500", "Traditional Top 4000", "Traditional Top 4500", 
  "Traditional Top 5000", "Traditional Top 5500", "Traditional Top 6000",
  "TOCFL (2023) Novice 1", "TOCFL (2023) Novice 2", "TOCFL (2023) 1",
  "TOCFL (2023) 2", "TOCFL (2023) 3", "TOCFL (2023) 4", "TOCFL (2023) 5",
  "TBCL (20220920) 1", "TBCL (20220920) 2", "TBCL (20220920) 3",
  "TBCL (20220920) 4", "TBCL (20220920) 5", "TBCL (20220920) 6",
  "TBCL (20220920) 7",
  "Unlisted"
  ]
  ```
