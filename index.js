function getMarkdown() {
	var reader = new FileReader();
	jQuery.get('log.md', function(data){
		insertMarkdown(data);
	});
}

function updateHtml(html) {
	var day = 1;
	newHtml = html.replace(/<a href=/g, function() {
		newAnchor = '<a name="r1-d' + day.toString() + '" href=';
		day++;
		return newAnchor;
	});
	return newHtml;
}

function insertMarkdown(markdown) {
	var converter = new showdown.Converter();
	html = converter.makeHtml(markdown);
	fixedHtml = updateHtml(html);
	document.getElementById("markdown-content").innerHTML = fixedHtml;
	jumpToAnchor();
}

$(document).ready(function() {
	getMarkdown();
});

function jumpToAnchor() {
	console.log("Jump to anchor.");
	if (window.location.hash) {
		console.log(window.location.hash);
		window.location.hash = window.location.hash;
	}
}
