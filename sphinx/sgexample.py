def setup(app):
    app.add_config_value('sgexample_include_examples', False, True)

    app.add_node(sgexample,
            html=(visit_sgexample_node, depart_sgexample_node))
    app.add_node(tabpanel,
            html=(visit_tabpanel_node, depart_tabpanel_node))
    app.add_node(navtabs,
            html=(visit_navtabs_node, depart_navtabs_node))
    app.add_node(navtab,
            html=(visit_navtab_node, depart_navtab_node))

    app.add_directive('sgexample', ShogunExample)

    return {'version': '0.1'}

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

def visit_sgexample_node(self, node):
    cls = ""
    if node.index is 0:
        cls = 'active'
    self.body.append('<div role="tabpanel" class="tab-pane %s" id="%s">' % (cls, node.language))

def depart_sgexample_node(self, node):
    self.body.append('</div>')

from docutils import nodes
class sgexample(nodes.Element):
    pass
class tabpanel(nodes.Element):
    pass
class navtabs(nodes.Element):
    pass
class navtab(nodes.Element):
    pass

from sphinx.directives.code import LiteralInclude
import os
import uuid
class ShogunExample(LiteralInclude):
    def run(self):
        uid = str(uuid.uuid1())[:6]
	result = tabpanel()
        nvtbs = navtabs()
        nvtbs.uid = uid
        for i, (target, _) in enumerate(get_supported_languages()):
            nvtb = navtab()
            nvtb.language = target + '-code-' + uid
            nvtb.index = i
            nvtbs += nvtb

        result += nvtbs

	# save original node
	orig_fname = self.arguments[0].strip()
	orig_language = self.options['language'].strip()

        tbcntnt = nodes.container(classes=['tab-content'])

	# create nodes with parsed listings
	for i, (target, extension) in enumerate(get_supported_languages()):
	    self.arguments[0] = filename_sg_to_target(orig_fname, target, extension)
	    self.options['language'] = target
	    # call base class, returns list
            include_container = sgexample()
            include_container.language = target + '-code-' + uid
            include_container.index = i
	    include_container += LiteralInclude.run(self)
	    tbcntnt += include_container
        result += tbcntnt

	# restore
	self.arguments[0] = orig_fname
	self.options['language'] = orig_language

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

def get_supported_languages():
    return (("python", "py"),
            ("octave", "m"))

    from docutils.statemachine import ViewList
def container_wrapper(directive, literal_node, caption):
    container_node = nodes.container('', literal_block=True,
            classes=['literal-block-wrapper'])
    parsed = nodes.Element()
    directive.state.nested_parse(ViewList([caption], source=''),
            directive.content_offset, parsed)
    caption_node = nodes.caption(parsed[0].rawsource, '',
            *parsed[0].children)
    caption_node.source = parsed[0].source
    caption_node.line = parsed[0].line
    container_node += caption_node
    container_node += literal_node
    return container_node
