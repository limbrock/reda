Github pages branch for REDA


How to update the documentation
-------------------------------

* switch to master branch and build documentation in *doc/*
* switch to gh-pages branch and run::

	rsync -avz doc/_build/html/ doc_reda/
	git add doc_reda
	git commit -m "update documentation on gh-pages"
