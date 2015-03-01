# A new Shogun web manual
## aka minimal examples 2.0

We attempt to get documentation such as [sckit's](http://scikit-learn.org/stable/user_guide.html).
We showcase our main strength via allowing users to switch the target language of the code snippets with one click.


# Prototype

The idea is to write a single file such as ```knn.md```.
Those are then locally copied into ```knn_python.md```, ```knn_octave.md```, with lines as

```
\snippet knn.sg	 load_data
```

being transformed into

```
\snippet knn.py	 load_data
```

for the appropriate target language.

Have a look into ```classifier```, where I created such copies by hand. A script would do that in practice.


The file ```classifier/examples/knn.sg``` here contains the meta-language example.
This (with some soon to happen patch) can be easily converted to ```classifier/examples/knn.py```, ```classifier/examples/knn.m``` etc for all target languages. I also included those files for now. See [Esben's meta-language project](https://github.com/sorig/shogun/tree/develop/examples/example-generation).

Run

```
doxygen doxyfile.in . html
```

to get an example output. Look at ```html/page.html```.

In practice, we would now paste these pages together to get a page that contains all listings one after another.
The we add a JavaScript bar that allows users to select their language of choice, hiding all other listings from the html.

# Pipeline
 * We write pages such as ```knn.md```, including snippets from a meta language example ```knn.sg```
 * Some script produces copies such as ```knn_python.md``` which include the python source file for snippets
 * doxygen renders static html pages for all languages
 * (Maybe listings from all pages are copied into a big html file that contains all listings)
 * Some JavaScript header bar allows to switch between the languages while browsing the docs
