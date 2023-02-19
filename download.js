<!DOCTYPE html>
<html>
  <head>
    <title>Download converted_data.json</title>
  </head>
  <body>
    <button id="download">Download converted_data.json</button>
    <script>
      document.getElementById('download').addEventListener('click', function(event) {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/media/converted_data.json', true);
        xhr.responseType = 'blob';
        xhr.onload = function(e) {
          if (this.status == 200) {
            var blob = new Blob([this.response], {type: 'application/json'});
            var link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = 'converted_data.json';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
          }
        };
        xhr.send();
      });
    </script>
  </body>
</html>