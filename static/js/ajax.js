function loadDoc(url) {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			document.getElementById("about_creator").innerHTML =
			this.responseText;
		}
	};
	xhttp.open("GET", url , true);
	xhttp.send();
}
