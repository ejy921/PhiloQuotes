async function fetchData() {
  const data = 'page=1&type=Movie&release_year=1975';

  const xhr = new XMLHttpRequest();
  xhr.withCredentials = true;
  
  xhr.addEventListener('readystatechange', function () {
    if (this.readyState === this.DONE) {
      console.log(this.responseText);
    }
  });
  
  xhr.open('POST', 'https://netflix-movies-and-tv-shows1.p.rapidapi.com/list');
  xhr.setRequestHeader('x-rapidapi-key', 'e5507dde33msha9648e4165beb25p10e833jsnaea497132cea');
  xhr.setRequestHeader('x-rapidapi-host', 'netflix-movies-and-tv-shows1.p.rapidapi.com');
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  
  xhr.send(data);
}
fetchData(); 