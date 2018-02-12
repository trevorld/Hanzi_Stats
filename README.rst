Hanzi Stats
-----------

This Anki add-on calculates the number of Hanzi (simplified only) that you have learned so far in the following categories: 

* New HSK levels
* 6000 most frequently used characters (divided into 12 categories) 

Installation
------------

Anki 2.0.x
~~~~~~~~~~~

To install put the file ``addons/Hanzi_Stats.py`` into the ``addons`` folder in your Anki folder or install using the Anki plugin manager: https://ankiweb.net/shared/info/181243826

Anki 2.1.x
~~~~~~~~~~

Porting the Hanzi_Stats plugin to Anki 2.1.x is a `work in progress <https://github.com/trevorld/Hanzi_Stats/issues/5>`_.

.. To install put the folder ``addons/Hanzi_Stats`` into the ``addons21`` folder in your Anki folder or install using the Anki plugin manager: 

Project Page
------------

https://github.com/trevorld/Hanzi_Stats

History
-------

This is an updated version of the Anki Hanzi Stats plugin by Ben Lickly that could previously be found at https://ankiweb.net/shared/info/296672579.  This version includes the following modifications by Trevor L. Davis:

#. The New HSK character lists has been updated from the 2010 version to the 2012 version.
#. The 6000 most frequently characters in the original plugin have been replaced by the list computed by Dr. Sharoff.  
#. Only looks for characters in the first field instead of all fields.
#. Clicking character links now sends you to hanzicraft.com instead of dict.cn.
#. Got rid of the HSK A, HSK B, HSK E, and HSK I categories.
#. Fixed some typos.

This plugin was originally written by Ben Lickly based on Japanese Stats by Damien Elmes.  This modified version also includes a couple modified code snippets from the Chinese Support plugin by Roland Sieker and Thomas Tempe (which was also based on a plugin by Damien Elmes).

This plugin is available under the GNU GPL, version 3 or later;  http://www.gnu.org/copyleft/gpl.html

Data Notes
----------

``data/HSK-2012-words.txt`` is the export of first sheet from http://files.hskhsk.com/lists/HSK-2012.xls which is supposed to be a copy of the official 2012 new HSK word lists.

``data/i-zh-char.num.html`` is a character frequency lists from the "Chinese Internet Corpus" compiled by Serge Sharoff in Feb. 2005.  It is available at http://corpus.leeds.ac.uk/query-zh.html.

Details available from:

Sharoff, S. (2006) Creating general-purpose corpora using automated search engine queries. In Marco Baroni and Silvia Bernardini, editors, WaCk y! Working papers on the Web as Corpus. Gedit, Bologna.  http://corpus.leeds.ac.uk/serge/publications/wacky-paper.pdf
