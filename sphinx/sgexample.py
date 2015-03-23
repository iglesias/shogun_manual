def setup(app):
    app.add_config_value('sgexample_include_examples', False, True)

    app.add_node(sgexample,
				html=(visit_sgexample_node, depart_sgexample_node),
				latex=(visit_sgexample_node, depart_sgexample_node),
				text=(visit_sgexample_node, depart_sgexample_node))

    app.add_directive('sgexample', ShogunExample)

    return {'version': '0.1'}

def visit_sgexample_node(self, node):
    self.visit_admonition(node)

def depart_sgexample_node(self, node):
    self.depart_admonition(node)

from docutils import nodes
class sgexample(nodes.Admonition, nodes.Element):
    pass

from sphinx.directives.code import LiteralInclude
import os
class ShogunExample(LiteralInclude):
	def run(self):
		result = []
		# save original node
		orig_fname = self.arguments[0].strip()
		orig_language = self.options['language'].strip()
		
		# create nodes with parsed listings
		for target in get_supported_languages():
			self.arguments[0] = filename_sg_to_target(orig_fname, target)
			self.options['language'] = target
			
			# call base class, returns list
			result += LiteralInclude.run(self)
		
		# restore
		self.arguments[0] = orig_fname
		self.options['language'] = orig_language
		
		return result

def filename_sg_to_target(fname, target):
	# extract filename from unicode
	splitted = str(fname).split(os.sep)
	directory = os.sep.join(splitted[:-1])
	fname_base = splitted[-1][:-3]

	# make sure the format is like "knn.sg"
	if not splitted[-3:] != ".sg":
		raise ValueError("Could not parse example filename \"%s\"" % fname)

	# construct actual code filename
	suffix = get_language_file_suffix(target)
	return directory + os.sep + target + os.sep + fname_base + "." + suffix

def get_language_file_suffix(target):
	if target == "python":
		return "py"
	elif target == "octave":
		return "m"
	else:
		raise ValueError("Unsupported Shogun target language: %s" % target)

def get_supported_languages():
	return [
			"python",
			"octave",
			]

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