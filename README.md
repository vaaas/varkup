# Varkup

This is a simple markup language that compiles to XML. It's a fusion between XML and S expressions. This reduces syntactic noise and is more pleasant to write manually.

## Syntax

- A document is defined as a series of elements.
- Each element is enclosed in angle brackets (`< >`), and it can have children.
- The children of an element are atoms or other elements, separated by whitespace.
- An atom is a string.
- Immediately following the opening bracket of an element (`<`), the first atom defines the element's name.
- Children elements whose name starts with colon (`:`) are considered attributes instead
- Attributes must consist entirely of atoms. Attributes must have at least two atoms.
- The first atom of an attribute is the attribute name, starting wich colon. The rest are its value.

## Examples

The following HTML document:

```xml
<body>
	<nav>
		<a href='page.html'>Page</a>
		<a href='page2.html'>Page 2</a>
	</nav>
	<p>A <em>nice</em> paragraph</p>
</body>
```

Can be written instead as:

```
<body
	<nav
		<a <:href page.html> Page>
		<a <:href page2.html> Page 2>>
	<p A <em nice> paragraph>>
```
