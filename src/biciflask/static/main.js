let startTime;
let updatedTime;
let difference;
let tInterval;
let running = false;


async function startRider(){
  const response = await fetch("startTimer", {method: 'POST'});
  const rider = await response.json();
  startTime = Math.floor(rider['startTime'])
  token = rider['token']
  window.localStorage.setItem('startTime', startTime)
  window.localStorage.setItem('token', token)
  startTimer()
}

function stopRider(){

  startTime = window.localStorage.getItem('startTime')
    // window.localStorage.setItem('startTime', startTime)
    // const rider = await response.json();

    startTimer()
}




function startTimer() {
  if (!running) {
    // startTime = new Date().getTime();
    tInterval = setInterval(getShowTime, 1);
    running = true;
  }
}

function stopTimer() {
  if (running) {
    clearInterval(tInterval);
    running = false;

    // Aqui es donde nos conectamos de nuevo con el servidor
    fetch("stopTimer", {
      method: 'POST',
      headers: {
      'Content-Type': 'application/json'
      },
      body: JSON.stringify(`${startTime}`)
      }).then(response => response.json())
      .then(data => {
          console.log('Respuesta del servidor:', data);
          // Puedes manejar la respuesta del servidor aquí
      })
      .catch(error => {
          console.error('Error en la solicitud:', error);
      });
    }
}

function resetTimer() {
  clearInterval(tInterval);
  running = false;
  document.getElementById('cronometro').innerHTML = '00:00:00';
}

function getShowTime() {
  updatedTime = new Date().getTime();
  difference = updatedTime - startTime;

  let hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  let minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
  let seconds = Math.floor((difference % (1000 * 60)) / 1000);
  let milliseconds = Math.floor((difference % (1000 * 60)) / 100);

  hours = (hours < 10) ? "0" + hours : hours;
  minutes = (minutes < 10) ? "0" + minutes : minutes;
  seconds = (seconds < 10) ? "0" + seconds : seconds;
  milliseconds = (milliseconds < 100) ? (milliseconds < 10) ? "00" + milliseconds : "0" + milliseconds : milliseconds;

  document.getElementById('cronometro').innerHTML = hours + ':' + minutes + ':' + seconds;
}

