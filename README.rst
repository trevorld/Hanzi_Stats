Hanzi Stats
-----------

.. image:: https://www.repostatus.org/badges/latest/inactive.svg
   :alt: Project Status: Inactive – The project has reached a stable, usable state but is no longer being actively developed; support/maintenance will be provided as time allows.
   :target: https://www.repostatus.org/#inactive

This Anki add-on calculates the number of Hanzi that you have learned so far in the following categories: 

* HSK (2010 aka 2.0) levels
* HSK (2012 aka 2.0) levels
* HSK (2021 aka 3.0) bands
* 6000 most frequently used simplified characters (divided into 12 categories)
* TOCFL (2023) levels
* TBCL (20220920) levels
* 6000 most frequently used traditional characters (divided into 12 categories)

Users can configure which categories are enabled or disabled.  By default in new installations we enable the HSK (2012), HSK (2021), and most frequently used characters categories.

Installation
------------

Anki 2.0.x
~~~~~~~~~~~

To install put the file ``addons/Hanzi_Stats.py`` into the ``addons`` folder in your Anki folder or install using the Anki plugin manager: https://ankiweb.net/shared/info/181243826

Anki 2.1.x
~~~~~~~~~~

To install put the folder ``addons21/Hanzi_Stats`` into the ``addons21`` folder in your Anki folder or install using the Anki plugin manager: https://ankiweb.net/shared/info/181243826 .  If you don't like the defaults the plugin can be further configured by going to "Tools -> Addons" and then clicking on "Hanzi_Stats" and then "Config".

Project Page
------------

https://github.com/trevorld/Hanzi_Stats

History
-------

This is an updated version of the Anki Hanzi Stats plugin by Ben Lickly that could previously be found at https://ankiweb.net/shared/info/296672579.  This version includes the following modifications by Trevor L. Davis:

1. The New HSK (aka v2.0) character lists have been updated from the 2010 version to the 2012 version.
2. Added a new list of the 2021 (aka v3.0) HSK character lists
3. The 6000 most frequent simplified characters in the original plugin have been replaced by the list computed by Dr. Sharoff.  
4. Add a new list of 6000 most frequent traditional characters.
5. By default only looks for characters in the "sort field" instead of all fields.  Which field(s) to look for Hanzi can be configured in the Anki 2.1.x version (Thanks Kyle Waranis for patch).
6. By default clicking character links now sends you to hanzicraft.com instead of dict.cn.  Which URL to look up characters can be configured in the Anki 2.1.x version.
7. Got rid of the HSK A, HSK B, HSK E, and HSK I categories.
8. Fixed some typos.
9. In the Anki 2.1.x version allows users to configure which categories to show.
10. Update the code so it still works when there are non-reversible-compatible changes made to Anki (Thanks Andreas Rücklé for patch).
11. Added new lists for the Taiwanese TOCFL (2023) and TBCL (20220920) wordlists (Thanks Kat Tipton for patch).

This plugin was originally written by Ben Lickly based on Japanese Stats by Damien Elmes.  This modified version also includes a contribution by Kyle Waranis as well as a couple modified code snippets from the Chinese Support plugin by Roland Sieker and Thomas Tempé (which was also based on a plugin by Damien Elmes).

This plugin is available under the GNU GPL, version 3 or later;  http://www.gnu.org/copyleft/gpl.html

Data Notes
----------

``data/HSK-2012-words.txt`` is the export of first sheet from http://files.hskhsk.com/lists/HSK-2012.xls which is supposed to be a copy of the official 2012 new HSK word lists.

``data/HSK-2021-words.csv`` is a csv spreadsheet of two columns of just the word/character and matching HSK band extracted from https://ankiweb.net/shared/info/1144807196 which in turn is supposed to be extracted from the official 2021 HSK word/character lists from http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202103/t20210329_523304.html.

``data/i-zh-char.num.html`` is a character frequency lists from the "Chinese Internet Corpus" compiled by Serge Sharoff in Feb. 2005.  It is available at http://corpus.leeds.ac.uk/query-zh.html.  For more information please read: 

    Sharoff, S. (2006) Creating general-purpose corpora using automated search engine queries. In Marco Baroni and Silvia Bernardini, editors, WaCk y! Working papers on the Web as Corpus. Gedit, Bologna.  http://corpus.leeds.ac.uk/serge/publications/wacky-paper.pdf

``data/traditional_frequency.txt`` is a character frequency list from a corpus of all the BIG-5 Chinese characters that appeared on Usenet newsgroups during 1993-1994 which was compiled by Shih-Kun Huang. It is available at http://technology.chtsai.org/charfreq/

``data/TOCFL-2023-words.csv`` is a csv spreadsheet of two columns of the word and TOCFL level extracted from the official word list at https://tocfl.edu.tw/index.php/exam/download; a machine-friendly copy is available at https://github.com/sneaky-foxes/tocfl (forked from PSeitz/tocfl)

``data/TBCL-20220920-characters.csv`` is a csv spreadsheet extracted from the official TBCL character list from https://coct.naer.edu.tw/standsys/querychar.php?q=&num=4000&page=1&deng_ji=all; a machine-friendly copy is available at https://github.com/sneaky-foxes/tbcl
