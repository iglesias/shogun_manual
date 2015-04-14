from sphinx.directives.code import LiteralInclude
from docutils import nodes
import os
import uuid

def setup(app):
    """
    Set up plugin
    """
    
    app.add_config_value('target_languages', None, True)

    # register functions called upon node-visiting
    app.add_node(sgexample,
            html=(visit_sgexample_node, depart_sgexample_node))
    app.add_node(tabpanel,
            html=(visit_tabpanel_node, depart_tabpanel_node))
    app.add_node(navtabs,
            html=(visit_navtabs_node, depart_navtabs_node))
    app.add_node(navtab,
            html=(visit_navtab_node, depart_navtab_node))
    app.add_node(fluid_tab_content,
            html=(visit_fluid_tab_content, depart_fluid_tab_content))

    app.add_directive('sgexample', ShogunExample)
    app.connect('builder-inited', setup_languages)

    return {'version': '0.1'}

class LocalContext(object):
    pass

context = LocalContext()

def setup_languages(app):
    context.target_languages = app.config.target_languages

# functions called upon node visiting, building tab-structure for examples
def visit_tabpanel_node(self, node):
    self.body.append('<div role="tabpanel">')
def depart_tabpanel_node(self, node):
    self.body.append('</div>')

def visit_navtabs_node(self, node):
    self.body.append('<ul style="display:none" id="tabs-%s" class="nav nav-tabs" role="tablist">' % node.uid)
def depart_navtabs_node(self, node):
    self.body.append('</ul>')

def visit_navtab_node(self, node):
    cls = ""
    if node.index is 0:
        cls = 'class="active"'
    self.body.append('<li role="presentation" id="tab-%s" %s><a href="#%s" aria-controls="%s" role="tab" data-toggle="tab">' % (node.language, cls, node.language, node.language))
def depart_navtab_node(self, node):
    self.body.append('</a></li>')

def visit_fluid_tab_content(self, node):
    self.body.append('<div class="fluid-container tab-content">')
def depart_fluid_tab_content(self, node):
    self.body.append('</div>')

def visit_sgexample_node(self, node):
    cls = ""
    if node.index is 0:
        cls = 'active'
    self.body.append('<div role="tabpanel" class="tab-pane %s" id="%s">' % (cls, node.language))
def depart_sgexample_node(self, node):
    self.body.append('</div>')


class sgexample(nodes.Element):
    pass
class fluid_tab_content(nodes.Element):
    pass
class tabpanel(nodes.Element):
    pass
class navtabs(nodes.Element):
    pass
class navtab(nodes.Element):
    pass

class ShogunExample(LiteralInclude):
    def run(self):
        section = self.arguments[0].split(':')[1]
        self.options['start-after'] = section
        self.options['end-before'] = section
        uid = str(uuid.uuid1())[:6]
	result = tabpanel()
        nvtbs = navtabs()
        nvtbs.uid = uid
        for i, (target, _) in enumerate(context.target_languages):
            nvtb = navtab()
            nvtb.language = target + '-code-' + uid
            nvtb.index = i
            nvtbs += nvtb

        result += nvtbs

	# save original node
        fname = self.arguments[0].split(':')[0].strip()

        tbcntnt = fluid_tab_content()

	# create nodes with parsed listings
	for i, (target, extension) in enumerate(context.target_languages):
            self.arguments[0] = filename_sg_to_target(fname, target, extension)
	    self.options['language'] = target
	    # call base class, returns list
            include_container = sgexample()
            include_container.language = target + '-code-' + uid
            include_container.index = i
	    include_container += LiteralInclude.run(self)
	    tbcntnt += include_container
        result += tbcntnt

	return [result]

def filename_sg_to_target(fname, target, extension):
    # extract filename from unicode
    splitted = str(fname).split(os.sep)
    directory = os.sep.join(splitted[:-1])
    fname_base = splitted[-1][:-3]

    # make sure the format is like "knn.sg"
    if not splitted[-3:] != ".sg":
	raise ValueError("Could not parse example filename \"%s\"" % fname)

    # construct actual code filename
    return os.path.join(directory, target, "%s.%s" % (fname_base, extension))
