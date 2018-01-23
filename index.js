function getMarkdown() {
	var reader = new FileReader();
	jQuery.get('log.md', function(data){
		insertMarkdown(data);
	});
}

function updateHtml(html) {
	anchors = html.getElementsByTagName('a');
	console.log(anchors);
	return html;
}

function insertMarkdown(markdown) {
	var converter = new showdown.Converter();
	html = converter.makeHtml(markdown);
	fixedHtml = updateHtml(html);
	document.getElementById("markdown-content").innerHTML = fixedHtml;
}

$(document).ready(function() {
	getMarkdown();
});
