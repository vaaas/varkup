# Varkup

This is a simple markup language that compiles to XML. It's a fusion between XML and S expressions. This reduces syntactic noise and is more pleasant to write manually.

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
