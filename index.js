function getMarkdown() {
	var reader = new FileReader();
	jQuery.get('log.md', function(data){
		insertMarkdown(data);
	});
}

function insertMarkdown(markdown) {
	var converter = new showdown.Converter();
	html = converter.makeHtml(markdown);
	document.getElementById("markdown-content").innerHTML = html;
}

$(document).ready(function() {
	getMarkdown();
});
