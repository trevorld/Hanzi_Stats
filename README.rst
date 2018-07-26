Hanzi Stats
-----------

.. image:: http://www.repostatus.org/badges/latest/active.svg
   :alt: Project Status: Active – The project has reached a stable, usable state and is being actively developed.
   :target: http://www.repostatus.org/#active

This Anki add-on calculates the number of Hanzi that you have learned so far in the following categories: 

* New HSK levels 
* 6000 most frequently used simplified characters (divided into 12 categories) 
* 6000 most frequently used traditional characters (divided into 12 categories) 

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

1. The New HSK character lists has been updated from the 2010 version to the 2012 version.
2. The 6000 most frequent simplified characters in the original plugin have been replaced by the list computed by Dr. Sharoff.  
3. Add a new list of 6000 most frequent traditional characters.
4. By default only looks for characters in the "sort field" instead of all fields.  Which field(s) to look for Hanzi can be configured in the Anki 2.1.x version (Thanks Kyle Waranis for patch).
5. By default clicking character links now sends you to hanzicraft.com instead of dict.cn.  Which URL to look up characters can be configured in the Anki 2.1.x version.
6. Got rid of the HSK A, HSK B, HSK E, and HSK I categories.
7. Fixed some typos.
8. In the Anki 2.1.x version allows users to configure which categories to show.

This plugin was originally written by Ben Lickly based on Japanese Stats by Damien Elmes.  This modified version also includes a contribution by Kyle Waranis as well as a couple modified code snippets from the Chinese Support plugin by Roland Sieker and Thomas Tempé (which was also based on a plugin by Damien Elmes).

This plugin is available under the GNU GPL, version 3 or later;  http://www.gnu.org/copyleft/gpl.html

Data Notes
----------

``data/HSK-2012-words.txt`` is the export of first sheet from http://files.hskhsk.com/lists/HSK-2012.xls which is supposed to be a copy of the official 2012 new HSK word lists.

``data/i-zh-char.num.html`` is a character frequency lists from the "Chinese Internet Corpus" compiled by Serge Sharoff in Feb. 2005.  It is available at http://corpus.leeds.ac.uk/query-zh.html.  For more information please read: 

    Sharoff, S. (2006) Creating general-purpose corpora using automated search engine queries. In Marco Baroni and Silvia Bernardini, editors, WaCk y! Working papers on the Web as Corpus. Gedit, Bologna.  http://corpus.leeds.ac.uk/serge/publications/wacky-paper.pdf

``data/traditional_frequency.txt`` is a character frequency list from a corpus of all the BIG-5 Chinese characters that appeared on Usenet newsgroups during 1993-1994 which was compiled by Shih-Kun Huang. It is available at http://technology.chtsai.org/charfreq/
