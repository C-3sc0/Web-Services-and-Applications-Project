// Functions to redirect the user to different pages
function returnToHome(){
    window.location.href = 'project.html';
}
function goToAbout(){
    window.location.href = 'about.html';
}
function goToMDB(){
    window.location.href = 'movie.html';
}
function goToTv(){
    window.location.href = 'tv-show.html';
}
function whishList(){
    window.location.href = 'wish-list.html';
}

function goBack(){
    window.location.href = 'movie.html';
}

//API Movie Details
const API_KEY = 'api_key=fa4eda4583d591db539b12271967147a';
const BASE_MOVIE_URL = 'https://api.themoviedb.org/3';
const API_MOVIE_URL = BASE_MOVIE_URL + '/discover/movie?sort_by=popularity.desc&' + API_KEY;
const IMG_URL = 'https://image.tmdb.org/t/p/w500';
const searchMovieURL = BASE_MOVIE_URL + '/search/movie?'+API_KEY;

//API TV show Details
const BASE_URL = 'https://api.themoviedb.org/3';
const API_URL = BASE_URL + '/trending/tv/week?language=en-US&'+API_KEY;
const searchURL = BASE_URL + '/search/tv?'+API_KEY;



document.addEventListener('DOMContentLoaded', function() {
        const main = document.getElementById('main');
        const form = document.getElementById('form');
        const search = document.getElementById('search');
    });