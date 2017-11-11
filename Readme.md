Github pages branch for REDA


How to update the documentation
-------------------------------

* switch to master branch and build documentation in *doc/*
* switch to gh-pages branch and run

::

	rsync -avz doc/_build/html/ documentation/
	git add documentation
	git commit -m "update documentation on gh-pages"
