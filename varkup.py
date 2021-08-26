import sys, string
whitespace = ' \t\n'

def each(f, xs):
	for x in xs: f(x)

class Parser:
	def __init__(self, xs):
		self.xs = xs
		self.i = 0
		self.len = len(self.xs)

	def next(self):
		if self.done():
			return StopIteration
		else:
			x = self.xs[self.i]
			self.i += 1
			return x

	def peek(self):
		return StopIteration if self.done() else self.xs[self.i]

	def skip(self, i=1):
		self.i += i
		return self

	def revert(self, i=1):
		self.i -= i
		return self

	def done(self): return self.i >= self.len

	def until(self, f):
		while not self.done():
			x = self.next()
			if f(x): return x
		return StopIteration

def main():
	each(print,
	map(serialise,
	map(transform,
	parse(sys.stdin.read()))))

def parse(xs):
	parser = Parser(xs)
	while not parser.done():
		x = parser.next()
		if x in whitespace: continue
		elif x == '<': yield parse_element(parser)
		else: raise Exception('unexpected token ' + str(x))

def parse_element(xs):
	elem = []
	elem.append(parse_element_atom(xs))
	elem.extend(parse_element_contents(xs))
	return elem

def parse_element_atom(xs):
	atom = []
	while not xs.done():
		x = xs.peek()
		if x in whitespace or x == '>':
			if len(atom) > 0: return ''.join(atom)
			else: raise Exception('empty atom')
		elif x == '<':
			raise Exception('unexpected token ' + str(x))
		else:
			atom.append(x)
			xs.skip()
	raise Exception('unexpected end of file')

def parse_element_contents(xs):
	contents = []
	while not xs.done():
		x = xs.next()
		if x in whitespace: continue
		elif x == '>': return contents
		elif x == '<': contents.append(parse_element(xs))
		else: contents.append(parse_element_atom(xs.revert()))
	raise Exception('unexpected end of file')

def transform(x):
	elem = [x[0], [], []]
	for i in x[1:]:
		if type(i) is str:
			elem[2].append(i)
		elif type(i) is list:
			if i[0][0] == ':':
				elem[1].append(transform_attribute(i))
			else:
				elem[2].append(transform(i))
	return elem

def transform_attribute(x):
	val = []
	for i in x[1:]:
		if type(i) is str: val.append(i)
		else: raise Exception('only strings are allowed in attribute values, got: ' + str(i))
	if len(val) == 0:
		raise Exception('empty attributes are not allowed')
	return [x[0][1:], ' '.join(val)]

def serialise(x):
	string = ['<', x[0]]
	if len(x[1]) > 0:
		string.append(' ')
		string.extend(' '.join(map(serialise_attributes, x[1])))
	if len(x[2]) == 0:
		string.append('/>')
	else:
		string.append('>')
		string.append(' '.join(map(serialise_children, x[2])))
		string.append('</')
		string.append(x[0])
		string.append('>')
	return ''.join(string)

def serialise_attributes(x):
	return ''.join([
		x[0],
		'=',
		'"',
		x[1],
		'"',
	])

def serialise_children(x):
	if type(x) is str: return x
	elif type(x) is list: return serialise(x)

main()
